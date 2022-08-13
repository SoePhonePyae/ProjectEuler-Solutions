f = open("pyramid.txt", "r")
line = f.readline()
pyramid_list = list()
index = 0

while line:
    pyramid_list.append(line.split())
    line = f.readline()

f.close()

total = int(pyramid_list[0][0])

for i in range(1, len(pyramid_list)):
    if pyramid_list[i][0] > pyramid_list[i][1]:
        total += int(pyramid_list[i][0])
        print(pyramid_list[i][0])
        for j in range(i, len(pyramid_list)):
            del pyramid_list[j][-1]

    elif pyramid_list[i][0] < pyramid_list[i][1]:
        total += int(pyramid_list[i][1])
        print(pyramid_list[i][1])
        for k in range(i, len(pyramid_list)):
            del pyramid_list[k][0]

    else:
        print("This Pyramid is invalid!!")

print(total)
