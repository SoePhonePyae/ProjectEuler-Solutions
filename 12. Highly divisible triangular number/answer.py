import math
import time
from collections import Counter
start = time.time()

triangular_number = 1
index = 2

def prime_factor(num):
    prime_factors = list()
    while num%2 == 0:
        prime_factors.append(2)
        num //= 2

    for i in range(3, int(math.sqrt(num))+1, 2):
        while num%i == 0:
            prime_factors.append(i)
            num //= i

    if num > 1:
        prime_factors.append(num)

    return prime_factors


def count_divisors(num):
    divisors = 1
    values = Counter(prime_factor(num)).values()

    for i in values:
        divisors *= i+1

    return divisors
    

while count_divisors(triangular_number) < 500:
    triangular_number += index
    index += 1
    
end = time.time()
print(triangular_number)
print(end - start, " seconds")
