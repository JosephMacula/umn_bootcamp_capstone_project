# Pollution and Economic Indicators – Data Science Report

## Project Scope  
This analysis suite comprises multiple Python notebooks investigating the interplay between **air pollution** and **economic indicators** across Chinese cities from **2014 through 2025**, with forecasts extending to **2030**. The objective is to provide evidence-based insights for **economic activity**.

---

## Key Findings  

### 1. **Pollution Trend Analysis Across Cities**  
- Cities analyzed include: **Beijing**, **Shuozhou**, **Baotou**, **Tangshan**, **Shanghai**, and others.  
- Data cleaning and transformation pipelines were established to harmonize datasets.  
- Seasonal and yearly pollution cycles are evident, with **winter spikes** (e.g., due to heating) and long-term **downward trends** in SO₂ and PM2.5 levels in industrial cities.  

### 2. **Pollution–Economy Interactions**  
- Coal prices and industrial indices (e.g., **CPI**, **PMI**) were aligned with pollution time series.  
- **Visual and statistical correlations** show pollution trends often **lead economic indicators**, supporting their use as early warning signals.  
- Seasonal adjustments and trend decomposition reveal **hidden long-term changes** that are not visible in raw data.  

### 3. **Time Series Modeling and Forecasting**  
- Statistical and machine learning models were applied:  
  - **Unobserved Components Models (UCMs)** separated signal from noise in pollution data.  
  - **VAR and Granger causality tests** confirmed predictive power of pollutants on CPI and PMI.  
  - **Dynamic Linear Trend (DLT)** models and **LSTMs** forecast pollutant levels in Shanghai and Baotou through 2030.  
- Decay trends were introduced to simulate **policy interventions**, revealing projected reductions under current regulatory trajectories.  

### 4. **Predicting Coal Market Movements**  
- Pollution lag features (1–6 months) were used to predict the **Chinese Coal Index**.  
- Both **SARIMAX** and **LSTM** models showed strong performance.  
- **Granger causality tests** validated multiple pollutants (PM10, O₃, NO₂, CO, PM2.5) as statistically significant predictors.  

---

## Strategic Implications  
- **Air pollution metrics can serve as leading indicators** for economic stress and industrial output shifts.  
- Forecast models offer tangible timelines for **air quality improvements under various policy regimes**.  
- Integration of pollution data into macroeconomic dashboards is feasible and valuable for real-time monitoring.  
- Targeted regulation in cities like **Shuozhou (coal hub)** and **Tangshan (steel industry)** could yield outsized national benefits.  

---

## Recommendations  
- Expand scope to include **weather**, **transport**, and **energy consumption** as additional regressors.  
- Use these insights to refine **environmental compliance strategies** and **resource planning**.  

---  
*Prepared by Chi Nguyen | Virginia Tech | July 2025*  

---

# `data_wrangling.ipynb`  

# Air Pollution and Economic Indicators Analysis (2014–2025)  

## Overview  
This notebook performs a comprehensive exploratory analysis of air pollution data across various Chinese cities, covering the period from 2014 to mid-2025. It includes data cleaning, visualization of trends, comparison across cities, and analysis of relationships with economic indicators such as coal prices.  

**Author**: Chi Nguyen  

---  

## Data Loading and Preprocessing  

### `read_and_clean(filepath)`  
- Reads air pollution data from a CSV file.  
- Converts the `date` column to datetime.  
- Sorts the data in descending order by date.  
- Renames columns and converts pollutant data to numeric format.  
- Returns a cleaned DataFrame.  

### Datasets Loaded:  
- **Beijing (Capital)**  
- **Panzhihua (Steel Industry)**  
- **Shuozhou (Coal Hub)**  
- **Taiyuan (Shanxi’s Capital)**  
- **Baotou (REE Mining)**  
- **Ganzhou**  
- **Tangshan**  
- **Qinhuangdao**  
- **Shanghai**  

### Economic Data:  
- Coal price time series data for comparison with pollution indicators.  

---  

## Daily Pollution Visualization  

### `plot_df(df, pollutant, title)`  
- Plots daily pollutant concentrations over time.  
- Example: `SO2` in Shuozhou (2014 to mid-2025).  

---  

## Pollution vs. Economic Indicator  

### `econ_Pollution(df, pollutant, economic_indicator, title)`  
- Overlays pollutant concentration with coal prices on dual Y-axes.  
- Enables visual correlation between industrial/economic activity and pollution trends.  

---  

## Monthly Trends  

### `monthlyAverage(df, city_name, pollutant)`  
- Aggregates pollutant levels into monthly averages.  
- Useful for observing smoothed long-term patterns.  
- Example: Monthly average `SO2` in Beijing.  

### `compareMonthlyAverages(df1, city1, df2, city2, pollutant)`  
- Compares monthly pollution trends between two cities.  
- Example: `NO2` levels in Baotou vs. Ganzhou.  

### `compareMonthlyAveragesEcon(df, city, pollutant, econ_indicator, econ_indicator_Name)`  
- Compares monthly pollution averages with an economic variable such as coal prices.  

---  

## Seasonality Analysis  

### `seasonalityPlot(df, city_name, pollutant)`  
- Plots pollutant concentration per month for each year.  
- Highlights seasonal fluctuations (e.g., winter heating effects).  

---  

## Yearly and Monthly Boxplots  

### `boxPlot(df, pollutant)`  
- Year-wise and month-wise boxplots to detect:  
  - Trend (via annual dispersion)  
  - Seasonality (via monthly patterns)  

---  

## Comparative Seasonal Trends  

### `comparativePlots(df1, city1, df2, city2, pollutant)`  
- Compares seasonal behavior of a pollutant across two cities.  
- Highlights differing industrial cycles or environmental policies.  

---  

## Trend Analysis  

### `plot_detrended_pollutant(df, pollutant)`  
- Fits a least-squares trend line to the time series.  
- Detrends the data to isolate long-term trend from seasonal/cyclical components.  

---  

## Deseasonalization  

### `plot_deseasonalized_pollutant(df, pollutant, city_name, period=365)`  
- Applies multiplicative seasonal decomposition.  
- Removes seasonality to uncover more subtle trends in pollutant concentration.  

---  

## Deseasonalized Trend Fitting  

### `plot_deseasonalized_trend(df, pollutant, city_name="", period=365)`  
- Combines deseasonalization and linear regression.  
- Plots the clean trend after eliminating both noise and seasonality.  

---  

## Summary  
This notebook:  
- Provides a thorough preprocessing pipeline for environmental time series data.  
- Implements multiple visualization strategies to reveal temporal patterns, city-wise comparisons, and potential economic linkages.  
- Utilizes statistical techniques (decomposition and regression) for extracting meaningful long-term signals.  

This analysis is valuable for policymakers, environmental scientists, and economists seeking to understand pollution behavior in relation to industrial and economic trends.  

---  

# `ccf.ipynb`  

# Pollution and CPI Time Series Analysis (Shanghai)  

This notebook investigates the relationship between **pollution levels** and the **Consumer Price Index (CPI)** in Shanghai using various time series analysis techniques. The workflow involves cleaning and transforming data, visualizing trends, assessing correlations, and performing causal inference tests.  

---  

## Data Sources  

1. **Pollution Data** (`shanghai.csv`):  
   Contains daily concentrations of:  
   - PM2.5  
   - PM10  
   - O₃ (Ozone)  
   - NO₂ (Nitrogen Dioxide)  
   - SO₂ (Sulfur Dioxide)  
   - CO (Carbon Monoxide)  

2. **CPI Data** (`shanghai-consumer-price-index.csv`):  
   Contains monthly CPI readings in the format `Mon-YY` (e.g., `Jun-25` for June 2025).  

---  

## Data Preprocessing  

- **Date Parsing**: Both CPI and pollution datasets require custom date parsing due to inconsistent formats. For the CPI, string parsing (`%b-%y`) is applied to convert to `datetime`.  
- **Monthly Aggregation**: Daily pollution data is aggregated into monthly averages to match the CPI frequency.  
- **Cleaning**: All non-numeric entries and invalid dates are removed or coerced.  

---  

## Visual Analysis  

### `plotPollutantVsCPI()`  
- A dual-axis line plot that compares the monthly average of a selected pollutant (e.g., NO₂) against CPI.  
- Useful for visual correlation and pattern inspection over time.  

---  

## Cross-Correlation Analysis (CCF)  

### `ccf(pollutant)`  
- Ensures stationarity (via the Augmented Dickey-Fuller test) and applies differencing if needed.  
- Computes the cross-correlation function (CCF) to measure lead-lag relationships between pollution and CPI.  
- Helps identify whether pollution levels lead or lag CPI changes.  

---  

## Prewhitening  

### `prewhitening(pollutant)`  
- Fits an AR(1) model to the pollutant series to filter out autocorrelation.  
- Applies the same transformation to the CPI series.  
- Performs a CCF on the residuals to isolate the genuine influence between the two series, minimizing spurious correlations.  

---  

## Granger Causality  

### `granger_test(pollutant)`  
- Performs Granger causality tests to determine if pollution predicts future values of CPI.  
- Both series are made stationary before testing.  
- Lag orders up to 12 months are considered.  

---  

## VAR Modeling  
- A Vector AutoRegression (VAR) model is fit using the stationary pollutant and CPI series.  
- Lag order selection is performed using AIC/BIC.  
- Once fitted, the model is used to:  
  - Plot Impulse Response Functions (IRFs) to analyze the dynamic impact of a shock in pollution on CPI.  
  - Compute Forecast Error Variance Decomposition (FEVD) to quantify the contribution of each variable to CPI forecast variance.  

---  

## Key Objectives  
- Assess whether pollution levels are leading indicators of inflationary pressures (via CPI).  
- Examine the strength and timing of relationships using time-lagged analysis.  
- Use econometric modeling (Granger, VAR) to provide statistical evidence for policy or economic insight.  

---  

## Next Steps / Suggestions  
- Expand pollutant list for CCF/Granger tests.  
- Incorporate seasonality adjustments.  
- Explore external factors like weather, industry activity, or fuel prices for multivariate modeling.  

---  

## Dependencies  
- pandas  
- numpy  
- matplotlib  
- statsmodels  

---  
# `Structural Time Series.ipynb`

# `Unobserved Components Modeling of PM2.5 and Its Relationship with PMI`  

This notebook explores air pollution trends—specifically PM2.5 concentrations in Beijing—using **Unobserved Components Models (UCM)**. It extends the analysis by examining the possible relationship between air quality and China's **Purchasing Managers’ Index (PMI)**.  

---  

## Objective  
- Extract the underlying **true pollution signal** from noisy daily PM2.5 measurements.  
- Quantify the uncertainty of these estimates.  
- Use advanced time series models (local level and local linear trend) to track both the level and slope of pollution trends.  
- Evaluate how past air pollution may influence **economic indicators** such as PMI.  

---  

## Workflow Overview  

### 1. **Data Loading & Cleaning**  
- Loads pollution data from `'beijing, west park.csv'`.  
- Cleans missing values and converts relevant columns to numeric types.  
- Sorts the dataset chronologically.  
- Selects a target pollutant (`PM2.5`) for modeling.  

### 2. **Model 1: Local Level Model**  
- Fits a **local level model** to extract a smoothed estimate of the true pollution level.  
- Separates:  
  - **Signal**: underlying pollution trend.  
  - **Noise**: short-term fluctuations.  

**Outputs:**  
- Summary statistics.  
- Plots comparing observed vs. estimated levels.  
- Confidence intervals for model estimates.  
- RMSE and MAE between observed and estimated values.  
- Variance of the latent state over time to assess model confidence.  

### 3. **Model 2: Local Linear Trend Model**  
- A more flexible model allowing for both **level** and **trend** (slope) components.  
- Handles missing data via linear interpolation.  
- Produces:  
  - Estimated level and trend over time.  
  - Confidence bands around estimates.  
  - Variance decomposition (level, trend, and observation noise).  

**Insights:**  
- Whether pollution is increasing, decreasing, or stabilizing.  
- Confidence in those patterns over time.  

---  

## Signal-to-Noise Ratio (SNR)  
- Computed as: `level_variance / noise_variance`.  
- Higher SNR indicates greater model confidence in the extracted trend.  
- Overestimated variances suggest the model believes pollution is highly volatile and noisy.  

---  

## One-Step-Ahead Forecast  
- Uses the model to predict PM2.5 for the next day.  
- Provides forecast intervals.  
- Wide intervals with negative lower bounds imply high model uncertainty.  

---  

## Model Diagnostics  
- **State Variance Plot**: Displays model confidence over time.  
  - Sharp drop in early steps reflects learning from initial data.  
  - Flat variance indicates stability and high certainty.  

---  

## Dynamic Regression: PM2.5 and PMI  

### Goal:  
Determine if **lagged PM2.5 levels** can help explain or predict China’s **Purchasing Managers' Index (PMI)**.  

### Steps:  
1. Aggregate PM2.5 to monthly means.  
2. Generate lagged pollutant features (e.g., previous month’s PM2.5).  
3. Merge with monthly PMI data.  
4. Fit a **UCM with exogenous regressors** (PM2.5 lag) to PMI.  

### Model:  
- **Endogenous**: PMI  
- **Exogenous**: Lagged PM2.5  
- **Trend**: Local linear trend  

**Outputs:**  
- Model summary and decomposition plots.  
- Signal-to-noise ratio for economic trend.  
- Model parameters showing how past pollution may impact PMI.  

---  

## Key Insights  
- **UCMs effectively separate trend from noise** in pollution data.  
- **State variance plots** indicate where the model is confident vs uncertain.  
- **Local linear models** better capture directional change over time.  
- **PM2.5 may be a leading indicator for economic trends** such as PMI when included as an exogenous regressor.  

---  

## Dependencies  
- `pandas`  
- `numpy`  
- `matplotlib`  
- `seaborn`  
- `statsmodels`  
- `scikit-learn`  

---  

## Suggested Extensions  
- Add additional pollutants (NO₂, O₃) as regressors.  
- Include seasonal or holiday dummy variables.  
- Evaluate structural breaks due to policy changes or events.  
- Compare with ARIMA or machine learning models for forecasting.  

---  

# `BSTS.ipynb`  

# Forecasting Air Pollution in Shanghai Using DLT  

This notebook demonstrates a time series forecasting workflow to model and predict the concentration of air pollutants in Shanghai, with a focus on sulfur dioxide (SO₂). The process leverages the **Dynamic Linear Trend (DLT)** model from the `orbit` library, along with engineered regressors and decay trends to simulate policy impacts.  

## Objectives  
- Clean and preprocess air pollution data.  
- Visualize daily and monthly pollutant trends.  
- Build predictive models using DLT.  
- Incorporate seasonal and policy-related regressors.  
- Forecast future pollution levels through 2030.  

## Key Steps  

### 1. Data Preparation  
- Three datasets are loaded: full, training, and testing subsets.  
- Dates are parsed, columns are cleaned, and missing values are handled.  
- Pollutant data is coerced to numeric for robustness.  

### 2. Visualization  
- **Time Series Plots**: Daily concentrations of SO₂ are plotted across full, training, and testing periods.  
- **Monthly Averages**: Aggregated monthly averages provide a smoothed view of trends over time.  

### 3. Seasonality Detection  
A heuristic is applied to detect natural seasonality based on median date differences:  
- Daily: 365  
- Weekly: 52  
- Monthly: 12  

### 4. Initial Forecast Using DLT  
- A DLT model is trained on the training set and evaluated on the test set.  
- Predictions are visualized alongside actual values, and **Mean Absolute Error (MAE)** is computed.  

### 5. Monthly Seasonality as Regressor  
- Monthly average pollutant values are computed and added as a regressor.  
- The model is retrained on the full dataset and used to forecast until the end of 2025.  
- Future dates are synthesized and predictions visualized.  

### 6. Long-Term Forecast to 2030  
- The forecast horizon is extended to 2030.  
- A **decay trend** is introduced, simulating policy-induced reductions in pollutant levels.  
- Two types of decay are used:  
  - **Exponential Decay**  
  - **Linear Decay Trend**  

These regressors are added to both historical and future datasets and included in model training.  

### 7. Feature Engineering & Advanced DLT  
Advanced regressors are added:  
- Standardized monthly average (`monthly_avg_std`)  
- Logarithmic decay (`decay_log`)  
- 7-day moving average of monthly averages (`monthly_avg_ma7`)  

The final DLT model uses the **MCMC estimator** for full Bayesian inference and outputs 90% prediction intervals.  

### 8. Final Forecast Plot  
The forecast is plotted with:  
- Historical values  
- Predicted means  
- Confidence intervals (5th and 95th percentiles)  
- Forecast horizon marked  

### 9. Saving Results  
The combined dataset (historical + forecast) is saved to CSV for downstream use or deployment.  

---  

This notebook provides a scalable blueprint for modeling pollution dynamics, factoring in temporal patterns and plausible external interventions such as environmental policy.  

---  

# `Recurrent Neural Network.ipynb`  

# PM2.5 Forecasting in Baotou Using LSTM  

This notebook builds and evaluates a deep learning model to forecast daily PM2.5 concentrations in Baotou using historical air quality data and a Long Short-Term Memory (LSTM) recurrent neural network. The model is trained on sliding time windows of past observations and makes both short-term and long-term predictions.  

## Workflow Overview  

### 1. Data Loading and Cleaning  
- Air quality data is loaded from CSV files containing daily readings of various pollutants.  
- The dataset includes: `PM2.5`, `PM10`, `O3`, `NO2`, `SO2`, and `CO`.  
- Date columns are parsed to datetime format.  
- Non-numeric and missing values are handled.  
- Only the `PM2.5` column is used for modeling.  
- The dataset is sorted chronologically and missing rows are dropped.  

### 2. Data Preprocessing  
- `MinMaxScaler` is applied to normalize the PM2.5 data into the range [0, 1].  
- A rolling window of 700 days is used to prepare the input sequences (`x`) and corresponding targets (`y`).  

### 3. Model Architecture  
An LSTM model is constructed with the following architecture:  
- Four LSTM layers with 64 units each.  
- Dropout regularization (0.2) after each LSTM layer.  
- A Dense output layer with a single unit.  
- Compiled using the Adam optimizer and Mean Absolute Error (MAE) loss.  

### 4. Training Strategy  
- The dataset is split into training and validation sets (90%/10%).  
- An early stopping callback monitors validation loss and restores the best model.  
- The model is trained for up to 45 epochs with a batch size of 32.  

### 5. Short-Term Testing and Evaluation  
- The test dataset is preprocessed and transformed to match the input format expected by the model.  
- Predictions are generated for the test period.  
- The output is inverse-scaled to the original PM2.5 range for evaluation.  
- Visualizations compare actual vs. predicted values to assess model performance.  

### 6. Long-Term Forecasting  
- A recursive prediction strategy is used to forecast PM2.5 levels 365 days into the future.  
- The model generates one step ahead at each iteration using the previous predictions as input.  
- The full historical PM2.5 time series is plotted along with the 1-year forecast.  

## Conclusion  
The notebook demonstrates a full pipeline for air pollution forecasting using LSTM models. It effectively:  
- Cleans and prepares real-world environmental data.  
- Builds and trains a deep learning model for time series forecasting.  
- Produces short-term and long-term predictions.  
- Visualizes results for model validation and interpretability.  

This methodology can be extended or adapted for other pollutants, locations, or time resolutions.  

---  

# `economic data.ipynb`  

# Forecasting the Chinese Coal Index Using Air Pollution Indicators  

This notebook explores the relationship between air pollution levels and the Chinese coal index, aiming to build predictive models based on historical pollutant data. Two modeling approaches are used: **SARIMAX** and **LSTM**. The workflow includes data preprocessing, exploratory analysis, feature engineering using lag variables, correlation and causality testing, and time series forecasting.  

---  

## 1. Data Loading and Preprocessing  

### Pollution Data (Shanghai)  
- Daily air quality data is loaded, including PM2.5, PM10, NO₂, O₃, SO₂, and CO.  
- The `date` column is parsed and set as the index.  
- Columns are renamed to lowercase for consistency.  
- All variables are converted to numeric values.  
- Daily pollution values are resampled to **monthly averages** to match the coal index frequency.  

### Coal Index Data  
- Monthly coal index data is loaded and indexed by date.  
- Dates are assumed to be in standard ISO format.  
- The coal index column is renamed to `coalindx`.  

---  

## 2. Feature Engineering  

### Lag Variables  
- For each pollution variable, **1 to 6-month lags** are generated to capture temporal dependencies and delayed effects on the coal index.  
- All rows with missing values resulting from lagging are dropped.  

---  

## 3. Exploratory Data Analysis  

### Correlation Analysis  
- A correlation heatmap reveals which pollution variables (and their lags) are most strongly associated with the coal index.  
- **PM10**, **PM2.5**, **NO₂**, **O₃**, and **CO** show notable correlations with the target variable.  

### Seasonal Decomposition  
- Seasonal decomposition plots are generated for each pollutant to understand their trend and seasonal behavior across time.  

---  

## 4. Granger Causality Testing  
- The Granger causality test is used to identify whether past values of pollutant variables can statistically predict the coal index.  
- Tests are performed for lags 1 to 12.  
- Variables that pass the significance threshold (p < 0.05) at any lag are selected as **predictive features**:  
  - **PM10**  
  - **O₃**  
  - **NO₂**  
  - **CO**  
  - **PM2.5**  

- A heatmap of p-values from the Granger causality test is plotted for visualization.  

---  

## 5. SARIMAX Forecasting Model  

### Data Preparation  
- The filtered lagged pollution variables are used as exogenous features.  
- The dataset is split into training (80%) and testing (20%) sets, preserving chronological order.  

### Model Configuration  
- A **SARIMAX(1,1,1)(1,1,1,12)** model is fitted on the training data.  
- Seasonal order accounts for annual cycles in the monthly data.  

### Evaluation  
- The model is used to forecast the coal index over the test set.  
- RMSE is calculated to assess accuracy.  
- Forecast vs. actual values are plotted to evaluate performance.  

---  

## 6. LSTM Neural Network Model  

### Scaling and Sequence Preparation  
- All features are scaled using **MinMaxScaler**.  
- The dataset is split into training (before 2023) and testing (2023 onward).  
- Time series sequences of length 3 are created for LSTM input.  

### Model Architecture  
- A simple LSTM with 64 units and a dense output layer is trained for 50 epochs using MSE loss.  
- Predictions are made on the test set and inverse-transformed for comparison.  

### Visualization  
- Forecasts are plotted against actual coal index values.  
- For each pollutant, its normalized trend is overlaid on the forecast to show alignment and potential influence.  

---  

## Conclusion  
This notebook demonstrates a hybrid approach for modeling economic indicators using environmental data:  
- **SARIMAX** provides an interpretable statistical baseline with lagged pollutant variables.  
- **LSTM** offers a flexible nonlinear alternative capable of learning complex temporal patterns.  

The analysis also reveals statistically significant relationships between pollutants and the coal index, offering potential insights into how environmental trends may foreshadow economic indicators in energy markets.  