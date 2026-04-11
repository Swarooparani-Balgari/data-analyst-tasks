
## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 2.xlsx",sheet_name="Dataset")

## NetRevenue by City

print("\nNetRevenue by City\n",df.groupby("City")["NetRevenue"].sum().sort_values(ascending=False))

## Restaurant Performance

print("\nRevenue by Restaurant\n",df.groupby("Restaurant")["NetRevenue"].sum().sort_values(ascending=False))

## Delivery Performance

print("\nAvg_DeliveryTime by City\n",df.groupby("City")["DeliveryTime_min"].mean().sort_values(ascending=False))

## Rating Analysis

print("\nCustomerRating by Restaurant\n",df.groupby("Restaurant")["CustomerRating"].mean().sort_values(ascending=False))

## Visualizations

df.groupby("City")["NetRevenue"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Revenue by City")
plt.show()

df.groupby("PaymentMethod")["NetRevenue"].sum().sort_values(ascending=False).plot(kind="pie")
plt.title("Revenue by Payment Method")
plt.show()

df.groupby("OrderDate")["NetRevenue"].sum().plot(kind="line")
plt.title("Revenue by OrderDate")
plt.xlabel("OrderDate")
plt.ylabel("NetRevenue")
plt.show()







