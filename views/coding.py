import pandas as pd
from itertools import product

# Function for calculating power, voltage, and resistance of a material pair with geometric parameters
def calculate_thermoelectric_properties(p_type, n_type, delta_t=100, length=0.01, width=0.005, height=0.005):
    # Difference of Seebeck coefficients
    alpha_pair = abs(p_type["seebeck_coefficient"] - n_type["seebeck_coefficient"]) * 1e-6  # Conversion to V/K
    
    # Cross-sectional area (m^2)
    A = width * height
    
    # Electrical resistance for each leg
    r_p = (1 / p_type["electrical_conductivity"]) * (length / A)
    r_n = (1 / n_type["electrical_conductivity"]) * (length / A)
    
    # Total electrical resistance
    r_total = r_p + r_n
    
    # Maximum power output calculation
    power_max = (alpha_pair**2 * delta_t**2) / (4 * r_total)
    
    # Voltage calculation
    voltage = alpha_pair * delta_t
    
    return power_max, voltage, r_total

# Import data
file_path = r"C:\Users\Виолетта\Desktop\stuff for thr E progect\estm_pr.xlsx"
data = pd.read_excel(file_path)

data.columns = data.columns.str.strip()

# Filtering materials by temperature below 500K
low_temp_materials = data[data["temperature"] < 500]

# Splitting into n-type and p-type
n_type_materials = low_temp_materials[low_temp_materials["seebeck_coefficient"] < 0]
p_type_materials = low_temp_materials[low_temp_materials["seebeck_coefficient"] > 0]

# Generation of all possible pairs (p-type and n-type)
pairs = [(p[1], n[1]) for p, n in product(p_type_materials.iterrows(), n_type_materials.iterrows())]

# Calculation for each pair
results = []
for p_material, n_material in pairs:
    power, voltage, resistance = calculate_thermoelectric_properties(p_material, n_material)
    results.append({
        "p_type_formula": p_material["Formula"],
        "n_type_formula": n_material["Formula"],
        "power_output": power,
        "voltage": voltage,
        "total_resistance": resistance,
        "p_seebeck": p_material["seebeck_coefficient"],  # Add Seebeck coefficient for p-type
        "n_seebeck": n_material["seebeck_coefficient"],  # Add Seebeck coefficient for n-type
        "p_conductivity": p_material["electrical_conductivity"],  # Add conductivity for p-type
        "n_conductivity": n_material["electrical_conductivity"],  # Add conductivity for n-type
        "p_temperature": p_material["temperature"],  # Add temperature for p-type
        "n_temperature": n_material["temperature"]   # Add temperature for n-type
    })

# DataFrame
results_df = pd.DataFrame(results)

# Eliminate duplicate pairs
max_power_pairs = []
used_materials = set()

# p-type
for p_material in p_type_materials.iterrows():
    p_material = p_material[1]
    p_pairs = results_df[results_df["p_type_formula"] == p_material["Formula"]]
    if not p_pairs.empty:
        max_power_pair = p_pairs.loc[p_pairs["power_output"].idxmax()]
        if max_power_pair["n_type_formula"] not in used_materials:
            max_power_pairs.append(max_power_pair)
            used_materials.add(max_power_pair["p_type_formula"])
            used_materials.add(max_power_pair["n_type_formula"])

# n-type
for n_material in n_type_materials.iterrows():
    n_material = n_material[1]
    if n_material["Formula"] not in used_materials:
        n_pairs = results_df[results_df["n_type_formula"] == n_material["Formula"]]
        if not n_pairs.empty:
            max_power_pair = n_pairs.loc[n_pairs["power_output"].idxmax()]
            if max_power_pair["p_type_formula"] not in used_materials:
                max_power_pairs.append(max_power_pair)
                used_materials.add(max_power_pair["p_type_formula"])
                used_materials.add(max_power_pair["n_type_formula"])

# Creating a DataFrame with final results
final_results = pd.DataFrame(max_power_pairs)

# Sorting by power and outputting the top 10 pairs
final_results_sorted = final_results.sort_values(by="power_output", ascending=False)

# Top 10 couples
top_10_pairs = final_results_sorted.head(10)
print(top_10_pairs)