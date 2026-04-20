# Customer Support Ticket Analysis

## Objective
**Scenario** - Working with support team. They want to understand:
- Which issues take the longest to resolve
- Which agent needs improvement
- How support team performance can improve

## Tools Used
- Excel
- SQL
- Python (Pandas, Matplotlib)
- Power BI

## Dataset
- TicketID - A person raised an issue and allocated some unique ID's by the team to resolve the issue
- Date - Date, when the issue was raised
- IssueType - What does the type of an issue which is raised by customers
- Priority - Whether the issue is highely prioritized or not
- ResolutionTime_hours - How many hours of time is taken to resolve the issue
- Agent - Who is trying to resolve the issue from the customer support team
- CustomerSatisfaction - Whether the customer is satisfied with the resolvation or not
- Escalated - Whether an issue has been transferred to higher authorities in the organization

## Calculated Columns
- EscalationFlag - Escalated is converted into if Yes = 1, and No = 0
- SatisfactionLevel - Customer satisfaction level has been converted to Low, Medium, High levels
- ResolutionSpeed - ResolutionTime_hours has been converted to performance like Fast, Moderate and Slow.

## Analysis Performed
- Calcualted EscalationFlag, SatisfactionLevel, and ResolutionSpeed columns
- Evaluated resolution type by issue type
- Analyzed escalation rate by issue type
- Compared satisfaction Levels
- Analyzed best performing agent in the customer support team
- Distributed ticket count by priority levels

## Business Insights
- Bug Reports and Payment issues are taking more time to resolve
- Agent A2 is performing best, Agents A1 and A3 needs improvement
- Customers are not highly satisfied with the resolvation
- Bug Report and Payment issues has been escalated more than the other issues
- High priority issues are raising more
- Bug Report and Payment issues has to be resolved quickly for better improvement
- A1 and A3 agents needs more training regarding ticket resolvation methods

## Files Included
- TASK 9.xlsx - Dataset, Pivot tables and charts
- TASK 9.sql - SQL Queries
