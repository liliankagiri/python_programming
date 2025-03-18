a = float(input("enter the 1st number:"))
b = float(input("enter the 2st number:"))
operator = input("enter an operator:'+','*','-','/':")

if operator == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif operator == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif operator == '*':
    result = a * b
    print(f"{a} * {b} = {result}")

elif operator == '/':
    result = a / b
    print(f"{a} / {b} = {result}")

else:
    print("invalid operator")