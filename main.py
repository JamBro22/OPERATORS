# declare common variables
# basic_salary = 1500
# bonus_rate = 200
# commission_rate = 0.02


# determine the bonus rate an employee will receive based on number of laptops sold
def determine_bonus_amount(bonus_rate, number_of_laptops):
    return bonus_rate * number_of_laptops


# determine the commission received by the employee based on the amount of laptops sold and their price
def determine_commission_amount(commission_rate, number_of_laptops, price_of_laptops):
    return commission_rate * number_of_laptops * price_of_laptops


# get the gross salary for the employee once the bonus and commission have been calculated
def determine_gross_salary(basic_salary, bonus_amount, commission_amount):
    return basic_salary + bonus_amount + commission_amount


# run from main
if __name__ == "__main__":
    # declare variables for use in functions
    current_basic_salary = 1500
    current_bonus_rate = 200
    current_commission_rate = 0.02

    bonus = determine_bonus_amount(current_basic_salary, 10)
    print(bonus)

    commission = determine_commission_amount(current_commission_rate, 10, 3000)
    print(commission)

    gross_salary = determine_gross_salary(current_basic_salary, bonus, commission)
    print(gross_salary)
