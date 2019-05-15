def move_right(no_of_moves, top_element, front_element, right_element, left_element, bottom_element, back_element):
    if no_of_moves % 4 == 1:
        new_top_element = left_element
        new_front_element = front_element
        new_right_element = top_element
        new_left_element = bottom_element
        new_back_element = back_element
        new_bottom_element = right_element
    if no_of_moves % 4 == 2:
        new_top_element = back_element
        new_front_element = front_element
        new_right_element = left_element
        new_left_element = right_element
        new_back_element = back_element
        new_bottom_element = top_element
    if no_of_moves % 4 == 3:
        new_top_element = right_element
        new_front_element = front_element
        new_right_element = bottom_element
        new_left_element = top_element
        new_back_element = back_element
        new_bottom_element = left_element
    if no_of_moves % 4 == 0:
        new_top_element = top_element
        new_front_element = front_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = back_element
        new_bottom_element = bottom_element
    return (new_top_element, new_front_element, new_right_element, new_left_element, new_back_element, new_bottom_element)
def move_down(no_of_moves, top_element, front_element, right_element, left_element, bottom_element, back_element):
    if no_of_moves % 4 == 1:
        new_top_element = back_element
        new_front_element = top_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = bottom_element
        new_bottom_element = front_element
    if no_of_moves % 4 == 2:
        new_top_element = bottom_element
        new_front_element = back_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = front_element
        new_bottom_element = top_element
    if no_of_moves % 4 == 3:
        new_top_element = front_element
        new_front_element = bottom_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = top_element
        new_bottom_element = back_element
    if no_of_moves % 4 == 0:
        new_top_element = top_element
        new_front_element = front_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = back_element
        new_bottom_element = bottom_element
    return (new_top_element, new_front_element, new_right_element, new_left_element, new_back_element, new_bottom_element)
def move_up(no_of_moves, top_element, front_element, right_element, left_element, bottom_element, back_element):
    if no_of_moves % 4 == 1:
        new_top_element = front_element
        new_front_element = bottom_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = top_element
        new_bottom_element = back_element
    if no_of_moves % 4 == 2:
        new_top_element = bottom_element
        new_front_element = back_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = front_element
        new_bottom_element = top_element
    if no_of_moves % 4 == 3:
        new_top_element = back_element
        new_front_element = top_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = bottom_element
        new_bottom_element = front_element
    if no_of_moves % 4 == 0:
        new_top_element = top_element
        new_front_element = front_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = back_element
        new_bottom_element = bottom_element
    return (new_top_element, new_front_element, new_right_element, new_left_element, new_back_element, new_bottom_element)
def move_left(no_of_moves, top_element, front_element, right_element, left_element, bottom_element, back_element):
    if no_of_moves % 4 == 1:
        new_top_element = right_element
        new_front_element = front_element
        new_right_element = bottom_element
        new_left_element = top_element
        new_back_element = back_element
        new_bottom_element = left_element
    if no_of_moves % 4 == 2:
        new_top_element = bottom_element
        new_front_element = front_element
        new_right_element = left_element
        new_left_element = right_element
        new_back_element = back_element
        new_bottom_element = top_element
    if no_of_moves % 4 == 3:
        new_top_element = left_element
        new_front_element = front_element
        new_right_element = top_element
        new_left_element = bottom_element
        new_back_element = back_element
        new_bottom_element = right_element
    if no_of_moves % 4 == 0:
        new_top_element = top_element
        new_front_element = front_element
        new_right_element = right_element
        new_left_element = left_element
        new_back_element = back_element
        new_bottom_element = bottom_element
    return (new_top_element, new_front_element, new_right_element, new_left_element, new_back_element, new_bottom_element)

import sys
while True:
	try:
		number = int(input("Enter the desired goal cell number: "))
		if number<1:
			raise ValueError
	except ValueError:
		print('Incorrect value, try again')
		continue
	break

sum = 0
sum2 = 1
steps = 0
Flag1 = False
Flag2 = False
end_point1 = None
end_point2 = None
list_of_end_points2 = []
list_of_end_points1 = []
list_of_turns1 = []
list_of_turns2 = []
list_of_numbers_of_directions = []
list_of_directions = []
top_element = 3
right_element = 1
front_element = 2
bottom_element = 4
left_element = 6
back_element = 5
loop_size = int(number)
for i in range (1,loop_size):
    sum = sum + i
    if sum >= number:
        end_point1 = i
        Flag1 = True
        break
    sum = sum + i
    if sum>=number:
        end_point2 = i
        Flag2 = True
        break
list_of_turns1.append(1)
list_of_turns2.append(1)
if end_point2 != None:
    for i in range (1,end_point2 + 1):
        list_of_end_points2.append(i)
        list_of_end_points2.append(i)
    for items in list_of_end_points2:
        sum2 = sum2 + items
        list_of_turns2.append(sum2)
    steps = number - list_of_turns2[len(list_of_turns2)-2]
    if number not in list_of_turns2:
        for i in range (0,len(list_of_end_points2)):
            if i % 4 == 0:
                list_of_directions.append("R")
            elif i % 4 == 1:
                list_of_directions.append("D")
            elif i % 4 == 2:
                list_of_directions.append("L")
            elif i % 4 == 3:
                list_of_directions.append("U")
        list_of_end_points2.pop(len(list_of_end_points2)-1)
        list_of_end_points2.append(steps)
        #list_of_directions.pop(len(list_of_directions)-1)
    else:
        for i in range (0,len(list_of_turns2)-2):
            if i % 4 == 0:
                list_of_directions.append("R")
            elif i % 4 == 1:
                list_of_directions.append("D")
            elif i % 4 == 2:
                list_of_directions.append("L")
            elif i % 4 == 3:
                list_of_directions.append("U")
        list_of_end_points2.pop(len(list_of_end_points2)-1)

if end_point1 != None:
    for i in range (1,end_point1 + 1):
        list_of_end_points1.append(i)
        if i != end_point1:
            list_of_end_points1.append(i)
    for items in list_of_end_points1:
        sum2 = sum2 + items
        list_of_turns1.append(sum2)
    steps = number - list_of_turns1[len(list_of_turns1)-2]
    if number not in list_of_turns1:
        for i in range (0,len(list_of_end_points1)):
            if i % 4 == 0:
                list_of_directions.append("R")
            elif i % 4 == 1:
                list_of_directions.append("D")
            elif i % 4 == 2:
                list_of_directions.append("L")
            elif i % 4 == 3:
                list_of_directions.append("U")
        list_of_end_points1.pop(len(list_of_end_points1)-1)
        list_of_end_points1.append(steps)
    else:
        for i in range (0,len(list_of_turns1)-2):
            if i % 4 == 0:
                list_of_directions.append("R")
            elif i % 4 == 1:
                list_of_directions.append("D")
            elif i % 4 == 2:
                list_of_directions.append("L")
            elif i % 4 == 3:
                list_of_directions.append("U")
        list_of_end_points1.pop(len(list_of_end_points1)-1)

if len(list_of_end_points1)==0:
    for i in range(0, len(list_of_end_points2)):
        for j in range(i, len(list_of_directions)):
            if list_of_directions[j] == "R":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_right(list_of_end_points2[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break
            if list_of_directions[j] == "D":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_down(list_of_end_points2[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break
            if list_of_directions[j] == "L":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_left(list_of_end_points2[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break
            if list_of_directions[j] == "U":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_up(list_of_end_points2[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break

if len(list_of_end_points2)==0:
    for i in range(0, len(list_of_end_points1)):
        for j in range(i, len(list_of_directions)):
            if list_of_directions[j] == "R":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_right(list_of_end_points1[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break
            if list_of_directions[j] == "D":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_down(list_of_end_points1[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break
            if list_of_directions[j] == "L":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_left(list_of_end_points1[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break
            if list_of_directions[j] == "U":
                top_element, front_element, right_element, left_element, back_element, bottom_element = move_up(list_of_end_points1[i],top_element,front_element,right_element,left_element,bottom_element,back_element)
                break

#print('perfect top',top_element)



#print("number---->", number)
#print("sum---->", sum)
#rint("endpoint1---->", end_point1)
#print("endpoint2---->", end_point2)
#print("list_of_endpoints2---->", list_of_end_points2)
#print("list_of_endpoints1---->", list_of_end_points1)
#print("list_of_turns1---->", list_of_turns1)
#print("list_of_turns2---->", list_of_turns2)
#print("Flag 1---->", Flag1)
#print("Flag 2---->", Flag2)
#print("Steps---->", steps)
#print("ListofDirections - --- > ", list_of_directions)
#print("Top Element----->",top_element)
#print("Right Element----->",right_element)
#print("Front Element----->",front_element)
print(f'On cell {number}, {top_element} is at the top, {front_element} at the front, and {right_element} on the right.')
# Insert your code here
