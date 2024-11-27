from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

def calculate_financial_score(row):
    savings_weight = 0.3
    expenses_weight = 0.2
    loans_weight = 0.2
    credit_weight = 0.15
    goals_weight = 0.15
    
    savings_ratio = row['Savings'] / row['Income'] if row['Income'] > 0 else 0
    expenses_ratio = row['Monthly Expenses'] / row['Income'] if row['Income'] > 0 else 0
    loans_ratio = row['Loan Payments'] / row['Income'] if row['Income'] > 0 else 0
    credit_spending = row['Credit Card Spending'] / row['Income'] if row['Income'] > 0 else 0
    goals_met = row['Financial Goals Met (%)'] / 100

    score = (
        (savings_weight * min(1, savings_ratio)) -
        (expenses_weight * min(1, expenses_ratio)) -
        (loans_weight * min(1, loans_ratio)) -
        (credit_weight * min(1, credit_spending)) +
        (goals_weight * goals_met)
    ) * 100

    return max(0, min(100, score))

@app.route('/get_score', methods=['POST'])
def get_financial_score():
    input_data = request.json
    input_df = pd.DataFrame(input_data)

    input_df['Financial Score'] = input_df.apply(calculate_financial_score, axis=1)
    
    insights = {}
    for _, row in input_df.iterrows():
        family_id = row['Family ID']
        family_insights = []

        if row['Savings'] / row['Income'] < 0.2:
            family_insights.append("Savings are below recommended levels, which affects your score.")
        if row['Financial Goals Met (%)'] < 100:
            family_insights.append("Financial goals are not being met.")

        if family_insights:
            insights[family_id] = family_insights

    insights_list = []
    for family_id, family_insights in insights.items():
        for insight in family_insights:
            insights_list.append(f"Family {family_id}: {insight}")

    response = {
        "Scores": input_df[['Family ID', 'Financial Score']].to_dict(orient='records'),
        "Insights": insights_list
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
