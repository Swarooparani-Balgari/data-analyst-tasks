
## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 7.xlsx",sheet_name="Dataset")

df["AddedToCartFlag"]=df["AddedToCart"].map({"Yes":1,"No":0})
print("\nAddedToCartFlag\n",df["AddedToCartFlag"])

df["PurchasedFlag"]=df["Purchased"].map({"Yes":1,"No":0})
print("\nPurchasedFlag\n",df["PurchasedFlag"])     

conversion_rate=df["PurchasedFlag"].mean()
print("\nConversion_rate\n", conversion_rate)

print("\nPurchasedFlagbyTrafficSource\n",df.groupby("TrafficSource")["PurchasedFlag"].sum().sort_values(ascending=False))

print("\nPurchasedFlagbyDevice\n",df.groupby("Device")["PurchasedFlag"].sum().sort_values(ascending=False))

## Visualizations

df.groupby("Date")["TimeOnSite_sec"].mean().plot(kind='line')
plt.title("Avg_TimeOnsite_sec")
plt.show()
