print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

choice = int(input("Enter your choice:"))

if(choice>=1 and choice<=4):
    print("Enter two number:")
    number1 = int(input("First number : "))
    number2 = int(input("Second number : "))

if choice == 1:
    result = number1+number2
    print("Sum of numbers is: ",result)
elif choice == 2:
    result = number1-number2
    print("Difference of numbers is: ",result)
elif choice == 3:
    result = number1*number2
    print("Multiplication of numbers is: ",result)
elif choice == 4:
    result = number1/number2
    print("Division of numbers is: ",result)
elif choice == 5:
    exit()
else :
    print("Wrong input..!!")
