total = 0
f = open("num_list.txt", "r")
num = f.readline().strip()

while num:
    total += int(num)
    num = f.readline().strip()

print(str(total)[:10])
