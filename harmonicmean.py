print("Python program that calculates harmonic mean of nth number")
def harmonic_mean():
    """Python program that calculates harmonic mean of nth number"""
    result = 0
    num = int(input("Enter the number: "))
    count = 0
    total = 0
    divider = 0
    while num != 0:
        divider = 1 / num
        total += divider
        num = int(input("Enter the number: "))
        count += 1
    else:
        result = count / total
    return round(result, 2)
print("The Harmonic Mean of the positive numbers entered is: ", harmonic_mean())
