# DA108 | Lab 08 Assignment

## Objective A: [Retail Sales Data Analysis using OOP and Pandas](Retail_Sales_Data_Analysis.ipynb)

You are working as a data analyst for a retail store. The store maintains sales data for its products, and
your task is to process, analyze, and generate reports using Object-Oriented Programming (OOP) and
Pandas.

You first task is to create a CSV file based dataset. You will use the below code snippet for this task. Try to understand the code block, copy it into your local system into a file named `create_dataset.py`. Run the .py file, and verify the created CSV file by opening it in MS Excel (or something similar). 

```py
import pandas as pd

# Define synthetic Indian retail sales data
data = {
    "OrderID": list(range(1001, 1021)),
    "Product": ["Laptop", "Smartphone", "Jeans", "LED TV", "Kurta", "Washing Machine", "Mixer Grinder", "Sports Shoes",
                "Microwave", "Earphones", "Refrigerator", "Sandals", "Tablet", "Hoodie", "Air Fryer", "Chappal",
                "Smartwatch", "Saree", "Jacket", "Toaster"],
    "Category": ["Electronics", "Electronics", "Clothing", "Electronics", "Clothing", "Appliances", "Appliances", 
                 "Footwear", "Appliances", "Electronics", "Appliances", "Footwear", "Electronics", "Clothing",
                 "Appliances", "Footwear", "Electronics", "Clothing", "Clothing", "Appliances"],
    "Quantity": [1, 2, 3, 1, 4, 1, 2, 2, 1, 3, 1, 2, 2, 1, 2, 1, 2, 3, 1, 2],
    "PricePerUnit": [60000, 20000, 1500, 45000, 800, 25000, 3000, 4000, 10000, 1500, 55000, 1200, 25000, 2000, 7000, 
                     500, 7000, 2500, 3500, 2000],
    "TotalPrice": [60000, 40000, 4500, 45000, 3200, 25000, 6000, 8000, 10000, 4500, 55000, 2400, 50000, 2000, 14000, 
                   500, 14000, 7500, 3500, 4000],
    "Date": pd.date_range(start="2024-01-01", periods=20, freq='D').strftime("%Y-%m-%d").tolist(),
    "CustomerID": ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", 
                   "C011", "C012", "C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008"],
    "City": ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
             "Surat", "Nagpur", "Indore", "Bhopal", "Vadodara", "Ludhiana", "Patna", "Kanpur", "Kochi", "Nashik"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sales_data_india.csv", index=False)

print("Indian retail sales dataset saved as 'sales_data_india.csv'")
```

Your next task is to use the `sales_data_india.csv` dataset and accomplish the task in the following assignment.

### Dataset:

You have been given a CSV file (`sales_data.csv`) with the following columns:
- `OrderID`: Unique identifier for the order.
- `Product`: Name of the product.
- `Category`: Product category (e.g., Electronics, Clothing, etc.)
- `Quantity`: Number of items sold.
- `PricePerUnit`: Price per unit of the product.
- `TotalPrice`: Total price (Quantity × PricePerUnit).
- `Date`: Date of purchase.
- `CustomerID`: Unique identifier for the customer.
- `City`: The city where the purchase was made.

### Task
### Part 1: Data Handling with Pandas (Basic)
1. Load the dataset into a Pandas DataFrame.
2. Display the first few rows of the dataset.
3. Handle missing values (if any) by filling or removing them.

### Part 2: Implementing OOP Concepts (Intermediate)

Create a Python class called `SalesDataProcessor` with the following:
- Attributes:
    - `df`: Stores the sales dataset as a Pandas DataFrame.
- Methods:
    - `load_data(file_path)`: Loads the dataset.
    - `clean_data()`: Handles missing values and converts data types.
    - `get_total_sales()`: Returns total sales (`sum of TotalPrice`).
    - `get_unique_products()`: Returns a list of unique products.
    - `get_sales_by_category()`: Returns total sales per product category.
    - `get_top_selling_product()`: Returns the product with the highest sales.

### Part 3: Extending OOP with Inheritance (Advanced)

Create a subclass called `CustomerSalesProcessor`, which extends `SalesDataProcessor` and adds:
- New Methods:
    - `get_total_sales_by_customer(customer_id)`: Returns total sales made by a specific customer.
    - `get_frequent_customers(n)`: Returns the top n customers who made the most purchases.
    - `get_sales_by_city()`: Returns total sales per city.

### Part 4: Data Visualization (Bonus)

1. Plot a **bar chart** showing total sales by category.
2. Plot a **line graph** of daily sales trends.
3. Plot a **pie chart** showing the percentage contribution of different cities to total sales.