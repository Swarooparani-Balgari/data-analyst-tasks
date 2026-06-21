## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 16.xlsx",sheet_name="Dataset")

# CancellationFlag

df["CancellationFlag"]=df["Cancelled"].map({"Yes":1,"No":0})

# MonthlyFee by MembershipPlan

print("\nMonthlyFee by MembershipPlan\n",df.groupby("MembershipPlan")["MonthlyFee"].sum().sort_values(ascending=False))

## Avg Fitness rating by EngagementLevel

print("\nAvg FitnessRating by EngagementLevel\n",df.groupby("Engagement Level")["FitnessRating"].mean().sort_values(ascending=False))

## Numerical columns

print("\nNumerical Columns\n",df.corr(numeric_only=True))

## Visualizations

df.groupby("MembershipPlan")["CancellationFlag"].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Cancellation rate by MembershipPlan")
plt.show()

df.groupby("Member Segment")["GymVisits_PerMonth"].mean().sort_values(ascending=False).plot(kind='pie')
plt.title("Avg Gymvisits_permonth by Membersegment")
plt.show()


