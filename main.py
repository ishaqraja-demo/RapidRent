

def calc_revenue(nightlyrate, occupancyrate):
    return nightlyrate * occupancyrate * 365

def calc_annual_rent(monthlyrent):
    return monthlyrent * 12

def calc_annual_electricity(electricity):
    return electricity * 12

def calc_annual_gas(gas):
    return gas * 12

def calc_annual_water(water):
    return water * 12

def calc_annual_wifi(wifi):
    return wifi * 12

def calc_annual_insurance(insurance):
    return insurance * 12

def calc_annual_other(other):
    return other * 12

def calc_annual_cleaning(occupancyrate, avgstay, cleaningcost):
    return ((365*occupancyrate)/avgstay)*cleaningcost

def calc_total_annual_expenses(electricity,gas,water,wifi,insurance,other,occupancyrate, avgstay, cleaningcost, monthlyrent):
    total = (calc_annual_electricity(electricity)  + calc_annual_gas(gas)
             + calc_annual_water(water)
             + calc_annual_wifi(wifi)
             + calc_annual_insurance(insurance)
             + calc_annual_other(other)
             + calc_annual_cleaning(occupancyrate, avgstay, cleaningcost)
             + calc_annual_rent(monthlyrent))
    return total


def calc_annual_profit(nightlyrate, occupancyrate, electricity , gas,water,wifi,insurance,other, avgstay, cleaningcost, monthlyrent ):
    expenses = calc_total_annual_expenses (electricity, gas, water, wifi, insurance, other, occupancyrate, avgstay,
                                   cleaningcost, monthlyrent)

    revenue = calc_revenue(nightlyrate, occupancyrate)
    return revenue - expenses

def calc_monhtly_profit(nightlyrate, occupancyrate, electricity , gas,water,wifi,insurance,other, avgstay, cleaningcost, monthlyrent ):
    expenses = calc_total_annual_expenses(electricity, gas, water, wifi, insurance, other, occupancyrate, avgstay,
                                          cleaningcost, monthlyrent)

    revenue = calc_revenue(nightlyrate, occupancyrate)

    return (revenue - expenses)/12

def calc_break_even_occupancy(nightlyrate, electricity,gas,water,wifi,insurance,other, avgstay, cleaningcost, monthlyrent):
    total_wo_cleaning = (calc_annual_electricity(electricity) + calc_annual_gas(gas)
             + calc_annual_water(water)
             + calc_annual_wifi(wifi)
             + calc_annual_insurance(insurance)
             + calc_annual_other(other)
             + calc_annual_rent(monthlyrent))

    formula = (365*nightlyrate) - ((365*cleaningcost)/avgstay)
    return total_wo_cleaning / formula


def get_positive_number(prompt):
    flag = False
    while flag == False:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if number <= 0:
            print("Invalid")
        else:
            flag = True
    return number


monthlyrent = get_positive_number("Monthly Rent (£): ")
nightlyrate = get_positive_number("Nightly Airbnb rate (£): ")

flag = False
while flag == False:


    try:
        occupancyrate = float(input("Expected occupancy (%): "))
    except ValueError:
        print("Please enter a number.")
        continue

    if occupancyrate < 0 or occupancyrate > 100:
        print("Rate invalid. Enter something between 0-100.")
        flag = False
    else:
        occupancyrate = occupancyrate/100
        flag = True

electricity = get_positive_number("Monthly electricity (£): ")
gas = get_positive_number("Monthly gas (£): ")
water = get_positive_number("Monthly water (£): ")
wifi = get_positive_number("Monthly Wi-Fi (£): ")
insurance = get_positive_number("Monthly insurance (£): ")
other = get_positive_number("Other monthly costs (£): ")
avgstay = get_positive_number("Average guest stay (nights): ")
cleaningcost = get_positive_number("Cleaning cost per booking (£): ")

print('\n')
print('\n')
print("=" * 40)
print("     AIRBNB ARBITRAGE CALCULATOR")
print("=" * 40)
print('\n')
print("RESULTS")
print("-" * 40)

annual_revenue = calc_revenue(nightlyrate, occupancyrate)
print(f"Annual Revenue: £{annual_revenue:.2f}")

annual_expenses = calc_total_annual_expenses(electricity, gas, water, wifi, insurance, other, occupancyrate, avgstay, cleaningcost, monthlyrent)
print(f"Annual Expenses: £{annual_expenses:.2f}")

annual_profit = calc_annual_profit(nightlyrate, occupancyrate, electricity, gas, water, wifi, insurance, other, avgstay, cleaningcost, monthlyrent)
print(f"Annual Profit: £{annual_profit:.2f}")

monthlyprofit = calc_monhtly_profit(nightlyrate, occupancyrate, electricity, gas, water, wifi, insurance, other, avgstay, cleaningcost, monthlyrent)
print(f"Monthly Profit: £{monthlyprofit:.2f}")

break_even = calc_break_even_occupancy(nightlyrate, electricity, gas, water, wifi, insurance, other, avgstay, cleaningcost, monthlyrent)
print(f"Break Even Occupancy Rate: {break_even:.2%}")



