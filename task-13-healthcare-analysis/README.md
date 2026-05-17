# Healthcare Patient Wait Time & Service Efficiency Analysis

## Objective
**Scenario - ** Analyzing operations for a hospital (like Apollo Hospitals).Management is concerned about:
- Long patient wait times
- Uneven doctor workload
- Poor patient experience

## Tools Used
- Excel
- SQL
- Python (Pandas, Matplotlib)
- Power BI

## Dataset
- VisitID - An unique ID for each specific patient visit or appointment
- Department - The specific medical department where the visit took place
- DoctorID - An unique identifier for the physician who saw the patient
- PatientsPerHour - A workload metric indicating how many patients a doctor sees within an one-hour window
- AvgConsultTime (mins) - The avg number of minutes the doctor spent consulting with the patient during the visit
- WaitTime (mins) - The amount of time the patient spent waiting before actually seeing the doctor
- DayType - Categorizes the day of the visit whether weekday or weekend
- SatisfactionScore - A rating provided by the patient post-visit reflecting their experience and happiness with the service

## Calculated Columns 
- EfficiencyScore - It quantifies the relation between volume (how many people are seen) and duration (how long each appointment lasts)
- WaitCategory - Converted WaitTime into categories based on mins
- SatisfactionCategory - Converted SatisfactionScore into categories based on score

## Analysis Performed
- Calculated EfficiencyScore, WaitCategory and SatisfactionCategory columns
- Compared avg waittime by department
- Evaluated EfficiencyScore by department
- Analyzed avg PatientsPerHour by doctor ID
- Analyzed waiting time by daytype
- Created Visualizations for better understanding of the data

## Business Insights
- Orthopedics and Cardiology has the highest avg waiting time
- General department has the highest efficiency score
- DoctorID D3 had the highest visting of patients compared to other doctors
- Weekdays have the highest waittime than the weekends
- Longer wait time reduces satisfaction
- Orthopedics & Cardiology have to decrease their waiting time to improve their efficiency score
- Doctor D2 has to increase their number of visting the patients

## Files Included
- 
- 
