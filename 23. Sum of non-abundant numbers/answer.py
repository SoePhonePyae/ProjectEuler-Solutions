import math
import time
from collections import Counter
start = time.time()
abundant_list = list()
num_range = range(1, 28124)
all_int = list(n for n in num_range)

#find the sum of the divisors of a number
def get_divisors(num):
    divisors = [1]

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num//i)

    divisors = Counter(divisors).keys()
    return sum(divisors)


for i in num_range:
    if i < get_divisors(i):
        abundant_list.append(i)

print(len(abundant_list))
