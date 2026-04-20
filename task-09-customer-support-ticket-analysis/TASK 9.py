## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 9.xlsx",sheet_name="Dataset")

## Escalation rate

df["EscalationFlag"]=df["Escalated"].map({"Yes":1,"No":0})

## Avg ResolutionTime by IssueType

print("\nAvg Resolutiontime by IssueType\n",df.groupby("IssueType")["ResolutionTime_hours"].mean().sort_values(ascending=False))

## Avg CustomerRating by Agent

print("\nAvg CustomerRating by Agent\n",df.groupby("Agent")["CustomerSatisfaction"].mean().sort_values(ascending=False))

print("\nEscalationFlag\n",df["EscalationFlag"].mean())

## Visualizations

df.groupby("IssueType")["EscalationFlag"].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("EscalationFlag by IssueType")
plt.show()

df.groupby("Priority")["TicketID"].count().sort_values(ascending=False).plot(kind='pie')
plt.title("TicketCount by Priority")
plt.show()
