a, b = [int(input()) for _ in range(2)]
try:
    print(a / b)
except ZeroDivisionError:
    print("The Error!")
