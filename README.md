# ==============================================================

# 📊 DATA ANALYSIS AND VISUALIZATION ASSIGNMENT

# ==============================================================

# Objective:

# Task 1: Load and Explore the Dataset

# Task 2: Perform Basic Data Analysis

# Task 3: Create Visualizations using Matplotlib & Seaborn

# ==============================================================

# Import required libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --------------------------------------------------------------

# 🧩 Task 1: Load and Explore the Dataset

# --------------------------------------------------------------

print("=== Task 1: Loading and Exploring the Dataset ===\n")

try:
# Load the Iris dataset from sklearn
iris_data = load_iris()

```
# Convert to a pandas DataFrame
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df["species"] = [iris_data.target_names[i] for i in iris_data.target]

# Display first few rows
print("Preview of the Dataset:")
print(df.head(), "\n")

# Check data types and missing values
print("Data Types:")
print(df.dtypes, "\n")

print("Checking for Missing Values:")
print(df.isnull().sum(), "\n")

# Clean dataset (fill or drop missing values if any)
if df.isnull().values.any():
    df.fillna(df.mean(), inplace=True)
    print("Missing values filled with column means.\n")
else:
    print("No missing values found.\n")
```

except FileNotFoundError:
print("Error: Dataset file not found.")
except Exception as e:
print(f"An unexpected error occurred: {e}")

# --------------------------------------------------------------

# 📈 Task 2: Basic Data Analysis

# --------------------------------------------------------------

print("=== Task 2: Basic Data Analysis ===\n")

# Compute basic statistics

print("Summary Statistics:")
print(df.describe(), "\n")

# Grouping by species and computing mean values

species_mean = df.groupby("species").mean()
print("Average Measurements per Species:")
print(species_mean, "\n")

# Identify patterns / findings

print("Observations:")
print("- Setosa species tend to have smaller petal lengths and widths.")
print("- Virginica species generally have larger flower dimensions.")
print("- Versicolor species fall between Setosa and Virginica in most features.\n")

# --------------------------------------------------------------

# 🎨 Task 3: Data Visualization

# --------------------------------------------------------------

print("=== Task 3: Creating Visualizations ===\n")

sns.set(style="whitegrid", palette="muted")

# (1) Line Chart - Trend of Sepal Lengths across samples

plt.figure(figsize=(8, 4))
plt.plot(df.index, df["sepal length (cm)"], color="blue", label="Sepal Length")
plt.title("Line Chart - Sepal Length Trend Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# (2) Bar Chart - Average Petal Length per Species

plt.figure(figsize=(7, 4))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.show()

# (3) Histogram - Distribution of Sepal Width

plt.figure(figsize=(7, 4))
plt.hist(df["sepal width (cm)"], bins=15, color="green", edgecolor="black")
plt.title("Histogram - Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# (4) Scatter Plot - Sepal Length vs Petal Length

plt.figure(figsize=(7, 4))
sns.scatterplot(
x="sepal length (cm)",
y="petal length (cm)",
hue="species",
data=df,
s=70
)
plt.title("Scatter Plot - Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()

# --------------------------------------------------------------

# 🧾 Findings

# --------------------------------------------------------------

print("=== Summary of Findings ===")
print("""
1️⃣ The Iris dataset contains 150 samples of three flower species.
2️⃣ No missing data was found, and all features are numeric.
3️⃣ The Virginica species generally has the largest measurements.
4️⃣ The line chart shows a stable variation in Sepal Length across samples.
5️⃣ The histogram reveals most sepal widths fall between 2.5 and 3.5 cm.
6️⃣ The scatter plot shows a positive correlation between Sepal and Petal Lengths.
""")
