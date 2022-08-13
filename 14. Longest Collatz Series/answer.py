import time
start = time.time()


number = 0
longest_length = 0


def collatzSequence(num):
    length = 1

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (3*num)+1
        length += 1

    return length


for i in range(1, 1000001):
    sequence_length = collatzSequence(i)
    if sequence_length > longest_length:
        number = i
        longest_length = sequence_length

end = time.time()
print("Took ", end-start, " seconds")
print(number)
