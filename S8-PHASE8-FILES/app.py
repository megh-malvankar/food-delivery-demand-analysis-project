# ===============================================================
# OBJECTIVE 5
# Machine Learning & Statistical Analysis
# ===============================================================

# ---------------------------------------------------------------
# Task 1 – Data Preparation
# ---------------------------------------------------------------

# Interpretation:
# Loaded the merged food delivery dataset and verified its quality before analysis.
# Checked the dataset structure, missing values, and duplicate records to ensure data readiness.

# Libraries
import pandas as pd
import numpy as np

# Load Dataset
merged_df = pd.read_excel("Merged_FoodDelivery_Dataset.xlsx")

# Data Checks
print(merged_df.info())

print(merged_df.isnull().sum())

print(merged_df.duplicated().sum())


# ---------------------------------------------------------------
# Task 2 – Statistical Analysis
# ---------------------------------------------------------------

# Interpretation:
# Performed statistical analysis to understand data distribution and relationships among variables.
# Compared customer spending behaviour and delivery performance to identify useful business patterns.

from scipy import stats


# 1. Descriptive Statistics

print("\n----- Descriptive Statistics -----")

print(merged_df.describe())


# 2. Correlation Matrix

print("\n----- Correlation Matrix -----")

numeric = merged_df.select_dtypes(include=np.number)

correlation = numeric.corr()

print(correlation)


# 3. Revenue by Customer Type

print("\n----- Revenue by Customer Type -----")

print(
    merged_df.groupby("Customer_Type")["Final_Amount"].mean()
)


# 4. Delivery Time by Region

print("\n----- Delivery Time by Region -----")

print(
    merged_df.groupby("Region")["Delivery_Time_Minutes"].mean()
)


# 5. Statistical Test (Independent T-Test)

print("\n----- Independent T-Test -----")

loyal = merged_df[
    merged_df["Customer_Type"]=="Loyal"
]["Final_Amount"]

new = merged_df[
    merged_df["Customer_Type"]=="New"
]["Final_Amount"]

t, p = stats.ttest_ind(
    loyal,
    new
)

print("T Statistic :", t)
print("P Value :", p)


# ---------------------------------------------------------------
# Task 3 – Feature Engineering
# ---------------------------------------------------------------

# Interpretation:
# Selected the important features required for prediction and converted categorical variables into numerical format.
# Prepared the dataset by separating input features and target values before model training.

print("\n----- Feature Engineering -----")

features = merged_df[
[
    "Delivery_Time_Minutes",
    "Avg_Rating",
    "Delivery_Efficiency_Score",
    "Vehicle_Type",
    "Customer_Type",
    "Region",
    "Festival_Flag"
]
]

features = pd.get_dummies(
    features,
    columns=[
        "Vehicle_Type",
        "Customer_Type",
        "Region"
    ],
    drop_first=True
)

target = merged_df["Order_Rating"]

features = pd.get_dummies(
    features,
    drop_first=True
)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

print("Training Dataset :", X_train.shape)

print("Testing Dataset :", X_test.shape)


# ---------------------------------------------------------------
# Task 4 – Machine Learning Model
# ---------------------------------------------------------------

# Interpretation:
# Developed two regression models to predict customer order ratings.
# Compared Linear Regression and Random Forest to identify the better-performing algorithm.

print("\n----- Machine Learning Models -----")


# Model 1 - Linear Regression

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(
    X_train,
    y_train
)

prediction_lr = lr.predict(X_test)


# Model 2 - Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    random_state=42
)

rf.fit(
    X_train,
    y_train
)

prediction_rf = rf.predict(X_test)


# ---------------------------------------------------------------
# Task 5 – Model Evaluation & Business Insights
# ---------------------------------------------------------------

# Interpretation:
# Evaluated both machine learning models using MAE and R² metrics.
# Compared model performance and identified the algorithm that produced better prediction accuracy.

print("\n----- Model Evaluation -----")

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# Linear Regression

print("\nLinear Regression")

print(
    mean_absolute_error(
        y_test,
        prediction_lr
    )
)

print(
    r2_score(
        y_test,
        prediction_lr
    )
)


# Random Forest

print("\nRandom Forest")

print(
    mean_absolute_error(
        y_test,
        prediction_rf
    )
)

print(
    r2_score(
        y_test,
        prediction_rf
    )
)


# Compare Models

print("\n----- Model Comparison -----")

print(f"Linear Regression MAE : {mean_absolute_error(y_test, prediction_lr):.4f}")

print(f"Linear Regression R²  : {r2_score(y_test, prediction_lr):.4f}")

print(f"Random Forest MAE     : {mean_absolute_error(y_test, prediction_rf):.4f}")

print(f"Random Forest R²      : {r2_score(y_test, prediction_rf):.4f}")


if r2_score(y_test, prediction_rf) > r2_score(y_test, prediction_lr):

    print("\nBest Model : Random Forest Regressor")

else:

    print("\nBest Model : Linear Regression")


# ---------------------------------------------------------------
# Final Business Interpretation
# ---------------------------------------------------------------

print("\n----- Final Business Interpretation -----")

print(
    "The machine learning models were successfully developed and evaluated using the merged food delivery dataset."
)

print(
    "Statistical analysis showed that the selected features had only weak relationships with customer order ratings, resulting in comparatively low predictive performance for both models."
)

print(
    "This indicates that additional business variables or richer customer behaviour data would improve prediction accuracy."
)

print(
    "Despite the limited predictive performance, the complete workflow from data preparation and statistical analysis to feature engineering, model development, and evaluation was successfully implemented."
)

print(
    "The project successfully demonstrates the practical application of statistical analysis and machine learning techniques for business decision support in the food delivery domain."
)