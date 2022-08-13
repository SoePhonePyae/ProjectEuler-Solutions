import time
import math
start = time.time()
stop = False
counter = 0


def is_xor_odd(m, n):
    if m%2 != 0 and n%2 != 0:
        return False
    else:
        return True


def is_usable(m, n):
    if math.gcd(m, n) == 1:
        return is_xor_odd(m, n)


for n in range(1, 25):
    for m in range(n+1, 25):
        counter += 1
        if is_usable(m, n):
            a = (m**2) - (n**2)
            b = 2 * m * n
            c = (m**2) + (n**2)
            
            if 1000%(a+b+c) == 0:
                k = 1000/(a+b+c)
                print(k*a*k*b*k*c)
                stop = True
                break
    if stop:
        break

end = time.time()
print(end - start, " seconds")
print(counter, " times")
