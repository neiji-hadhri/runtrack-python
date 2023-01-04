def calcule(num1, operator, num2,):
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    elif operator == "%":
        result = num1 % num2
    return result


print(calcule(40, "+", 20,))
print(calcule(111, "-", 11,))
print(calcule(10, "*", 7,))
print(calcule(2, "/", 4,))
print(calcule(4, "%", 12,))