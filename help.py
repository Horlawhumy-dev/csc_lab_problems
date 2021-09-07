print("Python program that calculates decibels of two powers based on a range of number.")
import math
num = int(input("Enter the range of your choice: "))
def decibels(num):
    """Python program that calculates decibels of two powers based on a range of number."""
    db = 0
    p1 = 1
    p2 = 0
    count = 1

    if num > 0:
        while count < num+1:
            p2 = count
            div = p2 / p1
            db = 10 * math.log(div, 10) # decibel expression logic with base 10
            print(f"Decibels of {p2} is", round(db, 2),"db")
            count += 0.5
    else:
        print("Unsupported value of range!!")
        return

decibels(num)