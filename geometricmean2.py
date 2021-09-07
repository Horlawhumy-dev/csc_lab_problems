
def geometric_mean():
    """Python program that calculates geometric mean of nth number"""
    result = 0
    num = int(input("Enter a number: "))
    count = 1
    total = 1
    while num > 0:
        total *= num
        num = int(input("Enter the number: "))
        count += 1
    else:
        count -= 1
        result = pow(total, (1 / count))
    return round(result, 2)

print("The Geometric Mean of the positive numbers entered is: ", geometric_mean())
