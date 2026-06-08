import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("netflix_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# -----------------------------
# Data Cleaning
# -----------------------------

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
df["Duration"] = df["Duration"].fillna("Unknown")
df["Rating"] = df["Rating"].fillna("Not Rated")

# Check Duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

# -----------------------------
# Visualization 1
# Movies vs TV Shows
# -----------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Type")
plt.title("Movies vs TV Shows")
plt.show()

# -----------------------------
# Visualization 2
# Content by Country
# -----------------------------

plt.figure(figsize=(8,4))
df["Country"].value_counts().plot(kind="bar")
plt.title("Content by Country")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Visualization 3
# Release Year Distribution
# -----------------------------

plt.figure(figsize=(8,4))
sns.histplot(df["Release_Year"], bins=10)
plt.title("Release Year Distribution")
plt.show()

# -----------------------------
# Visualization 4
# Genre Distribution
# -----------------------------

plt.figure(figsize=(8,4))
df["Genre"].value_counts().plot(kind="bar")
plt.title("Genre Distribution")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Visualization 5
# Ratings Distribution
# -----------------------------

plt.figure(figsize=(6,6))
df["Rating"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Ratings Distribution")
plt.ylabel("")
plt.show()

# Save Cleaned Dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("\nProject Completed Successfully!")