monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
rate = 0.05
annual_savings = int(monthly_savings * 12 + (monthly_savings * 12 * rate))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Pojected savings after one year, with interest, is: ${annual_savings:d}.")
