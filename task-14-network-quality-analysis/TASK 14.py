## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Import dataset

df=pd.read_excel("TASK 14.xlsx",sheet_name="Dataset")

## df["ChurnFlag"]=df["Churned"].map({"Yes":1,"No":0})

## ChurnFlag by PlanTYpe

print("\nChurnFlag by PlanTYpe\n",df.groupby("PlanType")["ChurnFlag"].mean().sort_values(ascending=False))

## CallDropComplaints by CustomerSegment

print("\nCallDropComplaints by CustomerSegment\n",df.groupby("CustomerSegment")["CallDropComplaints"].mean().sort_values(ascending=False))

## Avg MonthlyBill by PlanType

print("\nAvg MOnthlyBill by PlanType\n",df.groupby("PlanType")["MonthlyBill"].mean().sort_values(ascending=False)) 

## Visualizations

df.groupby("Churned")["NetworkRating"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Avg Networkrating by ChurnStatus")
plt.show()

df.groupby("CustomerSegment")["CallDropComplaints"].mean().sort_values(ascending=False).plot(kind='pie')
plt.title("Avg Complaints by CustomerSegment")
plt.show()

