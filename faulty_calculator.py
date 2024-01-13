while True:
    op = input("What do you want to do among {*, /, +, -, 0 to exit}-> ")

    if op == '0':
        break  

    a = int(input("Enter the first number -> "))
    b = int(input("Enter the second number -> "))

    if op == '*':
        if a == 45 and b == 3:
            print("555")
        else:
            print("Multiplication of", a, "and", b, "is ->", a * b)
    elif op == '/':
        if a == 56 and b == 6:
            print("4")
        else:
            print("Division of", a, "and", b, "is ->", float(a / b))
    elif op == '+':
        if a == 56 and b == 9:
            print("77")
        else:
            print("Addition of", a, "and", b, "is ->", (a + b))
    elif op == '-':
        print("Subtraction of", a, "and", b, "is ->", (a - b))
    else:
        print("Wrong input")
