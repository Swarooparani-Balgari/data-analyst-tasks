
## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

## Load Dataset

df=pd.read_excel("TASK 11.xlsx",sheet_name="Dataset")

## Calcualted Columns

df["CancelFlag"]==df["Cancelled"].map({"Yes":1,"No":0})

df["RevenuePotential"]==df["StayDuration"]*df["AvgDailyRate"]

## CancelFlag by BookingChannel

print("\nCancelFlag by BookingChannel\n",df.groupby("BookingChannel")["CancelFlag"].mean().sort_values(ascending=False))

## LeadTimeDays by HotelType

print("\nLeadTimeDays by HotelType\n",df.groupby("HotelType")["LeadTimeDays"].mean().sort_values(ascending=False))

## To see all the numerical colums

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
pd.set_option("display.width",None)
pd.set_option("display.max_colwidth",None)

print("\nNumerical_Columns\n",df.corr(numeric_only=True))

## Visualiations

df.groupby("HotelType")["CancelFlag"].sum().sort_values(ascending=False).plot(kind='pie')
plt.title("Cancellation rate by HotelType")
plt.show()

df.groupby("BookingChannel")["RevenuePotential"].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by BookingChannel")
plt.show()
