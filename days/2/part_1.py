input_data = open('./days/2/input.txt').readlines()

input_data = [i.replace('\n','').split(' ') for i in input_data]
int_data = []

for i in input_data:
    int_data.append([int(x) for x in i])

input_data = int_data
print(input_data)

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
    print('all small')
    return True 

def is_safe(list):
    safe_reports = 0
    for report in list:
        print(report)
        if all_ascending(report) is True:
            print('asc true')
            if all_descending(report) is False:
                print('desc false')
                if small_increments(report) is True:
                    print('small true')
                    safe_reports += 1

        elif all_ascending(report) is False:
            print('asc false')
            if all_descending(report) is True:
                print('desc true')
                if small_increments(report) is True:
                    print('small inc true')
                    safe_reports += 1
    print(safe_reports)

is_safe(input_data)

    