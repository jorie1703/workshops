__author__ = 'jc226070'

in_file = open("Stock.txt", "r")
for line in in_file:
    line = line.strip()
    #print(line)
    split_line = line.split(',')
    print("Name:", split_line[0])
    print("Year:", split_line[1])
    print("Price: $ {:.2f}".format(float(split_line[2])))
in_file.close()


