## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Import Dataset

df=pd.read_excel("TASK 6.xlsx",sheet_name="Dataset")

## Attrition by Department

print("\nAttritionFlag by Department\n",df.groupby("Department")["AttritionFlag"].sum().sort_values(ascending=False))

## Avg_Salary by Attrition

print("\nAvg_Salary by Attrition\n",df.groupby("Attrition")["Salary"].mean().sort_values(ascending=False))

## Avg_Salary by Department

print("\nAvg_Salary by Department\n",df.groupby("Department")["Salary"].mean().sort_values(ascending=False))

## Visualizations

df.groupby("JobRole")["Salary"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Avg_Salary by JobRole")
plt.show()

df.groupby("Department")["AttritionFlag"].mean().sort_values(ascending=False).plot(kind='pie')
plt.title("Attrition count by Department")
plt.show()
