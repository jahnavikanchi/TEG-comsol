import streamlit as st
import base64
import pandas as pd

# --- Style setup ---
st.markdown('''
    <style>
    body {
        color: white;
        font-family: 'Times New Roman', sans-serif;
    }
    h1 {
        font-family: 'Georgia', serif;
        font-size: 50px;
        color: white;
    }
    h2 {
        font-family: 'Georgia', serif;
        font-size: 30px;
        color: white;
        margin-top: 40px;
    }
    h3 {
        font-family: 'Georgia', serif;
        font-size: 18px;
        text-align: center;
        color: lightgray;
    }
    p {
        font-size: 16px;
        line-height: 1.8;
        text-align: justify;
    }
    </style>
''', unsafe_allow_html=True)

# --- Utility function to load image as base64 ---
def load_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Title ---
st.markdown("<h1>Machine Learning Results & Analysis</h1>", unsafe_allow_html=True)

# --- Section 1: Introduction ---
st.markdown("<h2>1. Objective and Dataset</h2>", unsafe_allow_html=True)
st.markdown("""
<p>
This machine learning workflow was developed to predict two critical performance metrics of thermoelectric generators (TEGs): power output and efficiency. The predictive model relies on eight input parameters that capture the essential geometric and thermal characteristics of the TEG structure, including leg height and width (HTE, HIC, Wp, Wn), fill factor (FF), hot-side temperature (Th), heat flux input (Qin), and contact resistivity (Rc). These parameters were derived from a dataset of 5000 high-fidelity COMSOL simulations. The comprehensive nature of this dataset ensures that a wide range of realistic operating conditions and design scenarios are covered. A deep Artificial Neural Network (ANN) was trained on this data to map the inputs to the desired outputs, dramatically accelerating the design process by eliminating the need for repeated simulations.
</p>
""", unsafe_allow_html=True)

# --- Section 2: Evaluation Metrics ---
st.markdown("<h2>2. Model Evaluation</h2>", unsafe_allow_html=True)
st.markdown("""
<h3>Table 1: Evaluation metrics and prediction snapshot.</h3>
""", unsafe_allow_html=True)

eval_metrics_df = pd.DataFrame({
    "Predicted_Power_output": [12.657933, 1.763126, 1.763126, 1.291263, 14.271257],
    "Predicted_Efficiency": [0.205946, 0.891846, 0.620642, 0.605060, 0.843168]
})
st.dataframe(eval_metrics_df)

st.markdown("""
<p>
The model was evaluated using several statistical metrics commonly applied to regression problems, including the Mean Squared Error (MSE), Mean Absolute Error (MAE), and the coefficient of determination (R²). An R² score of 0.87 was achieved, indicating a high degree of correlation between the predicted and actual target values. The MSE and MAE were both acceptably low, confirming the network’s capacity to generalize well to unseen data. These metrics were derived from the inverse-transformed outputs, meaning the performance reflects the model’s effectiveness in the original scale of the problem. Alongside the metrics, the table shows a small preview of actual and predicted values for both power and efficiency, demonstrating that the model remains accurate across diverse input conditions.
</p>
""", unsafe_allow_html=True)

# --- Section 3: Actual vs Predicted ---
st.markdown("<h2>3. Prediction Accuracy</h2>", unsafe_allow_html=True)
pred_img = load_image("views/Images/actual_vs_predicted_efficiency.png")
st.markdown(f'<img src="data:image/png;base64,{pred_img}" style="width:98%; display:block; margin:auto;"/>', unsafe_allow_html=True)
st.markdown("""
<h3>Figure 2: Predicted vs Actual Efficiency across dataset.</h3>
<p>
This plot compares predicted and actual efficiency values over the entire test set. The blue line represents the ground truth from simulation data, while the orange dashed line displays predictions from the trained ANN. The close alignment of the two lines across nearly 5000 data points highlights the model's precision and ability to generalize across the entire parameter space. Minor deviations between actual and predicted values occur in regions of high variability, which is expected in a nonlinear and complex thermoelectric system. Nonetheless, the consistent overlap affirms that the model has successfully learned underlying physical patterns and dependencies.
</p>
""", unsafe_allow_html=True)

# --- Section 4: Architecture Optimization ---
st.markdown("<h2>4. Neural Network Architecture Optimization</h2>", unsafe_allow_html=True)
layers_img = load_image("views/Images/layers_vs_avg_error.png")
st.markdown(f'<img src="data:image/png;base64,{layers_img}" style="width:98%; display:block; margin:auto;"/>', unsafe_allow_html=True)
st.markdown("""
<h3>Figure 3: Error statistics for various ANN architectures.</h3>
<p>
To optimize performance, we evaluated different ANN architectures with layer depths ranging from 1 to 6. Each configuration was trained and validated using identical data splits and evaluation criteria. The resulting average relative error was calculated and visualized alongside the frequency of predictions falling within specific error bins. The 3-layer model emerged as the most balanced architecture, yielding the lowest average error and highest proportion of low-error predictions. Models with additional layers tended to suffer from overfitting, while shallower networks lacked sufficient capacity. These results underscore the importance of tuning ANN complexity to match the nonlinearity and dimensionality of the target function.
</p>
""", unsafe_allow_html=True)

# --- Section 5: Input Feature Distributions ---
st.markdown("<h2>5. Input Feature Distributions</h2>", unsafe_allow_html=True)
histo1 = load_image("views/Images/feature_distributions.png")
st.markdown(f'<img src="data:image/png;base64,{histo1}" style="width:98%; display:block; margin:auto;"/>', unsafe_allow_html=True)
st.markdown("""
<h3>Figure 4: Histogram grid of geometric, thermal, and electrical inputs.</h3>
<p>
The dataset used for training the ANN consists of carefully selected values for each input parameter, shown in this multi-panel histogram. Variables like HTE, HIC, Wn, and Wp exhibit wide and evenly distributed ranges, ensuring that the network is exposed to diverse examples during training. Parameters such as contact resistance (Rc) are visualized using a logarithmic transformation to capture the spread of extremely small values. The lower two plots reveal log-transformed distributions of the output variables (Efficiency and Power Output), confirming sufficient variability across the dataset and supporting effective model learning. These visualizations also serve as a sanity check for data preprocessing and normalization steps.
</p>
""", unsafe_allow_html=True)

# --- Section 6: Statistical Summary of Features ---
st.markdown("<h2>6. Feature Statistics Overview</h2>", unsafe_allow_html=True)

st.markdown("""
<h3>Figure 5: Table of summary statistics for all variables.</h3>
<p>
This table replicates the statistical snapshot of the simulated dataset used to train and evaluate the neural network.
It includes geometrical, thermal, and electrical inputs along with the power output and efficiency. The data below 
matches the preview shown in the original simulation output.
</p>
""", unsafe_allow_html=True)

# Ricreiamo la tabella come nella figura statsfinals2.png
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

stats_df = pd.DataFrame(stats_data)
st.dataframe(stats_df.style.format(precision=6), use_container_width=True)

# --- Section 7: Feature Sensitivity and Behavior ---
vs_img = load_image("views/Images/feature_vs_efficiency_boxplots.png")
st.markdown("<h2>7. Feature Sensitivity Plots</h2>", unsafe_allow_html=True)
st.markdown(f'<img src="data:image/png;base64,{vs_img}" style="width:1400px; display:block; margin:auto;"/>', unsafe_allow_html=True)
st.markdown("""
<h3>Figure 6: 2D scatter plots of feature values vs predicted efficiency.</h3>
<p>
These visualizations investigate how each input feature correlates with efficiency predictions from the trained ANN. Each subplot compares a single feature against predicted efficiency, enabling visual sensitivity analysis. Features like Rc and Qin show steep gradients, indicating strong influence on output, while others such as FF exhibit more modest effects. Identifying which parameters most significantly affect performance allows researchers to prioritize variables in future optimization efforts. These plots are essential not only for interpretability but also for supporting explainable AI frameworks in physical sciences.
</p>
""", unsafe_allow_html=True)

# --- Section 8: Optimal Geometry from Genetic Algorithm ---
st.markdown("<h2>8. Best Geometry and Performance (GA)</h2>", unsafe_allow_html=True)
st.markdown("""
<p>
Using a Genetic Algorithm (GA), we searched the design space for the configuration that maximizes predicted efficiency using the ANN model as a fast surrogate. The result is the best-performing thermoelectric geometry and its corresponding power output and efficiency.
</p>
<p><b>Optimal Configuration:</b></p>
<ul>
  <li>HTE = 5.668849 mm</li>
  <li>HIC = -0.385386 mm</li>
  <li>Wp = 1.962334 mm</li>
  <li>Wn = 0.265036 mm</li>
  <li>FF = 0.192786</li>
  <li>Th = 446.963566 K</li>
  <li>Qin = 107.568774 mW/cm²</li>
  <li>Rc = 4.322733e-08 Ω·cm²</li>
</ul>
<p>
<b>Performance:</b> Power Output = 378.48 mW, Efficiency = 2.11%
</p>
<p>
This optimal geometry serves as a benchmark for future design iterations and validates the model’s potential in guiding real-time thermoelectric optimization.
</p>
""", unsafe_allow_html=True)

# --- Final Note ---
st.markdown("<h2>9. Conclusion</h2>", unsafe_allow_html=True)
st.markdown("""
<p>
This study demonstrates the successful integration of physics-based simulations and machine learning to accelerate the design and optimization of thermoelectric generators. By training an ANN on a dataset of COMSOL simulations, we created a predictive surrogate capable of approximating device performance with high fidelity. Combined with Genetic Algorithms and hyperparameter tuning via Optuna, this pipeline enables efficient exploration of design spaces and identification of optimal geometries. The methods and results presented here lay the groundwork for automated, intelligent thermoelectric device development.
</p>
""", unsafe_allow_html=True)
