

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


monthlyrent = float(input("Monthly Rent (£):"))
nightlyrate = float(input("Nightly Airbnb rate (£): "))
occupancyrate = float(input("Expected occupancy (%): ")) / 100

electricity = float(input("Monthly electricity (£): "))
gas = float(input("Monthly gas (£): "))
water = float(input("Monthly water (£): "))
wifi = float(input("Monthly Wi-Fi (£): "))
insurance = float(input("Monthly insurance (£): "))
other = float(input("Other monthly costs (£): "))

avgstay = float(input("Average guest stay (nights): "))
cleaningcost = float(input("Cleaning cost per booking (£): "))

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

