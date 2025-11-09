import csv

# Define the file name
filename = "sales_data.csv"

# Define the header
header = ["Date (YYYY-MM-DD)", "Product", "Quantity Sold", "Revenue ($)"]

# Define the sales data
rows = [
    ["2025-11-01", "Laptop", 15, 15000],
    ["2025-11-02", "Smartphone", 30, 18000],
    ["2025-11-03", "Tablet", 20, 8000],
    ["2025-11-04", "Headphones", 25, 5000],
    ["2025-11-05", "Smartwatch", 10, 7000]
]

# Write data to CSV file
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print(f"✅ CSV file '{filename}' created successfully!")


import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv("sales_data.csv")

# Step 2: Calculate the total revenue
total_revenue = df["Revenue ($)"].sum()

# Step 3: Find the best-selling product (based on Quantity Sold)
best_selling_product = df.loc[df["Quantity Sold"].idxmax(), "Product"]

# Step 4: Identify the day with the highest sales (Revenue)
best_sales_day = df.loc[df["Revenue ($)"].idxmax(), "Date (YYYY-MM-DD)"]

# Step 5: Prepare the summary text
summary = (
    "=== Sales Summary Report ===\n"
    f"Total Revenue: ${total_revenue:,.2f}\n"
    f"Best-Selling Product: {best_selling_product}\n"
    f"Day with Highest Sales: {best_sales_day}\n"
)

# Step 6: Save the summary to a text file
with open("sales_summary.txt", "w") as file:
    file.write(summary)

print("✅ Sales summary generated successfully!")
print(summary)


