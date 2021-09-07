
def geometric_mean(arr):
    """Python program that calculates geometric mean of positive list numbers"""
    n = len(arr)
    result = 1
    for i in arr:
        result *= i
    return result ** (1/n)

geometric = geometric_mean([10, 5, 2, 5])
print(geometric)

