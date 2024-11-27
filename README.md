Financial Insights Dashboard

This is a Streamlit-based web app designed to calculate a financial score and provide recommendations based on your financial data.

Setup Instructions

Install the required libraries:
pip install streamlit pandas

Run the app:
streamlit run financial_dashboard.py

Model Logic

Inputs:
Income, 
Monthly Expenses, 
Savings, 
Loan Payments, 
Credit Card Spending, 
Financial Goals Met (Percentage).

Financial Score Calculation:

Savings: 40% weight (higher savings increases score), 
Expenses: 30% weight (higher expenses decrease score), 
Loans: 10% weight (higher loan payments decrease score), 
Credit Spending: 10% weight (higher credit card spending decreases score), 
Goals Met: 10% weight (meeting goals increases score).

Recommendations: Based on the inputs, the app provides recommendations like:

Increase savings if below 20% of income, 
Reduce expenses if over 50% of income, 
Lower loan payments if over 20% of income, 
Reduce credit card spending if over 10% of income, 
Work on meeting financial goals.

Features:

Calculate financial score (0 to 100).
Personalized recommendations to improve financial health.
