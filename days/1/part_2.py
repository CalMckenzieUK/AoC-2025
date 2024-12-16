input_data = open('./days/1/input.txt').readlines()

list_1 = []
list_2 = []

for i in input_data:
    list_1.append(i.split(' ')[0])
    list_2.append(i.split(' ')[3].replace('\n', ''))

list_1 = sorted(list_1)
list_1 = [int(i) for i in list_1]
list_2 = sorted(list_2)
list_2 = [int(i) for i in list_2]

sim_list = []

for number in list_1:
    freq = 0
    for num2 in list_2:
        if number == num2:
            freq += 1
    sim_list.append(freq*number)

total = 0

for sim in sim_list:
    total += sim

print(total)

