1️⃣ Import Libraries & Load Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

train_path = "/mnt/data/customer_churn_dataset-training-master.csv"
test_path = "/mnt/data/customer_churn_dataset-testing-master.csv"

df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

df = pd.concat([df_train, df_test], axis=0)
df.reset_index(drop=True, inplace=True)

df.head()



2️⃣ Data Cleaning & Preprocessing
df.info()

# Handle missing values
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_charges'].fillna(df['total_charges'].median(), inplace=True)

# Convert churn to binary
df['churn_flag'] = df['churn'].map({'Yes': 1, 'No': 0})

3️⃣ Exploratory Data Analysis (EDA)
Churn Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='churn', data=df)
plt.title("Churn Distribution")
plt.show()

Tenure vs Churn
plt.figure(figsize=(8,5))
sns.boxplot(x='churn', y='tenure', data=df)
plt.title("Tenure vs Churn")
plt.show()

Monthly Charges vs Churn
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='monthly_charges', hue='churn', bins=40, kde=True)
plt.title("Monthly Charges vs Churn")
plt.show()

4️⃣ Key Churn Drivers Analysis
churn_rate_contract = df.groupby('contract')['churn_flag'].mean().sort_values(ascending=False)
churn_rate_contract

plt.figure(figsize=(8,4))
churn_rate_contract.plot(kind='bar')
plt.ylabel("Churn Rate")
plt.title("Churn Rate by Contract Type")
plt.show()

5️⃣ Correlation Analysis
plt.figure(figsize=(10,6))
sns.heatmap(df[['tenure', 'monthly_charges', 'total_charges', 'churn_flag']].corr(),
            annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
