# 🍽️ Food Delivery Demand Analysis

An end-to-end **Data Analytics Capstone Project** focused on understanding food delivery demand, customer behaviour, regional performance, restaurant activity, delivery operations, and business opportunities using **Excel, MySQL, Python, Power BI, Statistics, and Machine Learning**.

## 📌 Project Overview

The project analyzes a merged Food Delivery dataset containing **94,550 order records and 34 columns**.

**Workflow:** Data Preparation → Excel Analysis → SQL Analysis → Python EDA → Power BI Dashboard → Statistical Analysis → Machine Learning → Business Insights & Recommendations

The project supports decisions related to regional expansion, customer behaviour, revenue and order growth, restaurant performance, delivery efficiency, payment preferences, operational improvement, and predictive analytics.

## 🎯 Project Objectives

| Objective | Area | Main Focus | Tools |
|---|---|---|---|
| **Objective 1** | Regional Demand & Business Performance Analysis | Regional demand, revenue, customers, cuisine preference, ratings and delivery efficiency | Microsoft Excel |
| **Objective 2** | Business Data Management & Query Analysis | Database creation, table organization, relationships and business reports | MySQL |
| **Objective 3** | Customer, Restaurant & Delivery Performance Analysis | Data preparation, validation, merging, EDA and visualizations | Python, Pandas, NumPy, Matplotlib |
| **Objective 4** | Business Intelligence & Interactive Dashboard | KPI reporting, interactive visuals and business storytelling | Power BI, Power Query, DAX |
| **Objective 5** | Statistical & Machine Learning Analysis | Statistical validation and predictive model evaluation | Python, SciPy, Scikit-learn |

## 📊 Dataset

The project uses four major datasets:

- **Customers**
- **Orders**
- **Restaurants**
- **Delivery Partners**

The final merged dataset contains:

- **94,550 records**
- **34 columns**
- **Date range:** 2023–2025
- **Missing values:** 0
- **Duplicate records:** 0

## 📗 Objective 1 — Excel Analysis

### Regional Demand & Business Performance Analysis

Excel was used for Pivot Tables, KPI cards, Pivot Charts, slicers and an interactive business dashboard.

### Key Findings

- **94,550 orders** were analyzed.
- **Urban** recorded the highest order volume.
- **Urban** generated the highest total revenue.
- **Chinese cuisine** was the most preferred cuisine.
- **Urban** achieved the highest average customer rating.
- **Urban** recorded the highest delivery efficiency.

## 🗄️ Objective 2 — MySQL Analysis

### Business Data Management & Query Analysis

MySQL was used to organize the business data into related tables and generate analytical reports.

```text
FoodDeliveryDB

├── customers
├── orders
├── restaurants
└── delivery_partners
```

### Main SQL Work

- Database and table creation
- Data organization and validation
- Relationships between business records
- Aggregation and grouping
- Filtering
- JOIN-based analysis
- Customer spending analysis
- Delivery partner performance
- Revenue and order analysis

### Main Reports

- Orders by Region
- Customer Type Distribution
- Restaurants by Region
- Vehicle Type Distribution
- Preferred Cuisine
- Payment Mode Analysis
- Delivery Partner Performance
- Customer Spending Analysis
- Complete 4-table JOIN report

## 🐍 Objective 3 — Python Exploratory Data Analysis

Python was used to prepare, validate, combine and explore the merged dataset.

### Libraries

- Pandas
- NumPy
- Matplotlib

### EDA Performed

- Total Orders
- Revenue Analysis
- Revenue by Region
- Customer Type Analysis
- Preferred Cuisine
- Restaurant Ratings
- Delivery Time
- Payment Mode Distribution
- Festival vs Non-Festival Orders
- Top Restaurants
- Delivery Efficiency

### Visualizations

- Orders by Region
- Revenue by Region
- Customer Type Distribution
- Preferred Cuisine
- Payment Mode Distribution
- Restaurant Ratings
- Delivery Time
- Vehicle Type Distribution
- Delivery Efficiency
- Festival vs Non-Festival Orders

## 📈 Objective 4 — Power BI Dashboard

Power BI was used to transform the analysis into an interactive business dashboard.

### KPIs

| KPI | Value |
|---|---:|
| Total Orders | **95K** |
| Total Revenue | **₹52.96M** |
| Total Customers | **22K** |
| Total Restaurants | **550** |
| Total Delivery Partners | **1K** |
| Average Order Value | **560.09** |
| Average Delivery Time | **35.51 minutes** |

### Dashboard Visuals

- Preferred Cuisine Distribution
- Delivery Partners by Vehicle Type
- Customer Type Distribution
- Payment Mode Distribution
- Delivery Efficiency by Partner
- Revenue by Region
- Orders by Region

### Interactive Filters

- Region
- Customer Type
- Vehicle Type
- Preferred Cuisine

### Major Insights

- **Urban** generated the highest revenue.
- **Urban** recorded the highest number of orders.
- **Chinese cuisine** had the highest customer preference.
- **Returning customers** were the largest customer segment.
- **UPI** was the most commonly used payment mode.
- **Bike** was the most common delivery vehicle type.

## 📐 Objective 5 — Statistical & Machine Learning Analysis

### Statistical Analysis

The project performed descriptive statistics, correlation analysis and an independent samples t-test.

### Independent Samples t-Test

The test compared spending between **Loyal** and **New** customers.

```text
T Statistic: -0.1591
P Value:      0.8736
```

**Interpretation:** Since p > 0.05, there is insufficient evidence of a statistically significant difference in average spending between Loyal and New customers.

### Machine Learning

Two regression models were evaluated:

- Linear Regression
- Random Forest Regressor

### Dataset Split

```text
Training Records: 75,640
Testing Records:  18,910
```

### Model Evaluation

| Model | MAE | R² |
|---|---:|---:|
| Linear Regression | 0.6429 | -0.0005 |
| Random Forest | 0.7683 | -0.1794 |

**Best Model:** Linear Regression

The models showed limited predictive power, indicating that additional business and behavioural variables may be required for stronger prediction.

## 💡 Consolidated Business Insights

- **Urban** was the strongest-performing region for orders and revenue.
- **Chinese cuisine** was the most preferred cuisine.
- **Returning customers** formed the largest customer segment.
- **UPI** was the most commonly used payment mode.
- Average delivery time was approximately **35.51 minutes**.
- The t-test found no statistically significant spending difference between Loyal and New customers.
- Machine learning performance was limited with the available features.

## 🎯 Business Recommendations

1. Expand and strengthen operations in the **Urban region** while studying successful practices for other regions.
2. Use customer and regional demand patterns to guide restaurant and cuisine expansion.
3. Monitor delivery partner efficiency, preparation time, delivery speed and delayed deliveries.
4. Prioritize commonly used payment methods while maintaining multiple payment options.
5. Use customer segmentation for targeted engagement.
6. Collect richer behavioural and operational data before deploying predictive models.

## ⚠️ Limitations

- The dataset is intended for capstone/training analysis and may not fully represent a live business.
- Correlation identifies association and does not establish causation.
- Statistical testing was limited to the hypotheses and variables available in the project.
- Machine learning performance was limited by the selected features.
- Additional real-world behavioural, restaurant and operational data could improve future analysis.

## 🚀 Future Scope

- Multivariate regression with additional business variables
- Advanced machine learning models
- Hyperparameter tuning and cross-validation
- Delivery delay prediction
- Customer satisfaction prediction
- Customer retention analysis
- Restaurant performance prediction
- Real-time Power BI reporting
- Time-series demand forecasting
- Advanced delivery partner monitoring
- A/B testing for customer promotions

## 🛠️ Technology Stack

**Data Analysis:** Python, Pandas, NumPy, Matplotlib

**Database:** MySQL, MySQL Workbench, SQL

**Business Intelligence:** Power BI, Power Query, DAX

**Statistics & Machine Learning:** SciPy, Scikit-learn, Linear Regression, Random Forest

**Spreadsheet Analytics:** Microsoft Excel, Pivot Tables, Pivot Charts, KPI Cards, Slicers

## 📁 Suggested Project Structure

```text
FoodDelivery/

├── data/
│   ├── customers.xlsx
│   ├── orders.xlsx
│   ├── restaurants.xlsx
│   ├── delivery_partners.xlsx
│   └── Merged_FoodDelivery_Dataset.xlsx
│
├── Excel/
├── SQL/
├── Python/
├── PowerBI/
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── documentation/
│   ├── Phase_1/
│   ├── Phase_2/
│   ├── Phase_3/
│   ├── Phase_4/
│   ├── Phase_5/
│   ├── Phase_6/
│   ├── Phase_7/
│   ├── Phase_8/
│   ├── Phase_9/
│   └── Phase_10/
│
└── README.md
```

## 🔄 End-to-End Workflow

```text
Raw Food Delivery Data
        ↓
Data Preparation & Validation
        ↓
Excel Business Analysis
        ↓
MySQL Database & SQL Analysis
        ↓
Python EDA & Visualizations
        ↓
Power BI Dashboard
        ↓
Statistical Validation
        ↓
Machine Learning
        ↓
Business Insights
        ↓
Recommendations & Future Scope
```

## 📌 Overall Project Outcome

The project demonstrates a complete business analytics workflow using multiple industry-relevant tools. It converts raw food delivery data into actionable insights covering regional demand, customer behaviour, revenue, cuisine preference, payment usage, delivery performance, statistical validation and predictive modelling.

## 👨‍💻 Project Information

**Project:** Food Delivery Demand Analysis  
**Domain:** Food Delivery / Business Analytics  
**Project Type:** Data Analytics Capstone Project  
**Dataset Size:** 94,550 records × 34 columns  
**Primary Tools:** Excel, MySQL, Python, Power BI, SciPy, Scikit-learn

## ⭐ Key Takeaway

> **The project transforms food delivery data into actionable business insights by combining spreadsheet analysis, SQL, Python EDA, interactive BI reporting, statistical validation, and machine learning.**
