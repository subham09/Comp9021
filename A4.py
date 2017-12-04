from random import seed
from random import randint
from itertools import groupby

list_face = ['Ace', 'King', '9', 'Queen','Jack']
dict_face = {'Ace':60,'King':50,'Queen':40,'Jack':30, '10':20,'9':10}
gen_roll = []
gen_roll1 = []
gen_face = []
gen_face1 = []

def roll_dice(n):
    for i in range(n):
        gen_roll1.append(randint(0,5))
    gen_roll = list(gen_roll1)
    del gen_roll1[:]
    return gen_roll

def convert_face(L):
    for items in L:
        if items == 0:
            gen_face1.append('Ace')
        if items == 1:
            gen_face1.append('King')
        if items == 2:
            gen_face1.append('Queen')
        if items == 3:
            gen_face1.append('Jack')
        if items == 4:
            gen_face1.append('10')
        if items == 5:
            gen_face1.append('9')
    gen_face = list(gen_face1)
    del gen_face1[:]
    return gen_face

def define_kind(L):
    a = sorted(L)
    a1 = [len(list(group)) for key, group in groupby(a)]
    a2 = sorted(a1)[::-1]
    #print('a2--->',a2)
    if a1 == [5]:
        result = 'It is a Five of a kind'
    if a2 == [4,1]:
        result = 'It is a Four of a kind'
    if a2 == [3,2]:
        result = 'It is a Full house'
    if a1 == [1,1,1,1,1] and (('Ace' in L and '9' not in L) or ('Ace' not in L and '9' in L)):
        result = 'It is a Straight'
    if a2 == [3,1,1]:
        result = 'It is a Three of a kind'
    if a2 == [2,2,1]:
        result = 'It is a Two pair'
    if a2 == [2,1,1,1]:
        result = 'It is a One pair'
    if a1 == [1,1,1,1,1] and ('Ace' in L and '9' in L):
        result = 'It is a Bust'
    del a1[:]
    del a2[:]
    return result

def sort_face(L):
    L.sort(key=lambda x: dict_face[x], reverse=True)
    return L

def play():
    a = roll_dice(5)
    b1 = convert_face(a)
    b =  sort_face(b1)
    #print(b)
    print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
    print(define_kind(b))
    c = input('Which dice do you want to keep for the second roll? ')
    c1 = c.split(' ')
    value = chance(c,c1,b)
    if value == 2:
        return
    while value == 1:
        c = input('Which dice do you want to keep for the second roll? ')
        c1 = c.split(' ')
        value = chance(c,c1,b)
        if value == 2:
            return
    if value == 3:
        s = []
        s1 =[]
        s5 = []
        s = roll_dice(5)
        s1 = convert_face(s)
        s5 = sort_face(s1)
        print(f'The roll is: {s5[0]} {s5[1]} {s5[2]} {s5[3]} {s5[4]}')
        print(define_kind(s5))
        s3 = input('Which dice do you want to keep for the third roll? ')
        s4 = s3.split(' ')
        value = chance(s3,s4,s5)
        if value == 3:
            s = roll_dice(5)
            s1 = convert_face(s)
            s5 = sort_face(s1)
            print(f'The roll is: {s5[0]} {s5[1]} {s5[2]} {s5[3]} {s5[4]}')
            print(define_kind(s5))
            return
        elif value == 1:
            while value == 1:
                c = input('Which dice do you want to keep for the third roll? ')
                c1 = c.split(' ')
                value = chance(c,c1,b)
                if value == 2:
                    return
                if value == 3:
                    s6 = roll_dice(5)
                    s7 = convert_face(s6)
                    s8 = sort_face(s7)
                    print(f'The roll is: {s8[0]} {s8[1]} {s8[2]} {s8[3]} {s8[4]}')
                    print(define_kind(s8))
                    return
        else:
            return


    if value != 1 and value !=3 :
        b = value
    c2 = input('Which dice do you want to keep for the third roll? ')
    c3 = c2.split(' ')
    value1 = chance(c2,c3,b)
    while value1 == 1:
        c2 = input('Which dice do you want to keep for the third roll? ')
        c3 = c2.split(' ')
        value1 = chance(c2,c3,b)
        if value == 2:
            return

def chance(choice, choice1,b):
    #a = roll_dice(5)
    #b = convert_face(a)
    #print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
    #print('a--->',a)
    #print('b--->',b)
    #print(define_kind(b))
    #choice = input('Which dice do you want to keep for the second roll?')
    
    #choice1 = choice.split(' ')
    result = 0
    if choice == 'all' or choice == 'All':
        print('Ok, done.')
        result = 2
        return result

    elif choice1 == ['']:
        result = 3
        return result

    elif len(choice1) == 1 and choice in b:
        #b.remove(choice)
        del b[:]
        b.append(choice)
        #print('removeing b',b)
        second_roll_dice = roll_dice(4)
        second_roll_face = convert_face(second_roll_dice)
        for item in second_roll_face:
            b.append(item)
        #print('adding b',b)
        b = sort_face(b)
        print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
        print(define_kind(b))
        return b

    elif len(choice1) == 2:
        if choice1[1] == choice1[0]:
            if choice1.count(choice1[0]) == b.count(choice1[0]) or b.count(choice1[0]) > choice1.count(choice1[0]):
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                #print('removeing b',b)
                second_roll_dice = roll_dice(3)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                return b
            else:
                
                print('That is not possible, try again!')
                result = 1
                return result
        else:
            if choice1[0] in b and choice1[1] in b:
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                #print('removeing b',b)
                second_roll_dice = roll_dice(3)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                return b
            else:
                print('That is not possible, try again!')
                result = 1
                return result

    elif len(choice1) == 3:
        if choice1[1] == choice1[0] == choice1[2]:
            if choice1.count(choice1[0]) == b.count(choice1[0]):
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                #b.remove(choice1[2])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                b.append(choice1[2])
                #print('removeing b',b)
                second_roll_dice = roll_dice(2)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                return b
            else:
                print('That is not possible, try again!')
                result = 1
                return result
        elif choice1[0] != choice1[1] and choice1[1] != choice1[2] and choice1[0] != choice1[2]:
            if choice1[0] in b and choice1[1] in b and choice1[2] in b :
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                #b.remove(choice1[2])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                b.append(choice1[2])
                #print('removing b',b)
                second_roll_dice = roll_dice(2)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                #print('going through')
                return b
            else:
                print('That is not possible, try again!')
                result = 1
                return result
        elif choice1[0] in b and choice1[1] in b and choice1[2] in b :
            if choice1.count(choice1[0]) == b.count(choice1[0]) and choice1.count(choice1[1]) == b.count(choice1[1]) and choice1.count(choice1[2]) == b.count(choice1[2]) :
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                #b.remove(choice1[2])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                b.append(choice1[2])
                #print('removeing b',b)
                second_roll_dice = roll_dice(2)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                #print('going through')
                return b
            else:
                print('That is not possible, try again!')
                result = 1
                return result
            #print('yipeee')
        else:
            print('That is not possible, try again!')
            result = 1
            return result

    elif len(choice1) == 4:
        if choice1[1] == choice1[0] == choice1[2] == choice1[3]:
            if choice1.count(choice1[0]) == b.count(choice1[0]):
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                #b.remove(choice1[2])
                #b.remove(choice1[3])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                b.append(choice1[2])
                b.append(choice1[3])
                #print('removeing b',b)
                second_roll_dice = roll_dice(1)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                return b
            else:
                print('That is not possible, try again!')
                result = 1
                return result
        elif choice1[0] != choice1[1] and choice1[1] != choice1[2] and choice1[2] != choice[3] and choice1[0] != choice1[3] and choice1[1] != choice1[3]:
            if choice1[0] in b and choice1[1] in b and choice1[2] in b and choice1[3] in b:
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                #b.remove(choice1[2])
                #b.remove(choice1[3])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                b.append(choice1[2])
                b.append(choice1[3])
                #print('removeing b',b)
                second_roll_dice = roll_dice(1)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                return b
            else:
                print('That is not possible, try again!')
                result = 1
                return result
        elif choice1[0] in b and choice1[1] in b and choice1[2] in b and choice1[3] in b:
            if choice1.count(choice1[0]) == b.count(choice1[0]) and choice1.count(choice1[1]) == b.count(choice1[1]) and choice1.count(choice1[2]) == b.count(choice1[2]) and choice1.count(choice1[3]) == b.count(choice1[3]):
                #b.remove(choice1[0])
                #b.remove(choice1[1])
                #b.remove(choice1[2])
                #b.remove(choice1[3])
                del b[:]
                b.append(choice1[0])
                b.append(choice1[1])
                b.append(choice1[2])
                b.append(choice1[3])
                #print('removeing b',b)
                second_roll_dice = roll_dice(1)
                second_roll_face = convert_face(second_roll_dice)
                for item in second_roll_face:
                    b.append(item)
                #print('adding b',b)
                b = sort_face(b)
                print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
                print(define_kind(b))
                #print('i am in')
                return b
            else:
                print('That is not possible, try again!')
                result = 1
                return result
        else:
            print('That is not possible, try again!')
            result = 1
            return result

    elif len(choice1) == 5:
        if sorted(choice1) == sorted(b):
            print('Ok, done.')
            result = 2
            return result
        else:
            print('That is not possible, try again!')
            result = 1
            return result
    else:
        print('That is not possible, try again!')
        result = 1
        return result









    #choice2 = input('Which dice do you want to keep for the third roll?')
    #choice3 = choice2.split(' ')

    #if choice2 == 'all' or choice2 == 'All':
    #    print('Ok Done')
    #    return

    #elif len(choice3) == 1 and choice2 in b:
    #    b.remove(choice2)
    #    print('removeing b',b)
    #    second_roll_dice = roll_dice(1)
    #    second_roll_face = convert_face(second_roll_dice)
    #    for item in second_roll_face:
    #        b.append(item)
    #    print('adding b',b)
    #    print(define_kind(b))

    #elif len(choice3) == 2:
    #    if choice3[1] == choice3[0]:
    #        if choice3.count(choice3[0]) == b.count(choice3[0]) or b.count(choice3[0]) > choice3.count(choice3[0]):
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            print('removeing b',b)
    #            second_roll_dice = roll_dice(2)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #        else:
    #            print('That is not possible try again')
    #    else:
    #        if choice3[0] in b and choice3[1] in b:
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            print('removeing b',b)
    #            second_roll_dice = roll_dice(2)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #        else:
    #            print('That is not possible try again')
    #elif len(choice3) == 3:
    #    if choice3[1] == choice3[0] == choice3[2]:
    #        if choice3.count(choice3[0]) == b.count(choice3[0]):
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            b.remove(choice3[2])
    #            print('removeing b',b)
    #            second_roll_dice = roll_dice(3)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #        else:
    #            print('That is not possible try again')
    #    elif choice3[0] != choice3[1] and choice3[1] != choice3[2] and choice3[0] != choice3[2]:
    #        if choice3[0] in b and choice3[1] in b and choice3[2] in b :
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            b.remove(choice3[2])
    #            print('removing b',b)
    #            second_roll_dice = roll_dice(3)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #            print('going through')
    #        else:
    #            print('That is not possible try again')
    #    elif choice3[0] in b and choice3[1] in b and choice3[2] in b :
    #        if choice3.count(choice3[0]) == b.count(choice3[0]) and choice3.count(choice3[1]) == b.count(choice3[1]) and choice3.count(choice3[2]) == b.count(choice3[2]) :
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            b.remove(choice3[2])
    #            print('removeing b',b)
    #            second_roll_dice = roll_dice(3)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #            print('going through')
    #        else:
    #            print('That is not possible try again')
    #        #print('yipeee')
    #    else:
    #        print('That is not possible try again')
    #elif len(choice3) == 4:
    #    if choice3[1] == choice3[0] == choice3[2] == choice3[3]:
    #        if choice3.count(choice3[0]) == b.count(choice3[0]):
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            b.remove(choice3[2])
    #            b.remove(choice3[3])
    #            print('removeing b',b)
    #            second_roll_dice = roll_dice(4)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #        else:
    #            print('That is not possible try again')
    #    elif choice3[0] != choice3[1] and choice3[1] != choice3[2] and choice3[2] != choice3[3] and choice3[0] != choice3[3] and choice3[1] != choice3[3]:
    #        if choice3[0] in b and choice3[1] in b and choice3[2] in b and choice3[3] in b:
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            b.remove(choice3[2])
    #            b.remove(choice3[3])
    #            print('removeing b',b)
    #            second_roll_dice = roll_dice(4)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #        else:
    #            print('That is not possible try again')
    #    elif choice3[0] in b and choice3[1] in b and choice3[2] in b and choice3[3] in b:
    #        if choice3.count(choice3[0]) == b.count(choice3[0]) and choice3.count(choice3[1]) == b.count(choice3[1]) and choice3.count(choice3[2]) == b.count(choice3[2]) and choice3.count(choice3[3]) == b.count(choice3[3]):
    #            b.remove(choice3[0])
    #            b.remove(choice3[1])
    #            b.remove(choice3[2])
    #            b.remove(choice3[3])
    #            print('removeing b',b)
    #            second_roll_dice = roll_dice(4)
    #            second_roll_face = convert_face(second_roll_dice)
    #            for item in second_roll_face:
    #                b.append(item)
    #            print('adding b',b)
    #            print(define_kind(b))
    #            print('i am in')
    #        else:
    #            print('That is not possible try again')
    #    else:
    #            print('That is not possible try again')
    #elif len(choice3) == 5:
    #    if choice3 == b:
    #        print('Ok done')
    #        return
    #    else:
    #        print('That is not possible try again')
    #else:
    #    print('That is not possible try again')


#a = roll_dice(5)
#print(a)
#print(convert_face(a))
#print(define_kind(list_face))
#seed(0)
#play()

#def simulate(n):
#    print('Five of a kind :'(float(6/7776*n)))
#    print('Four of a kind :')
#    print('Full house     :')
#    print('Straight       :')
#    print('Three of a kind:')
#    print('Two pair       :')
#    print('One pair       :')
def play1():
    a = roll_dice(5)
    b1 = convert_face(a)
    b =  sort_face(b1)
    #print(b)
    #print(f'The roll is: {b[0]} {b[1]} {b[2]} {b[3]} {b[4]}')
    #print(define_kind(b))
    c= define_kind(b)
    return c


def simulate(n):
    c2 = []
    five_kind = 0
    four_kind = 0
    full_house = 0
    straight = 0
    three_kind = 0
    two_kind = 0
    one_kind = 0
    for i in range(n):
        c1 = play1()
        c2.append(c1)
    #print(c2)
    for item in c2:
        if item == 'It is a Five of a kind':
            five_kind += 1
        if item == 'It is a Four of a kind':
            four_kind += 1
        if item == 'It is a Full house':
            full_house += 1
        if item == 'It is a Straight':
            straight += 1
        if item == 'It is a Three of a kind':
            three_kind += 1
        if item == 'It is a Two pair':
            two_kind += 1
        if item == 'It is a One pair':
            one_kind += 1
    a = five_kind * 100/n
    b = four_kind * 100/n
    c = full_house * 100/n
    d = straight * 100/n
    e = three_kind * 100/n
    f = two_kind * 100/n
    g = one_kind * 100/n
    #print(five_kind,' ',four_kind,' ',full_house,' ',straight,' ',three_kind,' ',two_kind,' ',one_kind)
    print(f'Five of a kind : {a:.2f}%')
    print(f'Four of a kind : {b:.2f}%')
    print(f'Full house     : {c:.2f}%')
    print(f'Straight       : {d:.2f}%')
    print(f'Three of a kind: {e:.2f}%')
    print(f'Two pair       : {f:.2f}%')
    print(f'One pair       : {g:.2f}%')

#play()
#seed(0)
#simulate(10)
#def simulate(n):
#    print('Five of a kind :'(float(6/7776*n)))
#    print('Four of a kind :')
#    print('Full house     :')
#    print('Straight       :')
#    print('Three of a kind:')
#    print('Two pair       :')
#    print('One pair       :')
#if a1 == [5]:
#        result = 'It is a Five of a kind'
#    if a2 == [4,1]:
#        result = 'It is a Four of a kind'
#    if a2 == [3,2]:
#        result = 'It is a Full house'
#    if a1 == [1,1,1,1,1] and (('Ace' in L and '9' not in L) or ('Ace' not in L and '9' in L)):
#        result = 'It is a Straight'
#    if a2 == [3,1,1]:
#        result = 'It is a Three of a kind'
#    if a2 == [2,2,1]:
#        result = 'It is a Two pair'
#    if a2 == [2,1,1,1]:
#        result = 'It is a One pair'
#    if a1 == [1,1,1,1,1] and ('Ace' in L and '9' in L):
#        result = 'It is a Bust'
#print(f'{3/5:.2f}')
