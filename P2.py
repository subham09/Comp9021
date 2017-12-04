# Written by *** and Subham Anand for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd
from fractions import Fraction


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions =  []
spot_on, closest_1, closest_2 = [None] * 3

# Replace this comment with your code

#declaration
M = []
N = []
P = []
Q = []
R = []
S = []

#swaping method
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
	
L.sort()

#checking for size of list and value less than 1
if len(L)==1:
    if L[0]<=1:
        P.append(L[0])
        closest_1 = L[0]
        fractions.append(str(L[0]))
else:
    for i in range (0,len(L)-1):
        for j in range(i+1,len(L)):
            M.append(str(L[i])+'/'+str(L[j]))
        M.append(1)
    for item in M:
        N.append(Fraction(item))
    P = list(set(N))

    for i in range(len(P)):
        for k in range(len(P)-1,i,-1):
            if (P[k]<P[k-1]):
                swap(P,k,k-1)

    #printing P without fraction 
    for items in P:
        fractions.append(str(items))
	#fractions = S
    

    #finding spot on
    for item in P:
        if (item==Fraction(1,2)):
            spot_on= 1

    #getting difference
    if spot_on==None:
        for item in P:
            Q.append(abs(Fraction(1,2)-item))


    #sorting the differences
        for i in range(len(Q)):
            for k in range(len(Q)-1,i,-1):
                if (Q[k]<Q[k-1]):
                    swap(Q,k,k-1)

    #if only one close
        if len(Q)>1:
            if Q[0]!=Q[1]:
                for item in P:
                    if (abs(item-Fraction(1,2))==Q[0]):
                        closest_1=str(item)
        else:
            if (abs(P[0]-Fraction(1,2))==Q[0]):
                closest_1 = str(P[0])


    #if two num are close
        if len(Q)>1:
            if Q[0]==Q[1]:
                for item in P:
                    if(abs(item-Fraction(1,2))==Q[0]):
                        R.append(item)
                closest_1 = str(R[0])
                closest_2 = str(R[1])
# Replace this comment with your code

print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
