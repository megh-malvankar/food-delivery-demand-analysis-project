# ===============================================================
# OBJECTIVE 3
# Python And EDA
# ===============================================================

# ----------------------------------------------------------
# Task 1 – Import Libraries & Load Data
# ----------------------------------------------------------
from xml.dom.minidom import Identified

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Load Datasets
# -------------------------------

customers = pd.read_excel("data/Customers.xlsx")

orders = pd.read_excel("data/Orders.xlsx")

restaurants = pd.read_excel(
    "data/Restaurants.xlsx",
    sheet_name=0      # First sheet
)

delivery = pd.read_excel(
    "data/Delivery_Partners.xlsx",
    sheet_name=0      # First sheet
)

# -------------------------------
# Dataset Information
# -------------------------------

print("Customers Shape:", customers.shape)
print("Orders Shape:", orders.shape)
print("Restaurants Shape:", restaurants.shape)
print("Delivery Shape:", delivery.shape)

# -------------------------------
# Preview Data
# -------------------------------

print("\nCustomers")
print(customers.head())

print("\nOrders")
print(orders.head())

print("\nRestaurants")
print(restaurants.head())

print("\nDelivery Partners")
print(delivery.head())

# -------------------------------
# Data Types
# -------------------------------

print("\nCustomers Info")
customers.info()

print("\nOrders Info")
orders.info()

print("\nRestaurants Info")
restaurants.info()

print("\nDelivery Partners Info")
delivery.info()

# -------------------------------
# Missing Values
# -------------------------------

print("\nMissing Values - Customers")
print(customers.isnull().sum())

print("\nMissing Values - Orders")
print(orders.isnull().sum())

print("\nMissing Values - Restaurants")
print(restaurants.isnull().sum())

print("\nMissing Values - Delivery Partners")
print(delivery.isnull().sum())

# -------------------------------
# Duplicate Records
# -------------------------------

print("\nDuplicate Records")

print("Customers :", customers.duplicated().sum())
print("Orders :", orders.duplicated().sum())
print("Restaurants :", restaurants.duplicated().sum())
print("Delivery Partners :", delivery.duplicated().sum())

# ----------------------------------------------------------
# Task 2 – Data Validation & Understanding
# ----------------------------------------------------------

# 1. Display Column Names
# -------------------------------
# Column Names
# -------------------------------

print("\nCustomers Columns")
print(customers.columns.tolist())

print("\nOrders Columns")
print(orders.columns.tolist())

print("\nRestaurants Columns")
print(restaurants.columns.tolist())

print("\nDelivery Partners Columns")
print(delivery.columns.tolist())

# 2. Statistical Summary
# -------------------------------
# Statistical Summary
# -------------------------------

print("\nCustomers Summary")
print(customers.describe(include='all'))

print("\nOrders Summary")
print(orders.describe(include='all'))

print("\nRestaurants Summary")
print(restaurants.describe(include='all'))

print("\nDelivery Partners Summary")
print(delivery.describe(include='all'))

# 3. Check Unique Values
# -------------------------------
# Unique Values
# -------------------------------

print("\nCustomer Regions")
print(customers["Region"].unique())

print("\nOrder Regions")
print(orders["Region"].unique())

print("\nRestaurant Regions")
print(restaurants["Region"].unique())

print("\nDelivery Regions")
print(delivery["Region"].unique())

# 4. Count Unique Records
# -------------------------------
# Unique Record Counts
# -------------------------------

print("Customers :", customers["Customer_ID"].nunique())

print("Orders :", orders["Order_ID"].nunique())

print("Restaurants :", restaurants["Restaurant_ID"].nunique())

print("Delivery Partners :", delivery["Delivery_Partner_ID"].nunique())

# 5. Check Invalid Numeric Values
# -------------------------------
# Invalid Values
# -------------------------------

print("\nNegative Order Values")
print((orders["Order_Value"] < 0).sum())

print("\nNegative Delivery Fee")
print((orders["Delivery_Fee"] < 0).sum())

print("\nNegative Final Amount")
print((orders["Final_Amount"] < 0).sum())

# 6. Verify Key Columns
# -------------------------------
# Primary Key Null Check
# -------------------------------

print(customers["Customer_ID"].isnull().sum())

print(orders["Order_ID"].isnull().sum())

print(restaurants["Restaurant_ID"].isnull().sum())

print(delivery["Delivery_Partner_ID"].isnull().sum())

# ----------------------------------------------------------
# Task 3 – Data Integration (Merge)
# ----------------------------------------------------------

# Merge Customers
merged_df = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="left",
    suffixes=("", "_Customer")
)

# Merge Restaurants
merged_df = pd.merge(
    merged_df,
    restaurants[
        [
            "Restaurant_ID",
            "Restaurant_Name",
            "Cuisine_Type",
            "Avg_Preparation_Time_Minutes",
            "Avg_Rating",
            "Order_Capacity_Per_Day"
        ]
    ],
    on="Restaurant_ID",
    how="left"
)

# Merge Delivery Partners
merged_df = pd.merge(
    merged_df,
    delivery[
        [
            "Delivery_Partner_ID",
            "Partner_Name",
            "Vehicle_Type",
            "Avg_Delivery_Speed_KMPH",
            "Successful_Deliveries",
            "Delayed_Deliveries",
            "Avg_Customer_Rating",
            "Delivery_Efficiency_Score"
        ]
    ],
    on="Delivery_Partner_ID",
    how="left"
)

# ----------------------------------------------------------
# Verify Merge
# ----------------------------------------------------------

print("\nMerged Dataset Shape:")
print(merged_df.shape)

print("\nMerged Dataset Preview:")
print(merged_df.head())

# ----------------------------------------------------------
# Missing Values After Merge
# ----------------------------------------------------------

print("\nMissing Values After Merge")
print(merged_df.isnull().sum())

# ----------------------------------------------------------
# Save Master Dataset
# ----------------------------------------------------------

merged_df.to_excel(
    "Merged_FoodDelivery_Dataset.xlsx",
    index=False
)

print("\nMerged dataset saved successfully.")

# ----------------------------------------------------------
# Task 4 – Exploratory Data Analysis (EDA)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Total Orders
# ----------------------------------------------------------

total_orders = merged_df["Order_ID"].count()

print("\n---------- Total Orders ----------")
print("Total Orders :", total_orders)

# ----------------------------------------------------------
# Revenue Analysis
# ----------------------------------------------------------

total_revenue = merged_df["Final_Amount"].sum()

average_order_value = merged_df["Final_Amount"].mean()

print("\n---------- Revenue Analysis ----------")
print("Total Revenue :", round(total_revenue,2))
print("Average Order Value :", round(average_order_value,2))

# ----------------------------------------------------------
# Revenue by Region
# ----------------------------------------------------------

revenue_region = (
    merged_df
    .groupby("Region")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n---------- Revenue by Region ----------")
print(revenue_region)

# ----------------------------------------------------------
# Customer Type Analysis
# ----------------------------------------------------------

customer_type = merged_df["Customer_Type"].value_counts()

print("\n---------- Customer Type ----------")
print(customer_type)

# ----------------------------------------------------------
# Preferred Cuisine
# ----------------------------------------------------------

preferred_cuisine = (
    merged_df["Preferred_Cuisine"]
    .value_counts()
)

print("\n---------- Preferred Cuisine ----------")
print(preferred_cuisine)

# ----------------------------------------------------------
# Restaurant Ratings
# ----------------------------------------------------------

restaurant_rating = (
    merged_df.groupby("Restaurant_Name")["Avg_Rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\n---------- Restaurant Ratings ----------")
print(restaurant_rating.head(10))

# ----------------------------------------------------------
# Delivery Time
# ----------------------------------------------------------

avg_delivery = merged_df["Delivery_Time_Minutes"].mean()

print("\n---------- Delivery Time ----------")
print("Average Delivery Time :", round(avg_delivery,2))

# ----------------------------------------------------------
# Payment Mode
# ----------------------------------------------------------

payment_mode = (
    merged_df["Payment_Mode"]
    .value_counts()
)

print("\n---------- Payment Mode ----------")
print(payment_mode)

# ----------------------------------------------------------
# Festival Analysis
# ----------------------------------------------------------

festival_orders = (
    merged_df.groupby("Festival_Flag")
    .agg(
        Orders=("Order_ID","count"),
        Revenue=("Final_Amount","sum")
    )
)

print("\n---------- Festival Analysis ----------")
print(festival_orders)

# ----------------------------------------------------------
# Top Restaurants
# ----------------------------------------------------------

top_restaurants = (
    merged_df.groupby("Restaurant_Name")
    .agg(
        Revenue=("Final_Amount","sum"),
        Orders=("Order_ID","count")
    )
    .sort_values(by="Revenue",ascending=False)
)

print("\n---------- Top Restaurants ----------")
print(top_restaurants.head(10))

# ----------------------------------------------------------
# Delivery Efficiency
# ----------------------------------------------------------

delivery_efficiency = (
    merged_df.groupby("Partner_Name")
    ["Delivery_Efficiency_Score"]
    .mean()
    .sort_values(ascending=False)
)

print("\n---------- Delivery Efficiency ----------")
print(delivery_efficiency.head(10))

import os

# Create Charts Folder
os.makedirs("outputs/charts", exist_ok=True)

plt.close('all')

# Visualization 1 – Orders by Region (Bar Chart)
# ----------------------------------------------------------
# Orders by Region
# ----------------------------------------------------------

orders_region = merged_df["Region"].value_counts()

plt.figure(figsize=(8,5))

orders_region.plot(kind="bar")
for i, value in enumerate(orders_region):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=9)

plt.title("Orders by Region", fontweight="bold")
plt.xlabel("Region")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/charts/orders_by_region.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Compared the number of orders received from each region.
# Identified regions with the highest customer demand.

# Visualization 2 – Revenue by Region (Bar Chart)
# ----------------------------------------------------------
# Revenue by Region
# ----------------------------------------------------------

revenue_region = merged_df.groupby("Region")["Final_Amount"].sum()

plt.figure(figsize=(8,5))

revenue_region.plot(kind="bar")
for i, value in enumerate(revenue_region):
    plt.text(i, value, f"{value:,.0f}", ha='center', va='bottom', fontsize=9)

plt.title("Revenue by Region", fontweight="bold")

plt.xlabel("Region")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/charts/revenue_by_region.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Compared total revenue generated by each region.
# Highlighted the regions contributing the highest revenue.

# Visualization 3 – Customer Type Distribution (Pie Chart)
# ----------------------------------------------------------
# Customer Type Distribution
# ----------------------------------------------------------

customer_type = merged_df["Customer_Type"].value_counts()

plt.figure(figsize=(7,7))

customer_type.plot(
    kind="pie",
    autopct=lambda p: f'{p:.1f}%\n({int(p*customer_type.sum()/100)})'
)

plt.title("Customer Type Distribution", fontweight="bold")

plt.ylabel("")

plt.savefig("outputs/charts/customer_type_distribution.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Showed the percentage distribution of different customer types.
# Helped identify the dominant customer category.

# Visualization 4 – Preferred Cuisine (Bar Chart)
# ----------------------------------------------------------
# Preferred Cuisine
# ----------------------------------------------------------

cuisine = merged_df["Preferred_Cuisine"].value_counts()

plt.figure(figsize=(8,5))

cuisine.plot(kind="bar")
for i, value in enumerate(cuisine):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=9)

plt.title("Preferred Cuisine", fontweight="bold")

plt.xlabel("Cuisine")

plt.ylabel("Customers")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/charts/preferred_cuisine.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Compared customer preferences across different cuisines.
# Identified the most popular cuisine choices.

# Visualization 5 – Payment Mode Distribution (Pie Chart)
# ----------------------------------------------------------
# Payment Mode
# ----------------------------------------------------------

payment = merged_df["Payment_Mode"].value_counts()

plt.figure(figsize=(7,7))

payment.plot(
    kind="pie",
    autopct=lambda p: f'{p:.1f}%\n({int(p*payment.sum()/100)})'
)

plt.title("Payment Mode Distribution", fontweight="bold")

plt.ylabel("")

plt.savefig("outputs/charts/payment_mode_distribution.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Displayed the proportion of transactions by payment method.
# Helped understand customer payment preferences.

# Visualization 6 – Restaurant Ratings (Histogram)
# ----------------------------------------------------------
# Restaurant Ratings
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

counts, bins, patches = plt.hist(
    merged_df["Avg_Rating"],
    bins=10
)

for count, left, right in zip(counts, bins[:-1], bins[1:]):
    plt.text(
        (left + right) / 2,
        count,
        str(int(count)),
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.title("Restaurant Ratings", fontweight="bold")

plt.xlabel("Rating")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("outputs/charts/restaurant_ratings.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Displayed the distribution of restaurant ratings.
# Showed how ratings vary across restaurants.

# Visualization 7 – Delivery Time (Histogram)
# ----------------------------------------------------------
# Delivery Time
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

counts, bins, patches = plt.hist(
    merged_df["Delivery_Time_Minutes"],
    bins=10
)

for count, left, right in zip(counts, bins[:-1], bins[1:]):
    plt.text(
        (left + right) / 2,
        count,
        str(int(count)),
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.title("Delivery Time Distribution", fontweight="bold")

plt.xlabel("Minutes")

plt.ylabel("Orders")

plt.tight_layout()

plt.savefig("outputs/charts/delivery_time.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Visualized the spread of delivery times.
# Helped identify common delivery durations.

# Visualization 8 – Vehicle Type Distribution (Bar Chart)
# ----------------------------------------------------------
# Vehicle Type
# ----------------------------------------------------------

vehicle = merged_df["Vehicle_Type"].value_counts()

plt.figure(figsize=(8,5))

vehicle.plot(kind="bar")
for i, value in enumerate(vehicle):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=9)

plt.title("Vehicle Type Distribution", fontweight="bold")

plt.xlabel("Vehicle Type")

plt.ylabel("Delivery Partners")

plt.tight_layout()

plt.savefig("outputs/charts/vehicle_type.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Compared the number of delivery partners using each vehicle type.
# Showed the most commonly used delivery vehicles.

# Visualization 9 – Delivery Efficiency (Bar Chart)
# ----------------------------------------------------------
# Delivery Efficiency
# ----------------------------------------------------------

efficiency = (
    merged_df
    .groupby("Partner_Name")["Delivery_Efficiency_Score"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))

efficiency.plot(kind="bar")
for i, value in enumerate(efficiency):
    plt.text(i, value, f"{value:.2f}", ha='center', va='bottom', fontsize=9)

plt.title("Top 10 Delivery Partners by Efficiency", fontweight="bold")

plt.xlabel("Delivery Partner")

plt.ylabel("Efficiency Score")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/charts/delivery_efficiency.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Compared delivery partners based on efficiency scores.
# Highlighted the highest-performing delivery partners.

# Visualization 10 – Festival vs Non-Festival Orders (Bar Chart)
# ----------------------------------------------------------
# Festival Analysis
# ----------------------------------------------------------

festival = merged_df["Festival_Flag"].value_counts()

plt.figure(figsize=(6,5))

festival.plot(kind="bar")
for i, value in enumerate(festival):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=9)

plt.title("Festival vs Non-Festival Orders", fontweight="bold")

plt.xlabel("Festival Flag")

plt.ylabel("Orders")

plt.tight_layout()

plt.savefig("outputs/charts/festival_orders.png")

plt.show(block=False)
plt.pause(1)
plt.close()
# Interpretation
# Compared the number of orders placed during festival and non-festival periods.
# Helped evaluate the impact of festivals on order demand.

# Task 6 – Business Insights
# 1. Highest Revenue-Generating Region
# ----------------------------------------------------------
# Highest Revenue-Generating Region
# ----------------------------------------------------------

highest_revenue_region = (
    merged_df.groupby("Region")["Final_Amount"]
    .sum()
    .idxmax()
)

highest_revenue = (
    merged_df.groupby("Region")["Final_Amount"]
    .sum()
    .max()
)

print("\n---------- Business Insight 1 ----------")
print(f"Highest Revenue Region : {highest_revenue_region}")
print(f"Revenue Generated : {highest_revenue:.2f}")
# Interpretation
# Identified the region contributing the highest total revenue.
# This region represents the strongest-performing market for the business.

# 2. Region with Maximum Orders
# ----------------------------------------------------------
# Region with Maximum Orders
# ----------------------------------------------------------

orders_region = merged_df["Region"].value_counts()

print("\n---------- Business Insight 2 ----------")
print("Region with Maximum Orders :", orders_region.idxmax())
print("Total Orders :", orders_region.max())
# Interpretation
# Determined the region receiving the largest number of customer orders.
# This helps identify areas with the highest customer demand.

# 3. Most Preferred Cuisine
# ----------------------------------------------------------
# Most Preferred Cuisine
# ----------------------------------------------------------

preferred_cuisine = merged_df["Preferred_Cuisine"].value_counts()

print("\n---------- Business Insight 3 ----------")
print("Most Preferred Cuisine :", preferred_cuisine.idxmax())
print("Customers :", preferred_cuisine.max())
# Interpretation
# Identified the cuisine most frequently preferred by customers.
# This insight can guide restaurant partnerships and menu planning.

# 4. Best Performing Restaurant
# ----------------------------------------------------------
# Best Performing Restaurant
# ----------------------------------------------------------

restaurant_revenue = (
    merged_df.groupby("Restaurant_Name")
    .agg(
        Revenue=("Final_Amount","sum"),
        Rating=("Avg_Rating","mean")
    )
)

best_restaurant = restaurant_revenue["Revenue"].idxmax()

print("\n----------Business Insight 4 ----------")
print("Best Performing Restaurant :", best_restaurant)

print(restaurant_revenue.loc[best_restaurant])
# Interpretation
# Identified the restaurant generating the highest revenue.
# Also reviewed its average customer rating to evaluate performance.

# 5. Best Delivery Partner
# ----------------------------------------------------------
# Best Delivery Partner
# ----------------------------------------------------------

partner = (
    merged_df.groupby("Partner_Name")
    ["Delivery_Efficiency_Score"]
    .mean()
)

print("\n---------- Business Insight 5 ----------")
print("Best Delivery Partner :", partner.idxmax())
print("Efficiency Score :", round(partner.max(),2))
# Interpretation
# Identified the delivery partner with the highest efficiency score.
# This helps recognize high-performing delivery personnel.

# 6. Most Common Payment Mode
# ----------------------------------------------------------
# Payment Mode
# ----------------------------------------------------------

payment = merged_df["Payment_Mode"].value_counts()

print("\n---------- Business Insight 6 ----------")
print("Most Common Payment Mode :", payment.idxmax())
print("Transactions :", payment.max())
# Interpretation
# Identified the payment method most frequently used by customers.
# This reflects customer payment preferences.

# 7. Festival Impact
# ----------------------------------------------------------
# Festival Analysis
# ----------------------------------------------------------

festival = (
    merged_df.groupby("Festival_Flag")
    .agg(
        Orders=("Order_ID","count"),
        Revenue=("Final_Amount","sum")
    )
)

print("\n---------- Business Insight 7 ----------")
print(festival)
# Interpretation
# Compared order volume and revenue during festival and non-festival periods.
# Assessed how festivals influence customer demand and sales.

# 8. Customer Spending Trend
# ----------------------------------------------------------
# Customer Spending
# ----------------------------------------------------------

customer_spending = (
    merged_df.groupby("Customer_Type")
    ["Final_Amount"]
    .mean()
)

print("\n---------- Business Insight 8 ----------")
print(customer_spending)
# Interpretation
# Compared average spending across different customer categories.
# Identified customer segments contributing higher average revenue.

# 9. Recommendation for Market Expansion
# ----------------------------------------------------------
# Market Expansion
# ----------------------------------------------------------

market = (
    merged_df.groupby("Region")
    .agg(
        Revenue=("Final_Amount","sum"),
        Orders=("Order_ID","count")
    )
    .sort_values(by="Revenue",ascending=False)
)

print("\n---------- Business Insight 9 ----------")
print(market)
# Interpretation
# Ranked regions by revenue and order volume.
# Helps identify high-potential regions for future market expansion.

# 10. Delivery Improvement Suggestions
# ----------------------------------------------------------
# Delivery Performance
# ----------------------------------------------------------

delivery_performance = (
    merged_df.groupby("Partner_Name")
    .agg(
        Avg_Delivery_Time=("Delivery_Time_Minutes","mean"),
        Efficiency=("Delivery_Efficiency_Score","mean")
    )
    .sort_values(by="Avg_Delivery_Time")
)

print("\n---------- Business Insight 10 ----------")
print(delivery_performance.head(10))
# Interpretation
# Compared delivery partners using delivery time and efficiency score.
# Helps identify best practices and opportunities to improve delivery operations.

# Final Conclusion

print("\n----------------------------------------------------------")
print("        FOOD DELIVERY BUSINESS INSIGHTS")
print("----------------------------------------------------------")

print("✓ Regional demand and revenue patterns were identified.")
print("✓ Customer purchasing behaviour was analyzed.")
print("✓ Restaurant performance was evaluated.")
print("✓ Delivery partner efficiency was assessed.")
print("✓ Payment preferences were identified.")
print("✓ Festival impact on business was evaluated.")
print("✓ Customer spending trends were analyzed.")
print("✓ Regions suitable for expansion were identified.")
print("✓ Operational improvements for delivery efficiency were suggested.")

print("\nProject Completed Successfully.")

# Interpretation
# Objective 3 successfully demonstrated the use of Python for end-to-end data analysis by importing, validating, integrating, analyzing, and visualizing the food delivery datasets. Using libraries such as Pandas, NumPy, and Matplotlib, the project transformed raw data into meaningful information through exploratory data analysis, charts, and business insights. The analysis identified important trends related to regional demand, customer preferences, restaurant performance, delivery efficiency, payment methods, and festival impact, enabling data-driven decision-making. Overall, this objective established a strong analytical foundation for the remaining stages of the capstone project, including Power BI visualization, predictive modeling, and the final business recommendations.