# the sum of the first 9 numbers
n = 1
result = 0
while n < 10:
    if n % 2 == 1:
        result = result + n
    n = n + 1
print("sum of the first 9 numbers that are odd is", result)
