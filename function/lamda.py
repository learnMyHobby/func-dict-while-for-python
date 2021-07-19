# Python Program to add two numbers using a lambda function

a = lambda x, y: x + y

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

result = a(x, y)
print("Sum is:", result)