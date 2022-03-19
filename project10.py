def average(a, b):
    """The function finds the average of 2 numbers
    The function can only carry 2 values
    The function is built specifically for numerical values"""
    avg = (a+b)/2
    return avg
#function built

x = average(72, 54)
print(x)
print(average.__doc__)
#printing docstring