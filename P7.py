# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Subham Anand for COMP9021


import sys
from random import seed, randrange

from stack_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def explore_depth_first(x, y, target):
	zero_count = 0
	all_sum = 0
	for i in range(10):
		for j in range(10):
			if grid[i][j] == 0:
				zero_count += 1
	if zero_count == 100:
		return
	for i in range(10):
		for j in range(10):
			all_sum += grid[i][j]
	if all_sum < target:
		return
	global sum1
	sum1 = 0
	global mystack
	mystack = Stack()
	global goingnorth
	goingnorth = False
	global goingeast
	goingeast = False
	global goingsouth
	goingsouth = False
	global goingwest
	goingwest = False
	#mystack = Stack()
	a = x
	b = y
	if target > 0 :
		mystack.push((a,b))
	sum = 0
	indexes = []
	cycle = True
	north = True
	east = False
	south = False
	west = False
	first = True
	mycount = 0
	temp = []
	n1 = None
	e1 = None
	s1 = None
	w1 = None
	count = 0
	count3 = 0
	flag1 = True
	#L = moving(x,y)
	while cycle == True and sum <= target and not mystack.is_empty():
		#going north
		count2 = 0
		popped = mystack.pop()
		a = popped[0]
		b = popped[1]
		flag = False
		if sum:
			sum = sum - grid[a][b]
		try:
			indexes.remove(popped)
		except ValueError:
			pass
		if north == True:
			count = 0
			mycount += 1
			if first:
				first = False
				for i in range(a, -1, -1):
					
					if sum + grid[i][b] <= target:
						for f in range(0,len(temp)):
							if temp[f] == (i,b):
                            	
								try:
									if temp[f+1] == (i-1,b):
                                    	
										count+=1
								except IndexError:
									pass
						if count > 0:
                        	
							break
						if (i,b) not in indexes:
							indexes.append((a,b))
							temp.append((a,b))
							sum += grid[i][b]
							indexes.append((i,b))
							mystack.push((i, b))
							n1 = ((i,b))
							temp.append((i,b))
						else:
							break
					else:
						break
					if sum == target and first == False:
						first = True
						break
				if sum < target:
					east = True
				else:
					break
			else:
				count = 0
				#top = mystack.peek()
				#a = top[0]
				#b = top[1]
				flag1 = True
				for i in range(a-1, -1, -1):
					if sum + grid[i][b] <= target:
						if n1 == (i,b) or (i-1,b) == n1:
							if count3:
								flag = True
								mystack.push((a,b))
							break
							
						for f in range(0,len(temp)):
							if temp[f] == (i,b):
                            	#print("True1")
								try:
									if temp[f+1] == (i-1,b):
                                    	#print("True2")
										count+=1
								except IndexError:
									pass
						if count > 0:
                        	#print('North Break')
							break
						
						if (i,b) not in indexes:
							if (a,b) not in indexes:
								mystack.push((a,b))
								
								indexes.append((a,b))
								temp.append((a,b))
							sum += grid[i][b]
							indexes.append((i,b))
							n1 = (i,b)
							mystack.push((i, b))
							flag1 = False
							temp.append((i,b))
							if count2 == 0 and count3 != 0:
								sum = sum + grid[a][b]
								count2+=1
						else:
							if count3 and flag1 == True:
								flag = True
								mystack.push((a,b))
							break
					else:
						if count3:
							flag = True
							mystack.push((a,b))
						break
					if sum == target:
						break
		if sum < target:
			east = True
		#going east
		if east == True:
			top = mystack.peek()
			a = top[0]
			b = top[1]
			flag1 =True
			if flag == True:
				mystack.pop()
				flag = False
			count = 0
			for i in range(b+1, 10):
				if sum + grid[a][i] <= target:
					if e1 == (a,i) or (a,i+1) == e1:
						if count3:
							flag = True
							mystack.push((a,b))
						break
						
					for f in range(0,len(temp)):
						if temp[f] == (a,i):
                           	#print("True1")
							try:
								if temp[f+1] == (a,i+1):
                                   	#print("True2")
									count+=1
							except IndexError:
								pass
					if count > 0:
                        	#print('North Break')
						break
					
					if (a,i) not in indexes:
						if (a,b) not in indexes:
							mystack.push((a,b))
							indexes.append((a,b))
							temp.append((a,b))
						sum += grid[a][i]
						indexes.append((a,i))
						e1 = (a,i)
						mystack.push((a, i))
						flag1 = False
						temp.append((a,i))
						if count2 == 0 and count3 != 0:
							sum = sum + grid[a][b]
							count2+=1
					else:
						if count3 and flag1 == True:
							flag = True
							mystack.push((a,b))
						break
				else:
					if count3:
						flag = True
						mystack.push((a,b))
					
					break
				if sum == target:
					break
		if sum < target:
			south = True
		#going south
		if south == True:
			top = mystack.peek()
			a = top[0]
			b = top[1]
			flag1 = True
			if flag == True:
				mystack.pop()
				flag = False
			count = 0
			for i in range(a+1, 10):
				if sum + grid[i][b] <= target:
					if s1 == (i,b) or (i+1,b) == s1:
						if count3:
							flag = True
							mystack.push((a,b))
						break
						
					for f in range(0,len(temp)):
						if temp[f] == (i,b):
                           	#print("True1")
							try:
								if temp[f+1] == (i+1,b):
                                   	#print("True2")
									count+=1
							except IndexError:
								pass
					if count > 0:
                        	#print('North Break')
						break
					
					if (i,b) not in indexes:
						if (a,b) not in indexes:
							mystack.push((a,b))
							indexes.append((a,b))
							temp.append((a,b))
						sum += grid[i][b]
						indexes.append((i,b))
						s1 = (i,b)
						mystack.push((i, b))
						flag1 = False
						temp.append((i,b))
						if count2 == 0 and count3 != 0:
							sum = sum + grid[a][b]
							count2+=1
					else:
						if count3 and flag1 == True:
							flag = True
							mystack.push((a,b))
						break
				else:
					if count3:
						flag = True
						mystack.push((a,b))
					break
				if sum == target:
					break
		if sum < target:
			west = True
			#going west
		if west == True:
			top = mystack.peek()
			a = top[0]
			b = top[1]
			flag1 =True
			if flag == True:
				mystack.pop()
				flag = False
			count = 0
			for i in range(b-1, -1, -1):
				if sum + grid[a][i] <= target:
					if w1 == (a,i) or (a,i-1) == w1:
						if count3:
							flag = True
							mystack.push((a,b))
						break
						
					for f in range(0,len(temp)):
						if temp[f] == (a,i):
                           	#print("True1")
							try:
								if temp[f+1] == (a,i-1):
                                   	#print("True2")
									count+=1
							except IndexError:
								pass
					if count > 0:
                        	#print('North Break')
						break
						
					if (a,i) not in indexes:
						if (a,b) not in indexes:
							mystack.push((a,b))
							indexes.append((a,b))
							temp.append((a,b))
						sum += grid[a][i]
						indexes.append((a,i))
						w1 = (a,i)
						mystack.push((a, i))
						flag1 = False
						temp.append((a,i))
						if count2 == 0 and count3 != 0:
							sum = sum + grid[a][b]
							count2+=1
					else:
						if count3 and flag1 == True:
							flag = True
							mystack.push((a,b))
						break
				else:
					break
				if sum == target:
					break
			
		if sum < target:
			#print(mystack._data)
			north =True
			cycle = True
			count3+=1
		else:
			north = False
			cycle = False
		if mycount == 100:
			while not mystack.is_empty():
				mystack.pop()
			break
	L1 = []
	while not mystack.is_empty():
		L1.append(mystack.pop())
	
	if len(L1) != 0:
		g,h = L1[0]
		if grid[g][h] == 0:
			L1.pop(0)
	b = L1[::-1]
	#print(temp)
	return b

    # Replace pass above with your code


try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
