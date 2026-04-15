import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 5.xlsx",sheet_name="Dataset")

df["StockStatus"].value_counts()

## Warehouse Performance

print("\nWareHouse Performance\n",df.groupby("Warehouse")["UnitsSold_Last30Days"].sum().sort_values(ascending=False))

## Product Performance

print("\nProductPerformance\n",df.groupby("Product")["UnitsSold_Last30Days"].sum().sort_values(ascending=False))

## Visualizations

df.groupby("Category")["UnitsSold_Last30Days"].sum().sort_values(ascending=False).plot(kind='pie')
plt.title("UnitsSold_Last30Days")
plt.show()

df.groupby("Product")["SupplierLeadTime_days"].mean().plot(kind='line')
plt.title("SupplierLeadTme_days by Product")
plt.show()
