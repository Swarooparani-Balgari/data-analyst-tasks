# Bank Loan Risk Analysis

## Objective
**Scenario** - Working with a bank's risk team. They want to identify:
- Which customers are likely to default
- What factors influence loan default
- How to reduce bad loans

## Tools Used
- Excel
- SQL
- Python (Pandas, Matplotlib)
- Power BI

## Dataset
- CustomerID - An Unique id for each customer
- Age - Age of the customer
- Income - How much money the customer earns
- LoanAmount - The total money the bank lent to the customer
- Loan Term Months - In how many months the customer has to repay the loan
- Credit Score - A number that shows how trustworthy a customer is with money based on their past behaviour
- Employmentstatus - Whether the customer is employed, self-employed, or unemployed
- Defaulted - Whether the customer failed to repay the loan (Yes/No)

## Calculated Columns
- DefaultFlag - A numeric version of "Defaulted" - usually  if they defaulted, 0 if they didn't
- DebtToIncomeRatio - (LoanAmount/Income)- Shows how big the loan is compared to what the customer earns
- RiskLevel - A category assigned based on the CreditScore to summarize how risky lending to that customer is.

## Analysis Performed
- Calculated DefaultFlag, DebtToIncomeRatio,and Risk Level
- Analyzed default count by Employment Status
- Evaluated Avg CreditScore by Defaulted rate
- Categorized risk level by default count
- Compared avg loan term months by Employment Status
- Created an interactive dashboard for better understanding

## Business Insights
- Customers 2004 (Unemployed, CreditScore 600) and 2006 (Self-employed, Credit Score 640) are marked as High Risk.
- The dashboard shows defaulters have a noticeably lower avg credit score (~647) compared to non-defaulters. So, lower credit score is equal to higher chance of default
- Unemployed and self-employed customers are at high risk level due to low credit scores
- So, reject a loan if credit score < 620, reject if employment status = "Unemployed" and limit loan amount for Self-Employed customers also.

## Files Included
- TASK 8.xlsx - Dataset, Pivot tables and charts
- 
  
