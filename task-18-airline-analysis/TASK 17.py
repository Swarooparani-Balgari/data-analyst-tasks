## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df = pd.read_excel("TASK 17.xlsx",sheet_name = "Dataset")

## CancellationFlag

df["Cancellation_Flag"]=df["Flight_Cancelled"].map({"Yes":1,"No":0})

## Avg Delay Minutes by Route Type

print("\nAvg Delay Minutes by Route Type\n",df.groupby("Route_Type")["Delay_Minutes"].mean().sort_values(ascending=False))

## Avg CancellationFlag by BaggageIssues

print("\nAvg Cancellation count by Baggage Issues\n",df.groupby("Baggage_Issues")["Cancellation_Flag"].mean().sort_values(ascending=False))

## Numeric Columns Only

print("\nNumeric Columns\n",df.corr(numeric_only=True))

## Visualizations

df.groupby("Route_Type")["Ticket_Price"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Avg Ticket Price by Route Type")
plt.show()

df.groupby("Delay_Category")["Passenger_Satisfaction"].mean().sort_values(ascending=False).plot(kind='pie')
plt.title("Avg PassengerSatisfaction by Delay Category")
plt.show()


                          
