f = open("pyramid.txt", "r")
line = f.readline()
pyramid_list = list()
index = 0

while line:
    pyramid_list.append(line.split())
    line = f.readline()

f.close()
print(pyramid_list)
