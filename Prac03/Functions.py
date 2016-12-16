__author__ = 'jc226070'
"""
"""
text = "Merry Christmas"
print(text[:5] + text[6:12])





def inch_to_meter(inch):
   return inch * 0.0254

print(inch_to_meter(5))


y, x = 5, "Jay"
try:
    result = x * y
    print(result)
except ValueError:
    print("value")
except TypeError:
    print("type")
except:
    print("other")


tax_return =0
income = float(input("Income:"))
if income > 16000:
    tax = (income - 16000) *0.3
    print(tax)

def tax_return(income):
    if income <= 16000:
         return 0
    else:
        return(income - 16000*0.3)







