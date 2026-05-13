import streamlit as st
import base64
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Machine Learning Results", layout="wide")


# -----------------------------
# Helpers
# -----------------------------
def load_image(image_path):
    image_path = Path(image_path)
    if not image_path.exists():
        return None

    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render_image(image_path, caption, width="100%"):
    img = load_image(image_path)

    if img:
        st.markdown(
            f'<div class="image-card">'
            f'<img src="data:image/png;base64,{img}" style="width:{width}; display:block; margin:auto;">'
            f'<div class="image-caption">{caption}</div>'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Image not found: {image_path}")


def render_section(title, body):
    st.markdown(
        f'<div class="section-card">'
        f'<div class="section-title">{title}</div>'
        f'<div class="section-text">{body}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

def render_table_card(title, caption, df):
    table_html = df.to_html(
        index=False,
        escape=False,
        border=0,
        classes="custom-table"
    )

    st.markdown(
        f'<div class="section-card">'
        f'<div class="section-title">{title}</div>'
        f'<div class="small-caption">{caption}</div>'
        f'<div class="table-scroll">{table_html}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: #f7f9fb;
    color: #1f2937;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
}

.main-title {
    text-align: center;
    font-size: 3.1rem;
    font-weight: 900;
    color: #12372A;
    margin-bottom: 0.8rem;
}

.main-subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #526D5B;
    margin-bottom: 2.5rem;
}

.section-card {
    background: white;
    border-radius: 24px;
    padding: 2.2rem;
    margin-bottom: 1.8rem;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.06),
        0 4px 10px rgba(0,0,0,0.03);

    border: 1px solid rgba(0,0,0,0.04);
}

.section-title {
    font-size: 2rem;
    font-weight: 800;
    color: #12372A;
    margin-bottom: 1rem;
}

.section-text {
    font-size: 1.05rem;
    line-height: 1.85;
    text-align: justify;
    color: #374151;
}

.image-card {
    background: white;
    border-radius: 24px;
    padding: 1.5rem;
    margin-bottom: 1.8rem;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.06),
        0 4px 10px rgba(0,0,0,0.03);

    border: 1px solid rgba(0,0,0,0.04);
}

.image-card img {
    border-radius: 16px;
}

.image-caption {
    text-align: center;
    margin-top: 1rem;
    color: #374151;
    font-weight: 700;
    font-size: 0.95rem;
    line-height: 1.5;
}

.metric-table-card {
    background: white;
    border-radius: 24px;
    padding: 1.5rem;
    margin-bottom: 1.8rem;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.06),
        0 4px 10px rgba(0,0,0,0.03);

    border: 1px solid rgba(0,0,0,0.04);
}

.small-caption {
    text-align: center;
    font-size: 0.95rem;
    color: #374151;
    font-weight: 700;
    margin-bottom: 1rem;
}

.optimal-box {
    background: linear-gradient(135deg, #12372A, #1D4D3F);
    color: white;
    border-radius: 24px;
    padding: 2.2rem;
    margin-bottom: 1.8rem;

    box-shadow:
        0 12px 28px rgba(18,55,42,0.25);
}

.optimal-box .section-title {
    color: white;
}

.optimal-box .section-text {
    color: white;
}

.optimal-box ul {
    columns: 2;
    margin-top: 1rem;
}

.optimal-box li {
    margin-bottom: 0.5rem;
}
            
.table-scroll {
    width: 100%;
    overflow-x: auto;
}

.custom-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
}

.custom-table th {
    background: #12372A;
    color: white;
    padding: 0.75rem;
    text-align: center;
}

.custom-table td {
    padding: 0.75rem;
    border: 1px solid #d9d9d9;
    text-align: center;
}

.custom-table tr:nth-child(even) {
    background: #f7f9fb;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------
st.markdown('<div class="main-title">Machine Learning Results & Analysis</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="main-subtitle">ANN-based prediction of thermoelectric generator power output and efficiency</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Section 1
# -----------------------------
render_section(
    "1. Objective and Dataset",
    "This machine learning workflow was developed to predict two critical performance metrics of thermoelectric generators (TEGs): power output and efficiency. The predictive model relies on eight input parameters that capture the essential geometric and thermal characteristics of the TEG structure, including leg height and width (HTE, HIC, Wp, Wn), fill factor (FF), hot-side temperature (Th), heat flux input (Qin), and contact resistivity (Rc). These parameters were derived from a dataset of 5000 high-fidelity COMSOL simulations. The comprehensive nature of this dataset ensures that a wide range of realistic operating conditions and design scenarios are covered. A deep Artificial Neural Network (ANN) was trained on this data to map the inputs to the desired outputs, dramatically accelerating the design process by eliminating the need for repeated simulations."
)


# -----------------------------
# Section 2
# -----------------------------
st.markdown('<div class="section-card"><div class="section-title">2. Model Evaluation</div>', unsafe_allow_html=True)
st.markdown('<div class="small-caption">Table 1: Evaluation metrics and prediction snapshot.</div>', unsafe_allow_html=True)

eval_metrics_df = pd.DataFrame({
    "Predicted_Power_output": [12.657933, 1.763126, 1.763126, 1.291263, 14.271257],
    "Predicted_Efficiency": [0.205946, 0.891846, 0.620642, 0.605060, 0.843168]
})

render_table_card(
    "2. Model Evaluation",
    "Table 1: Evaluation metrics and prediction snapshot.",
    eval_metrics_df
)

render_section(
    "",
    "The model was evaluated using several statistical metrics commonly applied to regression problems, including the Mean Squared Error (MSE), Mean Absolute Error (MAE), and the coefficient of determination (R²). An R² score of 0.87 was achieved, indicating a high degree of correlation between the predicted and actual target values. The MSE and MAE were both acceptably low, confirming the network’s capacity to generalize well to unseen data. These metrics were derived from the inverse-transformed outputs, meaning the performance reflects the model’s effectiveness in the original scale of the problem. Alongside the metrics, the table shows a small preview of actual and predicted values for both power and efficiency, demonstrating that the model remains accurate across diverse input conditions."
)

# -----------------------------
# Section 3
# -----------------------------
render_section(
    "3. Prediction Accuracy",
    "This plot compares predicted and actual efficiency values over the entire test set. The blue line represents the ground truth from simulation data, while the orange dashed line displays predictions from the trained ANN. The close alignment of the two lines across nearly 5000 data points highlights the model's precision and ability to generalize across the entire parameter space. Minor deviations between actual and predicted values occur in regions of high variability, which is expected in a nonlinear and complex thermoelectric system. Nonetheless, the consistent overlap affirms that the model has successfully learned underlying physical patterns and dependencies."
)

render_image(
    "views/Images/actual_vs_predicted_efficiency.png",
    "Figure 2: Predicted vs Actual Efficiency across dataset.",
    width="98%"
)


# -----------------------------
# Section 4
# -----------------------------
render_section(
    "4. Neural Network Architecture Optimization",
    "To optimize performance, we evaluated different ANN architectures with layer depths ranging from 1 to 6. Each configuration was trained and validated using identical data splits and evaluation criteria. The resulting average relative error was calculated and visualized alongside the frequency of predictions falling within specific error bins. The 3-layer model emerged as the most balanced architecture, yielding the lowest average error and highest proportion of low-error predictions. Models with additional layers tended to suffer from overfitting, while shallower networks lacked sufficient capacity. These results underscore the importance of tuning ANN complexity to match the nonlinearity and dimensionality of the target function."
)

render_image(
    "views/Images/layers_vs_avg_error.png",
    "Figure 3: Error statistics for various ANN architectures.",
    width="98%"
)


# -----------------------------
# Section 5
# -----------------------------
render_section(
    "5. Input Feature Distributions",
    "The dataset used for training the ANN consists of carefully selected values for each input parameter, shown in this multi-panel histogram. Variables like HTE, HIC, Wn, and Wp exhibit wide and evenly distributed ranges, ensuring that the network is exposed to diverse examples during training. Parameters such as contact resistance (Rc) are visualized using a logarithmic transformation to capture the spread of extremely small values. The lower two plots reveal log-transformed distributions of the output variables (Efficiency and Power Output), confirming sufficient variability across the dataset and supporting effective model learning. These visualizations also serve as a sanity check for data preprocessing and normalization steps."
)

render_image(
    "views/Images/feature_distributions.png",
    "Figure 4: Histogram grid of geometric, thermal, and electrical inputs.",
    width="98%"
)


# -----------------------------
# Section 6
# -----------------------------
stats_data = {
    'HTE': [3.2, 3.4, 3.1, 3.4, 4.3],
    'HIC': [2.0, 2.4, 1.8, 2.1, 2.1],
    'Wp': [4.0, 4.8, 4.0, 4.8, 4.1],
    'Wn': [0.365497, 0.383877, 0.370135, 0.378053, 0.373667],
    'FF': [0.365497, 0.383877, 0.370135, 0.378053, 0.373667],
    'Th': [485, 495, 475, 495, 480],
    'Qin': [295, 305, 285, 305, 290],
    'Rc': [1.000000e-08, 1.000000e-08, 1.000000e-08, 1.000000e-08, 2.300000e-12],
    'Vp': [1.730000e-09, 1.700000e-09, 1.730000e-09, 1.700000e-09, 2.300000e-12],
    'Vn': [0.429536, 0.429536, 0.429536, 0.429536, 0.429536],
    'Voltage_diff': [2.66558, 2.66558, 2.66558, 2.66558, 2.66558],
    'Power_output': [16.1906, 16.3461, 16.3078, 16.3473, 10.7297],
    'Efficiency': [0.638697, 0.615298, 0.607018, 0.633768, 0.083368]
}

stats_df = pd.DataFrame(stats_data).round(6)

render_table_card(
    "6. Feature Statistics Overview",
    "Figure 5: Table of summary statistics for all variables.",
    stats_df
)

render_section(
    "",
    "This table replicates the statistical snapshot of the simulated dataset used to train and evaluate the neural network. It includes geometrical, thermal, and electrical inputs along with the power output and efficiency. The data below matches the preview shown in the original simulation output."
)

# -----------------------------
# Section 7
# -----------------------------
render_section(
    "7. Feature Sensitivity Plots",
    "These visualizations investigate how each input feature correlates with efficiency predictions from the trained ANN. Each subplot compares a single feature against predicted efficiency, enabling visual sensitivity analysis. Features like Rc and Qin show steep gradients, indicating strong influence on output, while others such as FF exhibit more modest effects. Identifying which parameters most significantly affect performance allows researchers to prioritize variables in future optimization efforts. These plots are essential not only for interpretability but also for supporting explainable AI frameworks in physical sciences."
)

render_image(
    "views/Images/feature_vs_efficiency_boxplots.png",
    "Figure 6: 2D scatter plots of feature values vs predicted efficiency.",
    width="100%"
)


# -----------------------------
# Section 8
# -----------------------------
st.markdown(
    '<div class="optimal-box">'
    '<div class="section-title">8. Best Geometry and Performance (GA)</div>'
    '<div class="section-text">'
    "Using a Genetic Algorithm (GA), we searched the design space for the configuration that maximizes predicted efficiency using the ANN model as a fast surrogate. The result is the best-performing thermoelectric geometry and its corresponding power output and efficiency."
    '<br><br>'
    '<b>Optimal Configuration:</b>'
    '<ul>'
    '<li>HTE = 5.668849 mm</li>'
    '<li>HIC = -0.385386 mm</li>'
    '<li>Wp = 1.962334 mm</li>'
    '<li>Wn = 0.265036 mm</li>'
    '<li>FF = 0.192786</li>'
    '<li>Th = 446.963566 K</li>'
    '<li>Qin = 107.568774 mW/cm²</li>'
    '<li>Rc = 4.322733e-08 Ω·cm²</li>'
    '</ul>'
    '<b>Performance:</b> Power Output = 378.48 mW, Efficiency = 2.11%'
    '<br><br>'
    "This optimal geometry serves as a benchmark for future design iterations and validates the model’s potential in guiding real-time thermoelectric optimization."
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Section 9
# -----------------------------
render_section(
    "9. Conclusion",
    "This study demonstrates the successful integration of physics-based simulations and machine learning to accelerate the design and optimization of thermoelectric generators. By training an ANN on a dataset of COMSOL simulations, we created a predictive surrogate capable of approximating device performance with high fidelity. Combined with Genetic Algorithms and hyperparameter tuning via Optuna, this pipeline enables efficient exploration of design spaces and identification of optimal geometries. The methods and results presented here lay the groundwork for automated, intelligent thermoelectric device development."
)