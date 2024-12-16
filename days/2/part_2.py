input_data = open('./days/2/input.txt').readlines()

input_data = [i.replace('\n','').split(' ') for i in input_data]
int_data = []

for i in input_data:
    int_data.append([int(x) for x in i])

input_data = int_data

def all_ascending(list):
    last = 0
    for i in list:
        if i <= last:
            return False
        last = i
    return True

def all_descending(list):
    last = max(list)+1
    for i in list:
        if i >= last:
            return False
        last = i
    return True

def small_increments(list):
    for i in range(len(list)-1):
        if list[i] - list[i+1] in [1,2,3,-1,-2,-3]:
            continue
        else:
            return False
    return True 

def is_safe(report):
    if small_increments(report) is True:
        if all_ascending(report) is True:
            if all_descending(report) is False:
                return 1
        elif all_ascending(report) is False:
            if all_descending(report) is True:
                return 1
    return 0

safe_reports = 0
for report in input_data:
    start_state = report
    variations = [report]
    for i in range(len(report)):
        temp = start_state.copy()
        del temp[i]
        variations.append(temp)
    for variant in variations:
        if is_safe(variant) == 1:
            safe_reports += 1
            break

print(safe_reports)

    