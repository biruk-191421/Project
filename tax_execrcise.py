def tax_determiner(income):
    if income <= 2000:
        tax_rate = 0
    elif income <= 4000:
        tax_rate = 0.15
    elif income <= 7000:
        tax_rate = 0.20
    elif income <= 10000:
        tax_rate = 0.25
    elif income <= 14000:
        tax_rate = 0.30
    else:
        tax_rate = 0.35

    tax = income * tax_rate
    net_income = income - tax
    return tax, net_income
    

income = float(input("Enter your income: "))

if income < 0:
    print("Income cannot be negative")
else:
    tax, net_income = tax_determiner(income)
    print("Tax on an income of", income, "is:", tax)
    print("Net income after tax is:", net_income)

