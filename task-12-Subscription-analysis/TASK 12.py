import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 12.xlsx",sheet_name="Dataset")

df["Revenue"] = df["MonthlyFee"]*df["MonthsActive"]

df["UpgradeFlag"]=df["Upgraded"].map({"Yes":1,"No":0})

df["ChurnFlag"]=df["Churned"].map({"Yes":1,"No":0})

print("\nRevenue by PlanType\n",df.groupby("PlanType")["Revenue"].sum().sort_values(ascending=False))

print("UpgradeFlag by PlanType\n",df.groupby("PlanType")["UpgradeFlag"].sum().sort_values(ascending=False))

print("\nRevenue by Country\n",df.groupby("Country")["Revenue"].mean().sort_values(ascending=False))

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
pd.set_option("display.width",None)
pd.set_option("display.max_colwidth",None)

print("\nNumerical Columns\n",df.corr(numeric_only=True))

df.groupby("PlanType")["ChurnFlag"].sum().sort_values(ascending=False).plot(kind='pie')
plt.title("Churn rate by PlanType")
plt.show()

df.groupby("Device")["Revenue"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by Device")
plt.show()




      
