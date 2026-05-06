import os
import subprocess
import csv

#Paths_directory
template_path = 'template_path'
geometry_dir = "geometry_case_folder"
output_dir = "output_folder"


def load_parameters(file_path):
    """
    Load parameters from a file, ignoring blank lines and comments.
    Supports both 'key=value' and 'key value' formats.
    """
    keys, values = [], []
    with open(file_path, 'r') as file:
        for line in file:
            # Ignore comments and blank lines
            stripped = line.strip()
            if stripped:
                if '=' in stripped:
                    # For key=value format
                    key, value = stripped.split('=', 1)
                elif ' ' in stripped:
                    # For key value format
                    key, value = stripped.split(maxsplit=1)
                else:
                    print(f"⚠️ Skipping invalid line in {file_path}: {line.strip()}")
                    continue

                keys.append(key.strip())
                values.append(value.strip())
            else:
                print(f"⚠️ Skipping blank line in {file_path}")
                
    return keys, values


def comsol_run_case(case_id, template_path, params_dir, output_dir):
    """
    Run a COMSOL case using the specified template and parameters.
    """
    # Paths
    input_file = os.path.abspath(template_path)
    output_file = os.path.join(output_dir, f'case_{case_id}.mph')
    params_file = os.path.join(params_dir, f'params_case_{case_id}.txt')

    print(f"🔍 Input File: {input_file}")
    print(f"🔍 Output File: {output_file}")
    print(f"🔍 Params File: {params_file}")

    # Load parameters
    keys, values = load_parameters(params_file)
    pname = ",".join(keys)
    plist = ",".join(values)

    # Run COMSOL simulation
    print(f"🚀 Running case {case_id}...")
    try:
        subprocess.run([
            r"C:\Program Files\COMSOL\COMSOL63\Multiphysics\bin\win64\comsolbatch.exe",
            "-inputfile", input_file,
            "-outputfile", output_file,
            "-study", "std1",
            "-pname", pname,
            "-plist", plist
        ], check=True)  # Remove shell=True for better security
    except subprocess.CalledProcessError as e:
        print(f"❌ COMSOL failed for case {case_id} with error: {e}")
        return [case_id, ";".join(keys), "Error", "Error"]

    # Extract results
    V, T = extract_results(case_id, output_file)
    return [case_id, ";".join([f"{k}={v}" for k, v in zip(keys, values)]), V, T]

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Prepare the summary data
all_results = []
for case_id in range(5000):  # Use a smaller range for testing if needed
    results = comsol_run_case(case_id, template_path, geometry_dir, output_dir)
    all_results.append(results)
    print(f"✅ Case {case_id} finished.")

print("✅ All cases processed")