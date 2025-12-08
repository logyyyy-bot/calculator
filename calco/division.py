num1 = int(input(""))
num2 = int(input(""))
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1// num2
print(divide(num1,num2))