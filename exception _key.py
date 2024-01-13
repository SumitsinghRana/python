import random
print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
try:
    print("The sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)



print("This line is very important")
a=random.randint(1,10)
print(a+10)



