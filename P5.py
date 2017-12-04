# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by Subham Anand for COMP9021

import collections
class PermutationError(Exception):
    def __init__(self, message):
        self.message = message
        
class Permutation:
    def __init__(self, *args, length = None):
        L = []
        L1 = []
        counter = 0
        
        for arg in args:
            L1.append(arg)
        for i in range(1,len(L1) + 1):
            if i in L1:
                counter += 1
        for arg in args:
            if isinstance(arg,int) == False:
                raise PermutationError('Cannot generate permutation from these arguments')
            if arg == 0:
                raise PermutationError('Cannot generate permutation from these arguments')

        if length != None and length < 0:
            raise PermutationError('Cannot generate permutation from these arguments')

        elif length != None and len(args) != length and len(args) != 0:
            raise PermutationError('Cannot generate permutation from these arguments')

        elif counter != len(args):
            raise PermutationError('Cannot generate permutation from these arguments')

        elif length != None and (len(args) < 1) :
            for i in range(1, length + 1):
                L.append(i)
            self.args = tuple(L)

        else:
            self.args = args
            self.length = length
        self.nb_of_cycles = self.len_()
        # Replace pass above with your code

    def __len__(self):
        nb_of_cycles = len(self.args)
        return nb_of_cycles
        # Replace pass above with your code

    def __repr__(self):
        a = ''
        L = []
        for arg in self.args:
            L.append(arg)
        a = ', '.join(str(item) for item in L)
        return f'Permutation({a})'
	# Replace pass above with your code

    def __str__(self):
        a = []
        a1 = []
        L1 = []
        L2 = []
        b = ''
        c=''
        if len(self.args) == 0:
            c = '()'
            return c
        for arg in self.args:
            L1.append(arg)
        #a = ')('.join(str(item) for item in L1)
        #a = '(' + a + ')'
        a = self.cycles(L1)
        for items in a:
            myList = ' '.join(map(str, items))
            b = '(' + myList + ')'
            L2.append(b)
        c = ''.join(i for i in L2)
                #b = b + str(itm)
            #c = c+'('+b+')'
        #print(L2)
            
        return c
        pass
        # Replace pass above with your code

    def __mul__(self, permutation):
        my_mul = []
        p1 = []
        p2 = []
        for arg in self.args:
            p1.append(arg)
        for arg in permutation.args:
            p2.append(arg)
        print(p1)
        print(p2)
        if len(p1) != len(p2):
            raise PermutationError('Cannot compose permutations of different lengths')
        if len(p1) == len(p2):
            for i in range(len(p1)):
                my_mul.append(p2[p1[i] - 1])
        p3 = tuple(my_mul)
        return Permutation(*p3)
        
        # Replace pass above with your code

    def __imul__(self, permutation):
        my_imul = []
        p1 = list(permutation.args)
        p2 = list(self.args)
        if len(p1) != len(p2):
            raise PermutationError('Cannot compose permutations of different lengths')
        if len(p1) == len(p2):
            for i in range(len(p2)):
                my_imul.append(p1[p2[i] - 1])
        p3 = tuple(my_imul)
        return Permutation(*p3)
        # Replace pass above with your code

    def inverse(self):
        L2 = []
        D = {}
        l_args = len(self.args)
        L3 = []
        L4 = []
        for arg in self.args:
            L2.append(arg)
        for i in range(1,len(L2) + 1):
            D[i] = L2[i-1]
        res = dict((v,k) for k,v in D.items())
        od = collections.OrderedDict(sorted(res.items()))
        for i in od.values():
            L4.append(i)
        for items in L4:
            myList = ' '.join(map(str, L4))
        myList = '(' + myList + ')'
        return Permutation(*L4)
        # Replace pass above with your code

    def len_(self):
        L1 = []
        for arg in self.args:
            L1.append(arg)
        nb_of_cycles = len(self.cycles(L1))
        return nb_of_cycles

    def cycles(self,perm):
        x = set(perm)
        z = []
        r =()
        N = []
        D1 = {}
        N1 = []
        while len(x) > 0:
            n = x.pop()
            cycle = [n]
            while True:
                n = perm[n-1]
                if n not in x:
                    break
                x.remove(n)
                cycle.append(n)
            z.append(cycle)
        for items in z:
            max1 = items.index(max(items))
            items1 = items[max1:] + items[:max1]
            N.append(items1)
        for items in N:
            D1[items[0]] = items
        od = collections.OrderedDict(sorted(D1.items()))
        for i in od.values():
            N1.append(i)
        N2 = N1
        return N2


#p = Permutation(2,3,4,5,1)
#print(p)
#print(p.nb_of_cycles)
#len(p)
#print(p.inverse())
    # Insert your code for helper functions, if needed



                
        
