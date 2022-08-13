import time
start = time.time()
limit = 2000000
answer = 0


'''generate_primes function creates a list every element is 1.
   Using Sieve of Eratosthenes, we eliminate composites and change their value
   to zero. 
'''
def generate_primes(limit):
    integers = list([1]*limit)
    for i in range(2, limit):
        for j in range(2, limit):
            if i*j < limit:
                integers[i*j] = 0
            else:
                break
    return integers


def get_primes():
    primes = list()
    num_list = generate_primes(limit)
    for i in range(2, len(num_list)):
        if num_list[i] == 1:
            primes.append(i)
    return primes

for n in get_primes():
    answer += n

end = time.time()

print(get_primes())
print(answer)
print(end - start, " seconds")
