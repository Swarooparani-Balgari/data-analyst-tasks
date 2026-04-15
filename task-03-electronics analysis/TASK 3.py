
## Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 3.xlsx",sheet_name="Dataset")

## Revenue by Region

print("\nRevenue by Region\n",df.groupby("Region")["Revenue"].sum().sort_values(ascending=False))

## Revenue by ProductCategory

print("\nRevenue by ProductCategory\n",df.groupby("ProductCategory")["Revenue"].sum().sort_values(ascending=False))

## Average Shipping Days

print("\nAverage shipping days\n",df.groupby("Region")["ShippingDays"].mean())

## Visualizations

df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Quantity by Product")
plt.show()

df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).plot(kind='pie')
plt.title("Revenue by Product")
plt.show()

df.groupby("OrderDate")["Revenue"].sum().plot(kind='line')
plt.title("Revenue by OrderDate")
plt.show()
