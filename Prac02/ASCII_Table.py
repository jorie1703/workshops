__author__ = 'jc226070'


lower = 33
upper = 100
print("ASCII Code   CHAR")
print("----------   ----")
for i in range(lower, upper):
    print("{:>6} {:>8}".format(i, chr(i)))




