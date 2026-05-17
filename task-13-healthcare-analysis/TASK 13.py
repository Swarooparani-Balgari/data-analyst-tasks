import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("TASK 13.xlsx",sheet_name="Dataset")

df["EfficiencyScore"]=df["PatientsPerHour"]/df["AvgConsultTime(mins)"]

print("\nAvg WaitTime by Department\n",df.groupby("Department")["WaitTime(mins)"].mean().sort_values(ascending=False))

print("\nAvg Patients Visiting by DoctorID\n",df.groupby("DoctorID")["PatientsPerHour"].mean().sort_values(ascending=False))

print("\nNumeric_Columns\n",df.corr(numeric_only=True))

df.groupby("Department")["EfficiencyScore"].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("EfficiencyScore by Department")
plt.show()

df.groupby("DoctorID")["PatientsPerHour"].sum().sort_values(ascending=False).plot(kind='pie')
plt.title("PatientsPerHour by DoctorID")
plt.show()
