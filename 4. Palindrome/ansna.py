import time
import math
start = time.time()

palindrome_list = list()


def is_palindrome(num):
    str_num = str(num)
    flag = True

    for j in range(math.ceil(len(str_num)/2)):
        if str_num[j] is not str_num[-j-1]:
            flag = False
            break

    return flag

for i in range(10000, 998001):
    if is_palindrome(i):
        palindrome_list.append(i)

breaked = False
for k in range(100):
    answer = palindrome_list[-k-1]
    for l in range(100, 1000):
        if answer%l == 0 and answer/l < 1000:
            print(answer)
            breaked = True
            break
    if breaked:
        break

end = time.time()
print(end-start, "seconds")
