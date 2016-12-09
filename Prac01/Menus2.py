__author__ = 'jc226070'



MENU="1. Show the even numbers from x to y\n" \
     "2. Show the odd numbers from x to y\n" \
     "3. Show the squares from x to y\n" \
     "4. Exit the program " \
     "\n>>>"
input1 = int(input("Enter X value: "))
input2 = int(input("Enter Y value: "))
choice = int(input(MENU))
while choice != 4:
    if choice == 1:
        even = ""
        for i in range(input1,input2):
            if i % 2 == 0:
                even += " " + format(i)
        print("Even Numbers between {} and {} are: {}".format(input1,input2,even))
    elif choice == 2:
        odd = ""
        for i in range(input1, input2):
            if i % 2 != 0:
                odd += " " + format(i)
        print("Odd Numbers between {} and {} are: {}".format(input1, input2, odd))
    elif choice == 3:
        squares = ""
        for i in range(input1, input2):
            squares += " " + format(i*i)
        print("Squares between {} and {} are: {}".format(input1, input2, squares))
    else:
        print("Invalid input..... Try again.")
    choice = int(input(MENU))