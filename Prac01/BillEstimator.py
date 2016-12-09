__author__ = 'jc226070'


"""
1.	Create an electricity bill estimator. Inputs should be:
    * price per kWh in cents,
    * daily use in kWh, and
    * number of days in the billing period.

"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariffPlan = int(input("Which tariff? <11 or 31>: "))
if tariffPlan == 11:
    pricePerKWH = TARIFF_11
elif tariffPlan == 31:
    pricePerKWH =TARIFF_31
else:
    print("Invalid input....")
dailyUsage = float(input("Daily Usage: "))
numDays = int(input("Number of days in billing period: "))
estimatedBill = pricePerKWH*dailyUsage*numDays
print("Estimated Bill: $ {:.2f}".format(estimatedBill))