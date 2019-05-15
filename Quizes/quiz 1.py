# Written by Subham Anand for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''


import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = []
N = []

# Replace this comment with your code
# L =      [1,4,0,2,0]
# answer = [1,4,0,0,2]
import copy
L1 = copy.deepcopy(L)
M = []
M.append(L1.pop(len(L1)//2))
for i in range(len(L)):
    try:
        M.append(L1.pop(0))
        M.append(L1.pop())
    except IndexError:
        pass

N = []
N.append(L[0])
a = L[0]
flag = 0
index = []
index.append(0)
while len(L) != len(N) :
    if a in index:
         for i in range(len(L)):
             if i not in index:
                 N.append(L[i])
         break
    else:
        #if a == len(L) - 1
        #    a = 0
        #    continue
        #else:
        #    a = a + 1
        #    continue



        N.append(L[a])
        index.append(a)
        a = L[a]

    
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)

