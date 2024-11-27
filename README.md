Dataset Loading:
I loaded the dataset from a CSV into a DataFrame and reviewed the first few rows to understand its structure.
Family-Level Aggregation:
I grouped the data by Family ID to calculate the sum of financial metrics like income, savings, expenses, and the average of Financial Goals Met (%).
Member-Level Aggregation:
Then, I grouped the data by Member ID to get the average income, total monthly expenses, and credit card spending per member.
Correlation Analysis:
I calculated and visualized the correlation matrix of key financial metrics (like income, savings, and expenses) using a heatmap.
Financial Scoring Model:
I created a function to calculate a financial score for each family based on savings ratio, credit card spending, and other factors, and added it to the family data.
Visualization:
I created several visualizations:
A pie chart for spending distribution by category.
A bar chart for family-wise financial scores.
A scatter plot for member-wise spending trends.
A scatter plot to analyze the correlation between income and expenses.
