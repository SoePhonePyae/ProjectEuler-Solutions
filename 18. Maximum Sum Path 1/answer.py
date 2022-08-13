def get_sum_list(row_number):
    if row_number == 1:
        exit
    
    temp_list = pyramid_list[row_number-1]
    
    for j in range(len(temp_list)):
        a, b = int(pyramid_list[row_number][j]), int(pyramid_list[row_number][j+1])
        x = int(temp_list[j])

        pyramid_list[row_number-1][j] = x + max(a, b)


f = open("pyramid.txt", "r")
line = f.readline()
pyramid_list = list()
index = 0

while line:
    pyramid_list.append(line.split())
    line = f.readline()

f.close()

total = 0           

for i in range(len(pyramid_list)-1, 0, -1):
    get_sum_list(i)

print(pyramid_list[0])
