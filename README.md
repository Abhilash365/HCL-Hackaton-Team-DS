

# 📈 Synthetic Sales Forecasting Engine

## 📖 Overview

This project focuses on forecasting future sales trends using time series analysis. We generated a comprehensive synthetic dataset with custom features, stored it in a SQLite database, and built predictive models to forecast sales for the upcoming quarter (3 months).

The project evolves from univariate models (**ARIMA/SARIMA**) to multivariate models (**SARIMAX**) to leverage external features for higher accuracy.

-----

## 🛠️ Tech Stack

  * **Language:** Python
  * **Database:** SQLite
  * **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, `psycopg2` / `sqlalchemy`, `scikit-learn`, `python-dotenv`





-----

## 🚀 Project Workflow

The project pipeline consists of the following stages:

1.  **Synthetic Data Generation:** Created a custom dataset simulating sales environments with added relevant features (e.g., marketing spend, seasonality, holidays).
2.  **Database Integration:** Uploaded the generated .csv data into a local SQLite database.
3.  **EDA & Preprocessing:** Performed Exploratory Data Analysis to understand trends and seasonality.
4.  **Modeling (Phase 1):** Implemented ARIMA and SARIMA for univariate time series forecasting.
5.  **Modeling (Phase 2):** Implemented **SARIMAX** with hyperparameter tuning (using `auto_arima`) to incorporate exogenous variables like Price, CPI, and Holidays.
6.  **Deployment:** Built an interactive **Streamlit Dashboard** for real-time forecasting and scenario planning.
-----

## 📊 Data Methodology

### 1\. Data Generation

Since real-world sensitive sales data was unavailable, we engineered a synthetic dataset.

  * **Features Added:** Beyond the target variable (`Sales`), we generated additional features relevant to the domain to be used in multivariate analysis later.
  * **Storage:** The final dataset was exported as a .csv and loaded into SQLite for structured querying.

### 2\. Database Connection

  * **Connection:** Established a connection between the Python environment and the local SQLite database file.
  * **Querying:** Data is fetched directly from the database for preprocessing to simulate a production data pipeline.

### 3\. Preprocessing & Split

  * **Stationarity Check:** Before modeling, we validated the stationarity of the time series using the **Augmented Dickey-Fuller (ADF) Test**. We applied differencing (Integration `d` parameter) where necessary to stabilize the mean and variance.
  * **Train-Test Split:** The data was split into **80% Training** and **20% Testing** sets to evaluate model performance.
  * **Outlier Handling:**
      * *Note:* For the initial ARIMA/SARIMA models, outlier handling was deprioritized as these models relied solely on the univariate series history. Strict outlier removal is being revisited for the SARIMAX phase.

-----


## 🧠 Modeling & Strategy

### Phase 1: Univariate Forecasting (Completed)

We established a baseline using standard statistical models that rely only on past sales data.

  * **Models Used:**
      * **ARIMA:** (AutoRegressive Integrated Moving Average) for non-seasonal trends.
      * **SARIMA:** (Seasonal ARIMA) to capture repeating seasonal patterns in the synthetic data.
  * **Outcome:** Successfully trained on the 80% split and generated a forecast for the **next 3 months**.

### Phase 2: Multivariate Forecasting (Completed)

We upgraded the model to **SARIMAX** to capture the impact of external business drivers.

  * **Exogenous Variables:** Integrated features like `Price`, `CPI`, `Promotion_Flag`, and `Holiday_Flag`.
  * **Hyperparameter Tuning:** Utilized `pmdarima.auto_arima` to automatically identify the optimal `(p,d,q)` and seasonal `(P,D,Q)s` parameters, minimizing the AIC score.
  * **Outcome:** Achieved a more robust model that responds to price changes and marketing events, validated against the test set.
-----

## 📉 Results

### Performance Metrics

To quantitatively assess the model's accuracy on the 20% test set, we utilized the following metrics:

  * **RMSE (Root Mean Squared Error):** To measure the standard deviation of the prediction errors.

  * **MAPE (Mean Absolute Percentage Error):** To understand the accuracy in percentage terms.

  * **Forecast Horizon:** 3 Months.

  * **Visualization:** Plots comparing the `Test Set` actuals vs. `Predicted` values are generated to visually inspect the deviation.

<img width="994" height="528" alt="sari-hyper" src="https://github.com/user-attachments/assets/e7890719-f900-4f73-9925-412c3e409de3" />

<img src="https://github.com/user-attachments/assets/deafa52b-3d22-47cc-a87b-847bbdf398ca" width="480" />

<img src="https://github.com/user-attachments/assets/46152983-d41e-442e-8d73-17dff9b37858" width="480" />

<img src="https://github.com/user-attachments/assets/a44d3b87-1295-428e-9112-c3d2e4f56043" width="480" />

<img src="https://github.com/user-attachments/assets/5497188e-2167-4809-98c5-cfcd3deb20a9" width="480" />

<img src="https://github.com/user-attachments/assets/104f6f13-4dbf-4bd4-9eca-f1730d547c86" width="480" />

<img src="https://github.com/user-attachments/assets/bf265e5e-9016-4ed2-9865-8e6116552672" width="480" />

<img src="https://github.com/user-attachments/assets/0f793390-a735-4211-b287-04e3e576858d" width="480" />

-----

## 💻 Interactive Dashboard

We have deployed a local Streamlit application  to make the forecasting engine accessible to business users.

https://hcl-app-7zsrtkwyzp4csj6u2xb2bj.streamlit.app/

**Key Features:**
* **Model Selection:** Choose between pre-trained models (ARIMA, SARIMA, SARIMAX).
* **Dynamic Forecasting:** Adjust the forecast horizon (e.g., 7, 30, 90 days) using a slider.
* **Scenario Planning (SARIMAX):** Simulate business scenarios by adjusting future parameters:
    * *What if we increase the price by 10%?*
    * *What if we run a promotion next week?*
* **Visualizations:** Interactive plots showing historical data, future forecasts, and confidence intervals.

## 🔮 Future Scope
  * **Deep Learning:** Experimenting with LSTM (Long Short-Term Memory) networks for comparison.
  

-----




