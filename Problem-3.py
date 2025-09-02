import math

def generate_series(a):
    n = math.ceil(a / 2)
    return [2*i + 1 for i in range(n)]

a = 6
print(generate_series(a))
