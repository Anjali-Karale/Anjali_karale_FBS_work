#a. 1! + 2! + 3! + ... + n!

import math

n = int(input("Enter n: "))
total = sum(math.factorial(i) for i in range(1, n+1))
print("Sum of factorial series:", total)

#b. N + N^2 + N^3 + ... + N^N

N = int(input("Enter N: "))
total = sum(N**i for i in range(1, N+1))
print("Sum of series:", total)

#c. Geometric Series with Common Ratio 2

n = int(input("Enter number of terms: "))
total = sum(2**i for i in range(n))
print("Geometric series sum:", total)

#d. S = a + a^2/2 + a^3/3 + ... + a^10/10

a = int(input("Enter value of a: "))
S = sum((a**i)/i for i in range(1, 11))
print("Sum of series:", S)

#e. x - x^2/3 + x^3/5 - x^4/7 + ... (n terms)

x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

total = 0
sign = 1
for i in range(n):
    power = i + 1
    denominator = 2 * i + 1
    term = sign * (x ** power) / denominator
    total += term
    sign *= -1

print("Sum of series:", total)
