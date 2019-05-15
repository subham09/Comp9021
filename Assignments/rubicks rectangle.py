import sys
from collections import deque
try:
    number = str(input('Input final configuration: '))
    str_number = number.replace(" ", "")
    if len(str_number.replace(" ", "")) != 8:
        raise ValueError
    elif '0' in str(number):
        raise ValueError
    for i in range(len(str_number)):
        counter = str_number.count(str_number[i])
        if counter>1:
            raise ValueError
except ValueError:
    print('Incorrect configuration, giving up...')
    sys.exit()
int_number = int(str_number)
initial_state = [1,2,3,4,5,6,7,8]
def row_exchange(sequence):
    return_value = sequence[::-1]
    return return_value
def right_shift(sequence):
    a = []
    a.append(sequence[3])
    a.append(sequence[0])
    a.append(sequence[1])
    a.append(sequence[2])
    a.append(sequence[5])
    a.append(sequence[6])
    a.append(sequence[7])
    a.append(sequence[4])
    return a
def middle_clockwise(sequence):
    a = []
    a.append(sequence[0])
    a.append(sequence[6])
    a.append(sequence[1])
    a.append(sequence[3])
    a.append(sequence[4])
    a.append(sequence[2])
    a.append(sequence[5])
    a.append(sequence[7])
    return a
def give_int(sequence):
    num = ''
    for items in sequence:
        num = num + str(items)
        int_num = int(num)
    return int_num

myqueue = deque()
myqueue.append([initial_state,0])
seen = {1}
flag = 0
level = 0
counter=0
while len(myqueue) > 0 and flag == 0:
    if give_int(initial_state) == int_number:
        flag = 1
        level = 0
        break
    else:
        seq = myqueue.popleft()
        sequence = seq[0]
        level = seq[1]
        if give_int(sequence) == int_number:
            break
        else:
            if give_int(sequence) not in seen:
                opr1 = row_exchange(sequence)
                opr2 = right_shift(sequence)
                opr3 = middle_clockwise(sequence)
                seen.add(give_int(seq[0]))
                level += 1
                if give_int(opr1) == int_number or give_int(opr2) == int_number or give_int(opr2) == int_number:
                    flag = 1
                    break
                else:
                    myqueue.append([opr1,level])
                    myqueue.append([opr2,level])
                    myqueue.append([opr3,level])
            else:
                #myqueue.popleft()
                #print('i m in continue')
                counter+=1
                continue
if level == 0:
	print(f'{level} step is needed to reach the final configuration.')
else:
	print(f'{level} steps are needed to reach the final configuration.')
#print(counter)
