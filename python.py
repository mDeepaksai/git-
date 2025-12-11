a=float(input("enter a number: "))
b=float(input("enter a number: "))
op=input("enter an operator which u want to perform (+,-,*,/): ")
match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':  
        print(a*b)
    case '/':
        if b!=0:
            print(a/b)
        else:
            print("division by zero is not allowed")
    case _:
        print("invalid operator")