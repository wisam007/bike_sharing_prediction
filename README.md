# Bike Sharing Demand Prediction

An end-to-end machine learning regression project that predicts the daily number of bike rentals using weather and calendar-related information. The project follows a modular Python architecture, performs exploratory data analysis (EDA), compares multiple regression algorithms, exports the best trained model, and provides predictions through a Streamlit web application.

---

## Problem Statement

Bike-sharing systems require accurate demand forecasting to ensure bicycles are available when and where customers need them. Reliable predictions help operators optimize fleet distribution, improve customer satisfaction, and reduce operational costs.

This project builds a complete machine learning pipeline that:

1. Loads and validates the raw bike-sharing dataset.
2. Cleans and preprocesses the data.
3. Performs exploratory data analysis and generates visualizations.
4. Trains and compares multiple regression models.
5. Selects and exports the best-performing model.
6. Deploys the trained model through a Streamlit application for interactive predictions.

**Target Variable:** `cnt` (Total Daily Bike Rentals)

---

## Dataset

The project uses the **Bike Sharing Dataset (Daily)** from the UCI Machine Learning Repository.

| Attribute    | Description                  |
| ------------ | ---------------------------- |
| `season`     | Season of the year           |
| `yr`         | Year (0 = 2011, 1 = 2012)    |
| `mnth`       | Month                        |
| `holiday`    | Holiday indicator            |
| `weekday`    | Day of the week              |
| `workingday` | Working day indicator        |
| `weathersit` | Weather condition            |
| `temp`       | Normalized temperature       |
| `atemp`      | Feeling temperature          |
| `hum`        | Humidity                     |
| `windspeed`  | Wind speed                   |
| `casual`     | Casual users                 |
| `registered` | Registered users             |
| `cnt`        | Total daily rentals (Target) |

### Dataset Summary

* **Records:** 731 daily observations
* **Target:** Daily bike rental count (`cnt`)
* **Missing Values:** None
* **Duplicate Records:** None

### Data Cleaning

The preprocessing pipeline performs the following tasks:

* Validates data quality
* Fixes zero humidity values using monthly median humidity
* Detects target leakage
* Removes redundant columns:

  * `instant`
  * `dteday`
  * `casual`
  * `registered`
  * `atemp`
* Maps encoded categorical values into readable labels

---

## Installation

### Prerequisites

* Python 3.12+
* pip

### Setup

```bash
git clone https://github.com/wisam007/bike_sharing_prediction.git
cd bike_sharing_prediction

python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## Usage

### 1. Train Models

Run the complete machine learning pipeline:

```bash
python main.py
```

This will:

* Load the dataset
* Perform preprocessing
* Generate EDA figures
* Train multiple regression models
* Evaluate all models
* Save evaluation reports
* Export the best model (`best_model.pkl`)

---

### 2. Make Predictions (CLI)

```bash
python predict.py
```

The prediction script loads the exported model and predicts the expected number of daily bike rentals for new observations.

---

### 3. Launch Streamlit Application

```bash
streamlit run app/app.py
```

The web application allows users to:

* Explore the dataset
* View EDA visualizations
* Compare trained models
* Predict daily bike rentals interactively

---

## Project Structure

```text
bike_sharing_prediction/
├── app/
│   ├── app.py
│   └── app_pages/
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── best_model.pkl
├── reports/
│   ├── figures/
│   ├── json/
│   └── tables/
├── src/
│   ├── loader.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── modeling.py
│   ├── evaluation.py
│   ├── visualization.py
│   ├── reporting.py
│   ├── persistence.py
│   ├── inference.py
│   └── eda.py
├── config.py
├── main.py
├── predict.py
├── requirements.txt
└── README.md
```

---

## Machine Learning Models

The following regression algorithms were trained and evaluated:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* Support Vector Regressor (SVR)
* Extra Trees Regressor
* AdaBoost Regressor

Each model was evaluated using:

* R² Score
* RMSE
* MAE
* MSE
* MAPE
* Training Time

The best-performing model is automatically selected and saved as:

```text
models/best_model.pkl
```

---

## Results

Model evaluation results are automatically exported to:

* `reports/json/evaluation_score.json`
* `reports/json/best_model.json`

Performance comparison includes:

* Test R²
* RMSE
* MAE
* Training Time

The project also generates comparison visualizations to help identify the best-performing model.

---

## Generated Reports

Running the training pipeline produces:

### Reports

* Dataset Summary
* Data Quality Report
* Model Evaluation Report
* Best Model Information

### Figures

* Rental Count Distribution
* Numerical Feature Distributions
* Categorical Feature Distributions
* Outlier Boxplots
* Correlation Heatmap
* Feature Relationship Scatterplots
* Model Comparison Chart
* Actual vs. Predicted Scatterplots

### Saved Artifacts

* Processed Dataset (CSV)
* Best Trained Model (`.pkl`)
* JSON Reports
* CSV Tables

---

## Streamlit Application

The Streamlit dashboard provides:

* Dataset overview
* Data quality summary
* Exploratory Data Analysis (EDA)
* Model comparison
* Prediction interface
* Best model information

The prediction page loads the exported `best_model.pkl`, applies the preprocessing pipeline automatically, and predicts the expected number of daily bike rentals.

---

## Tech Stack

* Python 3.12
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

---

## Future Improvements

Potential enhancements include:

* Hyperparameter optimization using GridSearchCV or RandomizedSearchCV
* Cross-validation analysis
* Feature importance and SHAP explanations
* Cloud deployment (Streamlit Community Cloud or Render)
* Continuous model monitoring and retraining

---

## License

This project is intended for educational and academic purposes.
