#task1
print("Simple Calculator")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)

if y != 0:
    print("Division:", x / y)
else:
    print("Division: Not defined")  
