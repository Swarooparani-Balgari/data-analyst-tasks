## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 15.xlsx",sheet_name="Dataset")

df["ReturnFlag"]=df["Returned"].map({"Yes":1,"No":0})

## ReturnFlag by ProductCategory

print("\nReturnFlag by ProductCategory\n",df.groupby("ProductCategory")["ReturnFlag"].mean().sort_values(ascending=False))

## CustomerRating by PaymentMethod

print("\nCustomerRating by PaymentMethod\n",df.groupby("PaymentMethod")["CustomerRating"].mean().sort_values(ascending=False))

## CustomerRating by DeliverySpeedCategory

print("\nCustomerRating by DeliverySpeedCategory\n",df.groupby("DeliverySpeedCategory")["CustomerRating"].mean().sort_values(ascending=False))

## DiscountPercent by Return Status

print("\nDiscountPercent by Returned\n",df.groupby("Returned")["DiscountPercent"].sum().sort_values(ascending=False))

## Numerical Columns

print("\nNumerical Columns\n",df.corr(numeric_only=True))


## Visualizations

## Bar Chart

df.groupby("ProductCategory")["FinalAmount"].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("FinalAmount by ProductCategory")
plt.show()

## Pie Chart

df.groupby("PaymentMethod")["DiscountPercent"].mean().sort_values(ascending=False).plot(kind='pie')
plt.title("Avg DiscountPercent by PaymentMethod")
plt.show()

