## Import libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 1.xlsx",sheet_name="Dataset")

## Revenue by City
print("\nRevenue by City\n",df.groupby("City")["Fare/Revenue"].sum().sort_values(ascending=False))

## Average Ratings
print("\nAverage Ratings\n",df.groupby("VehicleType")["DriverRating"].mean().sort_values(ascending=False))

## Surge Analysis
print("\nSurgeMultiplier\n",df["SurgeMultiplier"].value_counts())

## Visualizations

df.groupby("VehicleType")["Fare/Revenue"].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by VehicleType")
plt.show()

df.groupby("TripDate")["Fare/Revenue"].sum().plot(kind='line')
plt.title("Revenue by TripDate")
plt.show()

df.groupby("PaymentMode")["Fare/Revenue"].sum().sort_values(ascending=False).plot(kind='pie')
plt.title("Revenue by PaymentMode")
plt.show()
