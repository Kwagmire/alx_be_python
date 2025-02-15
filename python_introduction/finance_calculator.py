monthly_in = int(input("Enter your monthly income: "))
monthly_out = int(input("Enter your total monthly expenses: "))

monthly_keep = monthly_in - monthly_out
rate = 0.05
annual_savings = int(monthly_keep * 12 + (monthly_keep * 12 * rate))

print(f"Your monthly savings are ${monthly_keep}.")
print(f"Pojected savings after one year, with interest, is: ${annual_savings:d}.")
