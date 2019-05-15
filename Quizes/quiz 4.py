# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by Subham Anand for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():
    global grid1
    grid1 = list(grid)
    zero = []
    for i in range(height):
        grid1[i].append(0)
        grid1[i].reverse()
        grid1[i].append(0)
        grid1[i].reverse()
    for i in range(width+2):
        zero.append(0)
    grid1.append(zero)
    grid1.reverse()
    grid1.append(zero)
    grid1.reverse()
    areas = {}
    b = 0
    global max_length
    path = {}
    counter = 0
    for i in range(1,height+1):
        for j in range(1,width+1):
            if grid1[i][j] == 1:
                if grid1[i][j+1] != 2 and grid1[i][j-1] != 2 and grid1[i+1][j] != 2 and grid1[i-1][j] != 2 :
                    counter += 1
                    areas[1] = counter

    while max_length > 1:
        for i in range(1,height+1):
            for j in range(1,width+1):
                if grid1[i][j] == max_length:
                    
                    if grid1[i][j+1] != max_length + 1 and grid1[i][j-1] != max_length + 1 and grid1[i-1][j] != max_length + 1 and grid1[i+1][j] != max_length + 1 :
                        b = areas_of_region(max_length,i,j)
                        if max_length in areas:
                            areas[max_length] = areas[max_length] + b
                        else:
                            areas[max_length] = b
        max_length -= 1
                    
    return areas
    
    # Replace pass above with your code
# Insert your code for other functions


        
def areas_of_region(n,i,j,counter = 0, a = 0):
    if grid1[i][j+1] == n-1 and n > 1:
        if n-1 == 1 and n > 1:
            a+=1
        a += areas_of_region(n-1,i,j+1)

    if grid1[i][j-1] == n-1 and n > 1:
        if n-1 == 1 and n > 1:
            a+=1
        a += areas_of_region(n-1,i,j-1)

    if grid1[i+1][j] == n-1 and n > 1:
        if n-1 == 1 and n > 1:
            a+=1
        a += areas_of_region(n-1,i+1,j)

    if grid1[i-1][j] == n-1 and n > 1:
        if n-1 == 1 and n > 1:
            a+=1
        a += areas_of_region(n-1,i-1,j)

    return a


try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
#convert_grid()
paths = get_paths()


if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
