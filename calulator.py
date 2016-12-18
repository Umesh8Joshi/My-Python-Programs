""" Here is a simple program that will be used for simple calculator
    This one will allow you to do addition,subtraction,multiplication,
    and other things and conversion also with Interest calculator """
#here is the main function to choose which function will execute
#below function is for simple calculations
def simple_calc():
    print("Enter Number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter your choice")
    print("1- Addition \n 2-Subtraction \n 3-Muiltiplication \n 4- Division")
    print("Choice: ")
    ch = int(input())
    if ch == 1:
        sum = num1 + num2
        print(sum)
    elif ch == 2:
        sub = num1 - num2
        print(sub)
    elif ch == 3:
        mul = num1*num2
        print(mul)
    elif ch == 4:
        div = num1 / num2
        print(div)
    else:
        print("Wrong Choice")
#here is the code conversion function
def convert():
    print("Enter choice\n1-Decimal to Binary\n2-Decimal to octal\n3-Decimal to Hex\nChoice: ")
    ch1 = int(input())
    if ch1 == 1:
        d2b()
    elif ch1 == 2:
        deo()
    elif ch2 == 3:
        doh()
#subparts of above functions
#for decimal to binary conversion
def Interest():
    print("Enter your Amount in INR: ")
    am = int(input())
    print("Enter your interest rate: ")
    it = int(input())
    print("Enter Duration: ")
    du = int(input())
    bal = (am*it*du)/100
    print(bal)
print("Here are your options")
print("1- Simple Calculator")
print("2- Converter")
print("3- Interest Calculator")
opt = int(input())
if opt == 1:
    simple_calc()
elif opt == 2:
    convert()
elif opt == 3:
    Interest()
else:
    print("Wrong Choice")
