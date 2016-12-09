__author__ = 'jc226070'
"""
Enter the no of item :
Enter the shipping cost for each different item :
Shipping cost = no of item*cost
if(SC>$100)
sc=10/100* sc
print("Discounted rate is:",sc)
elif (SC<=0)
 print ("invalid no of item")
 """
item = 1
while item > 0 :
    item = int(input("Enter the no of item: "))
    cost = float(input("Enter the Shipping Cost: "))
    Finalcost = item * cost;
    if Finalcost > 100:
        Finalcost = Finalcost * 0.9
    print("Your final cost is:",Finalcost)
