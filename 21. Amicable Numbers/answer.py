import math
from collections import Counter
total = 0

#find the sum of the divisors of a number
def get_divisors(num):
    divisors = [1]

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num//i)

    divisors = Counter(divisors).keys()
    return sum(divisors)


for a in range(1, 10001):#find the answers of d(a) and d(b)
    num = get_divisors(a)
    b = get_divisors(num)
    
    if num > 10000 or num == b or num == a:#restrictions
        continue   
    
    if a == b:
        print(num, " : ", b)
        total += (a+b)

print(total//2)#calculating a pair twice so get the half value
