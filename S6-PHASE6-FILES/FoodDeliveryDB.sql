-- Task 1: Create Database
CREATE DATABASE FoodDeliveryDB;

USE FoodDeliveryDB;
-- Interpretation
 -- Created a new database named FoodDeliveryDB to store all the food delivery project data.
 -- Selected this database so that all tables and queries are executed inside it.
 
 -- Task 2: Create Tables
 -- Customers Table
CREATE TABLE customers (
    Customer_ID VARCHAR(10) PRIMARY KEY,
    Gender VARCHAR(10),
    Age_Group VARCHAR(20),
    Region VARCHAR(30),
    Customer_Type VARCHAR(30),
    Total_Orders INT,
    Average_Spend DECIMAL(10,2),
    Preferred_Cuisine VARCHAR(50)
);

-- Interpretation
-- Created the customers table to store customer information such as gender, age group, region, customer type, spending behavior, and preferred cuisine. The Customer_ID uniquely identifies each customer.

-- Restaurants Table
CREATE TABLE restaurants (
    Restaurant_ID VARCHAR(10) PRIMARY KEY,
    Region VARCHAR(30),
    Avg_Preparation_Time_Minutes INT,
    Avg_Rating DECIMAL(3,2),
    Order_Capacity_Per_Day INT,
    Restaurant_Name VARCHAR(100),
    Cuisine_Type VARCHAR(50)
);

-- Interpretation
-- Created the restaurants table to store restaurant details including location, cuisine type, preparation time, ratings, and daily order capacity. Restaurant_ID is the primary key.

-- Delivery Partners Table
CREATE TABLE delivery_partners (
    Delivery_Partner_ID VARCHAR(10) PRIMARY KEY,
    Partner_Name VARCHAR(100),
    Vehicle_Type VARCHAR(30),
    Avg_Delivery_Speed_KMPH DECIMAL(5,2),
    Successful_Deliveries INT,
    Delayed_Deliveries INT,
    Avg_Customer_Rating DECIMAL(3,2),
    Region VARCHAR(30),
    Delivery_Efficiency_Score DECIMAL(5,2)
);

-- Interpretation
-- Created the delivery_partners table to store information about delivery executives, including vehicle type, delivery speed, customer ratings, delivery performance, and efficiency score.

-- Orders Table
CREATE TABLE orders (
    Order_ID VARCHAR(15) PRIMARY KEY,
    Order_Date DATE,
    Customer_ID VARCHAR(10),
    Restaurant_ID VARCHAR(10),
    Region VARCHAR(30),
    Delivery_Partner_ID VARCHAR(10),
    Order_Value DECIMAL(10,2),
    Delivery_Fee DECIMAL(10,2),
    Discount_Applied DECIMAL(10,2),
    Final_Amount DECIMAL(10,2),
    Payment_Mode VARCHAR(30),
    Order_Status VARCHAR(30),
    Delivery_Time_Minutes INT,
    Order_Rating INT,
    Festival_Flag TINYINT(1)
);

-- Interpretation
-- Created the orders table to store complete order information including customer, restaurant, delivery partner, payment details, delivery time, ratings, and festival status.

-- Task 3: Import Data
-- Check Local File Import
SHOW VARIABLES LIKE 'local_infile';

-- Interpretation
-- Checked whether the MySQL server allows importing data from local files.

LOAD DATA LOCAL INFILE 'C:/Users/Megh/OneDrive/Desktop/NIIT_DA/CAPSTONE_PROJECT/project-topic-07-main/project-topic-07-main/Orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Interpretation
-- Imported the Orders.csv file into the orders table using MySQL's bulk data import feature.

-- Display All Records
SELECT * FROM customers;
SELECT * FROM restaurants;
SELECT * FROM delivery_partners;
SELECT * FROM orders;

-- Interpretation
-- Displayed all records from each table to verify that the data was imported successfully.

-- Count Total Records
SELECT COUNT(*) AS Customers FROM customers;
SELECT COUNT(*) AS Restaurants FROM restaurants;
SELECT COUNT(*) AS Delivery_Partners FROM delivery_partners;
SELECT COUNT(*) AS Orders FROM orders;

-- Interpretation
-- Counted the total number of records in each table to confirm that the complete datasets were imported correctly.

-- Task 4: Create Relationships
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY(Customer_ID)
REFERENCES customers(Customer_ID);

-- Interpretation
-- Created a relationship between the orders table and the customers table using Customer_ID.

ALTER TABLE orders
ADD CONSTRAINT fk_restaurant
FOREIGN KEY(Restaurant_ID)
REFERENCES restaurants(Restaurant_ID);

-- Interpretation
-- Connected each order with its respective restaurant using Restaurant_ID.

ALTER TABLE orders
ADD CONSTRAINT fk_partner
FOREIGN KEY(Delivery_Partner_ID)
REFERENCES delivery_partners(Delivery_Partner_ID);

-- Interpretation
-- Linked every order with the corresponding delivery partner using Delivery_Partner_ID.

SHOW CREATE TABLE orders;

-- Interpretation
-- Displayed the complete structure of the orders table to verify that the foreign key relationships were created successfully.

-- Task 5: Business Analysis Queries
-- Total Orders
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- Interpretation
-- Calculated the total number of orders placed.

-- Total Revenue
SELECT
ROUND(SUM(Final_Amount),2) AS Total_Revenue
FROM orders;

-- Interpretation
-- Calculated the total revenue earned from all completed orders.

-- Average Order Value
SELECT
ROUND(AVG(Order_Value),2) AS Average_Order_Value
FROM orders;

-- Interpretation
-- Calculated the average value of all customer orders.

-- Orders by Region
SELECT
Region,
COUNT(*) AS Total_Orders
FROM orders
GROUP BY Region
ORDER BY Total_Orders DESC;

-- Interpretation
-- Compared the number of orders placed in each region and displayed them from highest to lowest.

-- Revenue by Region
SELECT
Region,
ROUND(SUM(Final_Amount),2) AS Revenue
FROM orders
GROUP BY Region
ORDER BY Revenue DESC;

-- Interpretation
-- Calculated the total revenue generated by each region.

-- Customer Type Distribution
SELECT
Customer_Type,
COUNT(*) AS Customers
FROM customers
GROUP BY Customer_Type;

-- Interpretation
-- Displayed the number of customers belonging to each customer category.

-- Average Customer Spend
SELECT
ROUND(AVG(Average_Spend),2) AS Average_Customer_Spend
FROM customers;

-- Interpretation
-- Calculated the average amount spent by customers.

-- Preferred Cuisine
SELECT
Preferred_Cuisine,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY Preferred_Cuisine
ORDER BY Total_Customers DESC;

-- Interpretation
-- Identified the most preferred cuisine among customers. 

-- Top Rated Restaurants
SELECT
Restaurant_Name,
Cuisine_Type,
Avg_Rating
FROM restaurants
ORDER BY Avg_Rating DESC
LIMIT 10;

-- Interpretation
-- Displayed the top 10 highest-rated restaurants.

-- Restaurants by Region
SELECT
Region,
COUNT(*) AS Total_Restaurants
FROM restaurants
GROUP BY Region;

-- Interpretation
-- Counted the number of restaurants available in each region.

-- Average Preparation Time
SELECT
ROUND(AVG(Avg_Preparation_Time_Minutes),2) AS Avg_Preparation_Time
FROM restaurants;

-- Interpretation
-- Calculated the average time taken by restaurants to prepare orders.

-- Delivery Partner Performance
SELECT
Partner_Name,
Delivery_Efficiency_Score
FROM delivery_partners
ORDER BY Delivery_Efficiency_Score DESC;

-- Interpretation
-- Listed delivery partners according to their efficiency scores.

-- Vehicle Type Distribution
SELECT
Vehicle_Type,
COUNT(*) AS Total
FROM delivery_partners
GROUP BY Vehicle_Type;

-- Interpretation
-- Displayed the number of delivery partners using each type of vehicle.

-- Average Delivery Speed
SELECT
ROUND(AVG(Avg_Delivery_Speed_KMPH),2) AS Avg_Speed
FROM delivery_partners;

-- Interpretation
-- Calculated the average delivery speed of all delivery partners.

-- Average Delivery Time
SELECT
ROUND(AVG(Delivery_Time_Minutes),2) AS Average_Delivery_Time
FROM orders;

-- Interpretation
-- Calculated the average time taken to deliver customer orders

-- Payment Mode Analysis
SELECT
Payment_Mode,
COUNT(*) AS Total_Transactions
FROM orders
GROUP BY Payment_Mode
ORDER BY Total_Transactions DESC;

-- Interpretation
-- Displayed the number of transactions completed using each payment method.

-- Order Status Analysis
SELECT
Order_Status,
COUNT(*) AS Orders
FROM orders
GROUP BY Order_Status;

-- Interpretation
-- Counted the number of orders under each order status such as Delivered or Cancelled.

-- Festival vs Non-Festival Analysis
SELECT
Festival_Flag,
COUNT(*) AS Orders,
ROUND(SUM(Final_Amount),2) AS Revenue
FROM orders
GROUP BY Festival_Flag;

-- Interpretation
-- Compared the total orders and revenue generated during festival and non-festival periods.

-- Highest Value Orders
SELECT
Order_ID,
Final_Amount
FROM orders
ORDER BY Final_Amount DESC
LIMIT 10;

-- Interpretation
-- Displayed the top 10 highest-value customer orders.

-- Region-wise Delivery Performance
SELECT
Region,
ROUND(AVG(Delivery_Time_Minutes),2) AS Avg_Delivery_Time
FROM orders
GROUP BY Region
ORDER BY Avg_Delivery_Time;

-- Interpretation
-- Compared the average delivery time across different regions.

-- Customer Spending Analysis (JOIN) 
SELECT
c.Customer_ID,
c.Customer_Type,
COUNT(o.Order_ID) AS Total_Orders,
ROUND(SUM(o.Final_Amount),2) AS Total_Spent
FROM customers c
JOIN orders o
ON c.Customer_ID = o.Customer_ID
GROUP BY c.Customer_ID, c.Customer_Type
ORDER BY Total_Spent DESC;

-- Interpretation
-- Joined the customers and orders tables to calculate each customer's total orders and total spending.

-- Restaurant Revenue Analysis (JOIN)
SELECT
r.Restaurant_Name,
ROUND(SUM(o.Final_Amount),2) AS Revenue
FROM restaurants r
JOIN orders o
ON r.Restaurant_ID = o.Restaurant_ID
GROUP BY r.Restaurant_Name
ORDER BY Revenue DESC;

-- Interpretation
-- Joined the restaurants and orders tables to calculate revenue generated by each restaurant.

-- Delivery Partner Performance (JOIN)
SELECT
d.Partner_Name,
COUNT(o.Order_ID) AS Orders_Delivered,
ROUND(AVG(o.Delivery_Time_Minutes),2) AS Avg_Delivery_Time
FROM delivery_partners d
JOIN orders o
ON d.Delivery_Partner_ID = o.Delivery_Partner_ID
GROUP BY d.Partner_Name
ORDER BY Orders_Delivered DESC;

-- Interpretation
-- Joined the delivery_partners and orders tables to analyze the number of deliveries completed and the average delivery time for each delivery partner.

-- Complete Business Report (4-Table JOIN)
SELECT
o.Order_ID,
o.Order_Date,
c.Customer_Type,
r.Restaurant_Name,
r.Cuisine_Type,
d.Partner_Name,
o.Final_Amount,
o.Delivery_Time_Minutes,
o.Payment_Mode,
o.Order_Status
FROM orders o
JOIN customers c
ON o.Customer_ID = c.Customer_ID
JOIN restaurants r
ON o.Restaurant_ID = r.Restaurant_ID
JOIN delivery_partners d
ON o.Delivery_Partner_ID = d.Delivery_Partner_ID;

-- Interpretation
-- Joined all four tables (customers, orders, restaurants, and delivery_partners) to generate a comprehensive report showing customer details, restaurant information, delivery partner, payment mode, order amount, and order status in a single result set.