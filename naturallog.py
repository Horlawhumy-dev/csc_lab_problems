# importing math class
import math
def natural_log():
    """Python program that computes natural logarithm of numbers"""
    result = 0
    x = float(input("Please enter x: "))
    while x != "":
        if x < 1:
            val = 1/(1 - x)
            e = 2.718
            result = math.log(val, e)
            return round(result, 2)
        elif x > 1:
            val = -1 * (1/(1 - x))
            e = 2.718
            result = math.log(val, e)
            return round(result, 2)
        else:
            result = "Infinity"
            return result
    else:
       print("Please enter a value!")


print("The Natural Logarithm To Base 'e' is: ", natural_log())

