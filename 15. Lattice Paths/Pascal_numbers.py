pascal_list = list()
num = 40

for i in range(num):
    #pascal_list[0] = 1
    tmp = list()
    tmp = pascal_list.copy()

    if i > 1:
        for j in range(1, i):
            pascal_list[j] = tmp[j] + tmp[j-1]

    pascal_list.append(1)

    print(pascal_list)
