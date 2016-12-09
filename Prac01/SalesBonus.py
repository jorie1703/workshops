__author__ = 'jc226070'

sales = 0
while sales <= 0:
    sales = float(input("Enter Sales: $"))
if sales < 1000:
    bonus = 10/100* sales
    print ("Your bonus is:", bonus)
elif (sales >=1000):
        bonus = 15/100* sales
        print("Your bonus is:",bonus)
