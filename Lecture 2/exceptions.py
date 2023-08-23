import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Write a number")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Cant divide by 0")
    sys.exit(1)
print(result)