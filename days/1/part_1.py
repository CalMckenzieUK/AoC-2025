input_data = open('./days/1/input.txt').readlines()

list_1 = []
list_2 = []

for i in input_data:
    list_1.append(i.split(' ')[0])
    list_2.append(i.split(' ')[3].replace('\n', ''))

list_1 = sorted(list_1)
list_2 = sorted(list_2)

diff_list = []

for i in range(len(list_1)):
    list_1_element = int(list_1[i])
    list_2_element = int(list_2[i])
    diff = max(list_1_element, list_2_element)-min(list_1_element, list_2_element)
    diff_list.append(diff)

total = 0 

for diff in diff_list:
    total += diff

print(total)

