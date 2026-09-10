#renewed calculator
#using if operator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number?: "))
operator = input("What operator are you using?: ")
if operator == "+":
    tot=num1+num2
    print(tot)
elif operator == "-":
    tot=num1-num2
    print(tot)
elif operator == "*":
    tot=num1*num2
    print(tot)
elif operator == "/":
    tot=num1/num2
    print(tot)
elif operator == "%":
    tot=num1%num2
    print(tot)
else:
    print(f"{operator}: Syntax Error!!")