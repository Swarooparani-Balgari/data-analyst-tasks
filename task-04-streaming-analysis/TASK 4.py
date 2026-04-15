## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Import Dataset

df=pd.read_excel("TASK 4.xlsx",sheet_name="Dataset")

## Revenue by SubscriptionType

print("\nRevenue by SubscriptionType\n",df.groupby("SubscriptionType")["MonthlyRevenue"].sum().sort_values(ascending=False))

## Engagement

print("\nAvg WatchHours by Country\n",df.groupby("Country")["WatchHours"].mean().sort_values(ascending=False))

## Churn Analysis

print("\nChurnRate\n",(df["Churned"]=="Yes").mean()*100)

## Visualizations

df.groupby("Country")["MonthlyRevenue"].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by Country")
plt.show()

df.groupby("JoinDate")["MonthlyRevenue"].mean().plot(kind='line')
plt.title("Revenue by JoinDate")
plt.xlabel("JoinDate")
plt.ylabel("MonthlyRevenue")
plt.show()
      
