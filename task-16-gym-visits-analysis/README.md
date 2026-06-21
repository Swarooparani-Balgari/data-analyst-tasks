# Gym Membership & Fitness Engagement Analysis

## Objective
**Scenario** - Working for a fitness chain like Cult.fit or Gold's Gym.
The company is struggling with :
- Members cancelling subscriptions early
- Low gym visit frequency
- Poor engagement in premium membership plans

## Tools Used
- Excel
- SQL
- Python (Pandas, Matplotlib)
- Power BI

## Dataset 
- MemberID - An unique ID for each member in the gym
- MembershipPlan - What's the type of subscription plan
- MonthlyFee - How much was the fee
- GymVisits_PerMonth - How many times the member has visited the gym
- PersonalTrainingSessions - Whether the candidate has taken any personal training sessions from the trainer
- FitnessRating - Is the candidate fit enough
- MembershipDuration_month - How many months the member can avail the subscription plan
- Cancelled - Whether the candidate has cancelled the subscription plan

## Calculated columns 
- CancellationFlag - Converted cancelled into numericals
- EngagementLevel - Analyzed Engagement level based on their gym visits per month
- MemberSegment - Divided members into categories based on their membership duration months

## Analysis Performed 
- Calculated CancellationFlag, EngagementLevel and MemberSegment columns
- Analyzed monthlyfee based on their membership plan
- Evaluated cancellation rate by membership plan
- Categorized members into segments based on their gym visits per month
- Analyzed avg fitness rating by engagement level
- Evaluated avg personal training sessions by cancelled rate

## Business Insights
- Basic membership plan has generating the lowest revenue among all the plans
- Premium and Standard plans have lowest cancellation rate
- New customers are visiting the gym less often
- Engagement level directly proportional to fitness rating
- Customers who didn't even taken a single personal training session are cancelling more
- Premium & Standard plans have to push their adversity
- Company should first invest in member engagement programs
- Basic plan members with fewer than 6 monthly visits show the highest cancellation rates, indicating low engagement and lack of personalized support are major drivers of member churn

## Files Included
- TASK 16.xlsx - Dataset, Pivot tables and charts
- TASK 16.sql - SQL Queries
- TASK 16.py - Python analysis
- TASK 16.pbix - Power BI Dashboard
- Screenshot.png - Screenshot of dashboard

[Dashboard](Screenshot.png)
