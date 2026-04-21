## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 10.xlsx",sheet_name="Dataset")

## Calcualted columns

df["LateFlag"]=df["LateDelivery"].map({"Yes":1,"No":0})
df["DeliverySpeed"]=df["Distance_km"]/df["DeliveryTime_min"]
df["TotalTime"]=df["PrepTime_min"]+df["DeliveryTime_min"]

## LateFlag count by Restaurant

print("\nAvg Count of LateFlag by Restaurant\n",df.groupby("Restaurant")["LateFlag"].mean().sort_values(ascending=False))

## Delivery Time by City

print("\nAvg Delivery Time by City\n",df.groupby("City")["DeliveryTime_min"].mean().sort_values(ascending=False))

## Show Numerical columns only

print(df.corr(numeric_only=True))

## Visualizations

df.groupby("LateDelivery")["DeliveryPartnerRating"].mean().sort_values(ascending=False).plot(kind='pie')
plt.title("Avg DeliveryPartnerRating by LateDelivery")
plt.show()

df.groupby("Restaurant")["PrepTime_min"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Avg PrepTime_min by Restaurant")
plt.show()

plt.scatter(df["Distance_km"],df["DeliveryTime_min"])
plt.title("DeliveryTime_min")
plt.xlabel("Distance_km")
plt.ylabel("DeliveryTime_min")
plt.grid(True)
plt.show()
      

