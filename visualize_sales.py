import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder to store charts
os.makedirs("sales_charts", exist_ok=True)

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Ensure the Date column is treated as datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set Seaborn style
sns.set(style="whitegrid")

# -----------------------------
# 1️⃣ Daily Revenue Trend
# -----------------------------
daily_revenue = df.groupby("Date")["Revenue ($)"].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(x="Date", y="Revenue ($)", data=daily_revenue, marker="o", linewidth=2)
plt.title("📈 Daily Revenue Trend", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_charts/revenue_trend.png", dpi=300)
plt.show()

# -----------------------------
# 2️⃣ Revenue by Product
# -----------------------------
product_revenue = (
    df.groupby("Product")["Revenue ($)"]
    .sum()
    .reset_index()
    .sort_values(by="Revenue ($)", ascending=False)
)

plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Revenue ($)", data=product_revenue, palette="Blues_d")
plt.title("💰 Total Revenue by Product", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig("sales_charts/product_revenue.png", dpi=300)
plt.show()

# -----------------------------
# 3️⃣ Total Quantity Sold per Product
# -----------------------------
plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Quantity Sold", data=df, estimator=sum, ci=None, palette="Greens_d")
plt.title("📦 Total Quantity Sold per Product", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("sales_charts/quantity_sold.png", dpi=300)
plt.show()

print("✅ Charts generated and saved in 'sales_charts/' folder successfully!")
