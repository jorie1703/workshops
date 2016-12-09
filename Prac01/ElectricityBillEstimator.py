__author__ = 'jc226070'



"""
1.	Create an electricity bill estimator. Inputs should be:
    * price per kWh in cents,
    * daily use in kWh, and
    * number of days in the billing period.

"""

pricePerKWH = float(input("Price Per KWH in cents: "))
dailyUsage = float(input("Daily Usage: "))
numDays = int(input("Number of days in billing period: "))
pricePerKWH /= 100
estimatedBill = pricePerKWH*dailyUsage*numDays
print("Estimated Bill: $ {}".format(estimatedBill))