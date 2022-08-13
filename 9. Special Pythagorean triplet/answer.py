import time
start = time.time()
limit = 1000
counter = 0
stop = False

for a in range(1, limit):
    for b in range(a+1, limit):
        for c in range(b+1, limit):
            counter += 1
            if a+b+c == 1000:
                if (a**2) + (b**2) == (c**2):
                    print(a, b, c)
                    stop = True
                    break
    if stop:
        break

end = time.time()
print(end - start, " seconds")
print(counter, " times")
