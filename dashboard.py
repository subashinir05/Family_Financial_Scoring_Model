import streamlit as st
import pandas as pd

def calculate_financial_score(row):
    savings_weight = 0.4
    expenses_weight = 0.3
    loans_weight = 0.1
    credit_weight = 0.1
    goals_weight = 0.1

    savings_ratio = row['Savings'] / row['Income'] if row['Income'] > 0 else 0
    expenses_ratio = row['Monthly Expenses'] / row['Income'] if row['Income'] > 0 else 0
    loans_ratio = row['Loan Payments'] / row['Income'] if row['Income'] > 0 else 0
    credit_spending = row['Credit Card Spending'] / row['Income'] if row['Income'] > 0 else 0
    goals_met = row['Financial Goals Met'] / 100

    score = (
        (savings_weight * savings_ratio) +
        (goals_weight * goals_met) - 
        (expenses_weight * expenses_ratio) - 
        (loans_weight * loans_ratio) - 
        (credit_weight * credit_spending)
    ) * 100

    return max(0, min(100, round(score,2)))

def generate_recommendations(data):
    recommendations = []

    if data['Savings'] / data['Income'] < 0.2:
        recommendations.append("Increase your savings to at least 20% of your income.")
    if data['Monthly Expenses'] / data['Income'] > 0.5:
        recommendations.append("Reduce your expenses to below 50% of your income.")
    if data['Loan Payments'] / data['Income'] > 0.2:
        recommendations.append("Consider reducing loan payments to below 20% of your income.")
    if data['Credit Card Spending'] / data['Income'] > 0.1:
        recommendations.append("Try to keep credit card spending below 10% of your income.")
    if data['Financial Goals Met'] < 100:
        recommendations.append("Work on achieving at least 80%-100% of your financial goals.")
    
    if not recommendations:
        recommendations.append("Your financial health looks great! Keep up the good work.")

    return recommendations

st.title("Financial Insights Dashboard")

income = st.number_input("Income", min_value=0)
monthly_expenses = st.number_input("Monthly Expenses", min_value=0)
savings = st.number_input("Savings", min_value=0)
loan_payments = st.number_input("Loan Payments", min_value=0)
credit_card_spending = st.number_input("Credit Card Spending", min_value=0)
financial_goals_met = st.slider("Financial Goals Met (%)", 0, 100)

if st.button("Calculate Financial Score"):
    input_data = {
        "Income": income,
        "Monthly Expenses": monthly_expenses,
        "Savings": savings,
        "Loan Payments": loan_payments,
        "Credit Card Spending": credit_card_spending,
        "Financial Goals Met": financial_goals_met
    }

    score = calculate_financial_score(pd.DataFrame([input_data]).iloc[0])

    recommendations = generate_recommendations(input_data)

    st.write(f"**Financial Score:** {score}")
    st.write("### Recommendations:")
    for rec in recommendations:
        st.write(f"- {rec}")
