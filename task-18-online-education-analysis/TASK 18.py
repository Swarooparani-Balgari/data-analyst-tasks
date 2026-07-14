
## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 18.xlsx",sheet_name="Dataset")

## CancellationFlag

df["CompletionFlag"]=df["CourseCompleted"].map({"Yes": 1, "No": 0})

## Avg CompletionFlag by CourseCategory

print("\nAvg CompletionFlag by CourseCategory\n",df.groupby("CourseCategory")["CompletionFlag"].mean().sort_values(ascending=False))

## Avg StudentRating by EngagementLevel

print("\nAvg StudentRating by EngagementLevel\n",df.groupby("EngagementLevel")["StudentRating"].mean().sort_values(ascending=False))

## Numerical Columns

print("\nNumerical Columns\n",df.corr(numeric_only=True))

## Visualizations

df.groupby("CourseCategory")["RefundFlag"].sum().sort_values(ascending=False).plot(kind='pie')
plt.title("Refund Rate by CourseCategory")
plt.show()

df.groupby("CourseCategory")["CoursePrice"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Avg CoursePrice by CourseCategory")
plt.show()

