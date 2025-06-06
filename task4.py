def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Error : Division by zero is not possible"
def modulo(x,y):
    return x%y
print("\t\t\tBasic Calculator")
print("\t\t\t----------------")
while True:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    operator=input("Enter an operator(+,-,*,/,%):").strip()
    if operator=="+":
        result=add(num1,num2)
    elif operator=="-":
        result=subtract(num1,num2)
    elif operator=="*":
        result=multiply(num1,num2)
    elif operator=="/":
        result=divide(num1,num2)
    elif operator=="%":
        result=modulo(num1,num2)
    else:
        print("Error : Invalid operator")
    print(f"The result of {num1}{operator}{num2} is:{result}")
    continue_choice=input("want to perform another calculator? (yes to continue ,no to exit):").strip().lower()
    if continue_choice!="yes":
        print("Thank you........Exiting!!!")
        break