import string
alphabet_list = list(string.ascii_uppercase)
total = 0


def calculate_score(index_key):
    score = 0
    for i in name_dict[index_key]:
        score += alphabet_list.index(i)+1

    return score * index_key


#START COPY-PASTE
f = open("names.txt", "r")
line = f.readline()
name_list = list()
name_dict = dict()

while line:
    name_list = (line.replace('"', '')).split(',')
    name_list.sort()
    line = f.readline()

for i, j in enumerate(name_list):
    name_dict[i+1] = j

    
f.close()
#COPY-PASTE SECTION IS FINISHED HERE


for x in range(1, len(name_list)+1):
    total += calculate_score(x)

print(total)
