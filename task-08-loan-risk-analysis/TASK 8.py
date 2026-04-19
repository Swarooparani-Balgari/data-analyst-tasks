## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 8.xlsx",sheet_name="Dataset")

## Calculate Columns

df["DefaultFlag"]=df["Defaulted"].map({"Yes":1,"No":0})
df["DebtToIncomeRatio"]=df["LoanAmount"]/df["Income"]

## DefaultFlag by EmploymentStatus

print("\nDefaultFlag by EmploymentStatus\n",df.groupby("EmploymentStatus")["DefaultFlag"].sum().sort_values(ascending=False))

## Avg CreditScore by Default rate

print("\nAvg CreditScore by Default rate\n",df.groupby("Defaulted")["CreditScore"].mean().sort_values(ascending=False))

## DebtToIncomeRatio

print("\nDebtToIncomeRatio\n",df["DebtToIncomeRatio"].mean())

## Visualizations

df.groupby("Defaulted")["CreditScore"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Avg Creditscore by Default rate")
plt.show()

df.groupby("RiskLevel")["Defaulted"].value_counts().sort_values(ascending=False).plot(kind='pie')
plt.title("DefaultFlag by RiskLevel")
plt.show()

df.groupby("EmploymentStatus")["LoanTerm_months"].mean().plot(kind='line')
plt.title("Avg Loanterm_months by EmploymentStatus")
plt.show()
      
