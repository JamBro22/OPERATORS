Basic_salary = 1500
Bonus_rate = 200
Commission_rate = 0.02
Numberoflaptops = int(input("Number of laptops:\n"))
Priceoflaptops = float(input("Price of laptops:\n"))
Bonus = (Bonus_rate*Numberoflaptops)
Commission = (Commission_rate*Numberoflaptops*Priceoflaptops)
Gross_salary = (Basic_salary+Bonus+Commission)
if (Priceoflaptops<Bonus_rate):
    print("Invalid")
else:
    print(Bonus)
    print(Commission)
    print(Gross_salary)