# HCL-Hackaton-Team-DS

# Time Series Sales Forecasting Project

## 🎯 Project Overview and Objectives

This project is a comprehensive solution for time series forecasting, focusing on ingesting structured sales data, conducting in-depth analysis, developing and evaluating robust forecasting models (ARIMA and SARIMA), and exposing the final model for practical use. The primary goal is to predict future sales with a horizon of 3 months to support strategic planning and inventory management.

The core objectives addressed in this project are:

1.  **Ingests and preprocesses structured data:** Clean, transform, and prepare the raw sales data for time series analysis.
2.  **Perform exploratory data analysis (EDA) and visualize distributions:** Understand the data structure, identify trends, seasonality, and stationarity, and visualize key metrics.
3.  **Identify correlations and relevant features:** Determine the relationship between sales and other exogenous variables (e.g., holidays, promotions, lagged values).
4.  **Trains, optimizes, and evaluates a forecasting model:** Implement and tune statistical time series models like ARIMA and SARIMA.
5.  **Set a forecast horizon of 3 months:** Generate predictions for the next 90 days following the end of the historical data.
6.  **Exposes the model through an API or simple UI:** Create a functional interface for users to input a date range and receive a sales forecast.
7.  **Generates insights and visual explanations about predictions and how many are done:** Provide a clear breakdown of the model's performance, the confidence intervals of predictions, and business-relevant takeaways.

## 📁 Project Structure

The project utilizes a clear, modular structure for data processing, analysis, and modeling.

| File Name | Description |
| :--- | :--- |
| `FINAL_DATASET_3ys.csv` | The raw, structured dataset containing 3 years of daily sales transactions and related features. |
| `eda_of_Synthetic_Code.ipynb` | Jupyter notebook for **Exploratory Data Analysis (EDA)**. Contains initial data quality checks, statistical summaries, and time series visualizations (trend, seasonality, noise decomposition). |
| `arima1.ipynb` | Jupyter notebook for **ARIMA Modeling**. Focuses on classical ARIMA for non-seasonal time series forecasting, including stationarity testing (e.g., ADF test), model selection, fitting, and 3-month forecasting. |
| `sarima.ipynb` | Jupyter notebook for **SARIMA Modeling**. Focuses on Seasonal Auto-Regressive Integrated Moving Average to capture periodic patterns (e.g., weekly or monthly seasonality). Includes model optimization (e.g., using `auto_arima`). |
| `model_api.py` (Hypothetical) | Python script for the API/UI. Loads the best-performing model (`arima_model.joblib` or `sarima_model.joblib`) and serves predictions via a framework like Flask or Streamlit. |
| `requirements.txt` (Hypothetical) | List of required Python packages and their versions (e.g., `pandas`, `numpy`, `statsmodels`, `pmdarima`, `scikit-learn`, `flask`/`streamlit`). |

## 🛠️ Methodology and Implementation

### 1. Data Ingestion & Preprocessing

* **Ingestion:** The `FINAL_DATASET_3ys.csv` is loaded using `pandas`.
* **Time Series Indexing:** The `date` column is converted to a datetime object and set as the index.
* **Aggregation:** Transactional data is aggregated to the required frequency (e.g., daily total sales) for time series analysis.
* **Feature Handling:** Missing values are addressed, and categorical features are appropriately encoded if used as exogenous variables in a SARIMAX model.

### 2. Exploratory Data Analysis (EDA)

The `eda_of_Synthetic_Code.ipynb` notebook performs a deep dive into the sales data:
* **Trend and Seasonality:** Time series plots are generated to visually inspect long-term trends and recurring seasonal patterns.
* **Distribution Analysis:** Histograms and box plots are used to visualize the distribution of `total_sales` and check for outliers.
* **Stationarity Check:** The Augmented Dickey-Fuller (ADF) test is performed to determine if the time series is stationary, guiding the choice of the differencing order (**d**) for the ARIMA/SARIMA models.

### 3. Feature Identification and Correlation

* Features like `promotion_flag`, `festival_flag`, `holiday_flag`, `lag_7`, and `rolling_mean_7` are analyzed for their correlation with `total_sales`.
* Lagged values (`lag_1`, `lag_7`, `lag_30`) and rolling statistics (`rolling_mean_7`, `rolling_mean_30`) are crucial for time series prediction and are confirmed to be highly relevant.
* Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots are generated to systematically identify the appropriate lag orders (**p** and **q**) for the models.

### 4. Modeling, Optimization, and Evaluation

The core forecasting is done using statistical time series models:

| Model | Notebook | Purpose | Key Metric | Forecast Horizon |
| :--- | :--- | :--- | :--- | :--- |
| **ARIMA** | `arima1.ipynb` | Models non-seasonal time series after differencing. | RMSE / MAE | **3 Months (90 Days)** |
| **SARIMA** | `sarima.ipynb` | Accounts for both non-seasonal and seasonal components (e.g., daily/weekly seasonality). | AIC / BIC | **3 Months (90 Days)** |

* **Model Training:** The time series data is split into training and testing sets.
* **Optimization:** `auto_arima` is used in the SARIMA notebook to automatically select the optimal $$(p, d, q) \times (P, D, Q)_s$$ order based on the lowest AIC/BIC.
* **Evaluation:** Models are evaluated on the test set using standard metrics: **Root Mean Squared Error (RMSE)** and **Mean Absolute Error (MAE)**.
* **Persistence:** The final, optimized model (e.g., `sarima_model.joblib`) is saved for deployment.

### 5. Model Deployment (API/UI)

The final trained model is exposed to make predictions accessible:

* **API (Recommended):** A lightweight API (e.g., using **Flask** or **FastAPI**) is set up to load the saved model. A `POST` endpoint would accept a start date and end date and return the 3-month sales forecast in JSON format.
* **UI (Alternative):** A simple user interface (e.g., using **Streamlit**) can be implemented to allow users to select the forecast horizon and instantly visualize the predicted sales curve.

### 6. Results and Insights

The final stage provides clear interpretability of the model's output:

* **Visual Explanations:** A plot is generated showing the historical actual sales, the model's fitted values, and the **3-month forecast** with **Confidence Intervals**. 
* **Insights:**
    * **Performance:** A summary of the achieved RMSE/MAE is provided. (e.g., "The SARIMA model achieved an RMSE of 129.25 on the test set.")
    * **Forecasting Count:** The total number of predictions generated is clearly stated (e.g., "A total of 90 sales predictions were generated for the 3-month horizon.")
    * **Model Interpretation:** Key statistical findings, such as the significance of seasonal components or the impact of external variables, are highlighted.
