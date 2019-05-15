import os
import argparse
import subprocess
from collections import OrderedDict
from operator import itemgetter
import itertools
import copy

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message

class Sudoku:
    def __init__(self, filename):
        self.filename = filename
        L = []
        L1 = []
        L3 = []
        a, b = os.path.splitext(self.filename)
        #validation for txt file
        if str(b).lower() != '.txt':
            raise SudokuError('Incorrect input')
        #file exists or not
        if  os.path.isfile(self.filename) == False:
            raise SudokuError('Incorrect input')
        #opening file
        with open(self.filename,'r') as file:
            for items in file:
                L.append(items.strip('\n'))
        #replacing space with nothing
        for items in L:
            #items.strip()
            L1.append(items.replace(' ',''))
        #removing all none
        L1 = list(filter(None, L1))
        for items in L1:
            if items[0].isdigit() == False:
                L1.remove(items)
        #checking length of line
        if len(L1) != 9:
            raise SudokuError('Incorrect input')
        #checking length of digits in line
        for items in L1:
            if len(items) != 9:
                raise SudokuError('Incorrect input')
        #checking item it should be digit
        for items in L1:
            for letter in items:
                if letter.isdigit() == False:
                    raise SudokuError('Incorrect input')
        #int list of inputs
        self.L1 = L1
        L3 = [list(map(int, x)) for x in self.L1]
        self.L3 = L3
        self.L4 = []

    def preassess(self):
        L2,L3,L4,L5,L6,L7,L8 = [],[],[],[],[],[],[]
        total = ''
        a = ''
        #for colomn
        L2 = [list(map(int, x)) for x in self.L1]
        for items in L2:
            L3 = list(filter(lambda a: a != 0, items))
            if len(L3) != len(set(L3)):
                print('There is clearly no solution.')
                return

        #for row
        L5 = list(map(list, zip(*L2)))
        #print('L5-->',L5)
        
        for items in L5:
            L6 = list(filter(lambda a: a != 0, items))
            if len(L6) != len(set(L6)):
                print('There is clearly no solution.')
                return

        #for 3*3 matrix
        for i in range(0,3):
            for j in range(0,3):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L3) != len(set(L3)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(0,3):
            for j in range(3,6):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L8) != len(set(L8)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(0,3):
            for j in range(6,9):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L3) != len(set(L3)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(3,6):
            for j in range(0,3):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L3) != len(set(L3)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(3,6):
            for j in range(3,6):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L8) != len(set(L8)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(3,6):
            for j in range(6,9):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L3) != len(set(L3)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(6,9):
            for j in range(0,3):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L3) != len(set(L3)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(6,9):
            for j in range(3,6):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L8) != len(set(L8)):
            print('There is clearly no solution.')
            return
        del L8[:]

        for i in range(6,9):
            for j in range(6,9):
                L8.append(L2[i][j])
        L8 = list(filter(lambda a: a != 0, L8))
        if len(L3) != len(set(L3)):
            print('There is clearly no solution.')
            return
        del L8[:]

        self.L2 = L2
        print('There might be a solution.')
        return

    def bare_tex_output(self):
        a, b = os.path.splitext(self.filename)
        tex_file_content = r'''\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline
% Line 1'''
        
        bare_tex_file = open(a+'_bare.tex', 'w+')
        bare_tex_file.write(tex_file_content)
        bare_tex_file.write('\n')
        counter  = 0
        for i in range(9):
            for j in range(9):
                if self.L3[i][j] == 0:
                    bare_tex_file.write(r'\N{}{}{}{}{} ')
                    counter+=1
                else:
                    st = r'\N{}{}{}{}{' + str(self.L3[i][j]) + '} '
                    bare_tex_file.write(st)
                    counter+=1
                if counter % 9 != 0:
                    bare_tex_file.write(r'& ')
                else:
                    if counter in (27,54,81) :
                        
                        bare_tex_file.write(r'\\ \hline\hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                    else:
                        
                        bare_tex_file.write(r'\\ \hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                if counter%3==0:
                    bare_tex_file.write('\n')
        last_content = r'''\end{tabular}
\end{center}

\end{document}'''
        bare_tex_file.write(last_content)

        #print(tex_file_content)

    def forced_tex_output(self):

        self.bare_tex_output()
        all_indexes = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)], [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
                       [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)], [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)], [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
                       [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)], [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)], [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]]
        #for i in range(0,9):
        #    for j in range(0,9):
        #        all_indexes_for_line.append((i,j))
        original_all_indexes = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)], [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
                               [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)], [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)], [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
                               [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)], [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)], [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]]

        index_mapping = {(0,0):(0,0),(0,1):(0,1),(0,2):(0,2),(0,3):(1,0),(0,4):(1,1),(0,5):(1,2),(0,6):(2,0),(0,7):(2,1),(0,8):(2,2),
                         (1,0):(0,3),(1,1):(0,4),(1,2):(0,5),(1,3):(1,3),(1,4):(1,4),(1,5):(1,5),(1,6):(2,3),(1,7):(2,4),(1,8):(2,5),
                         (2,0):(0,6),(2,1):(0,7),(2,2):(0,8),(2,3):(1,6),(2,4):(1,7),(2,5):(1,8),(2,6):(2,6),(2,7):(2,7),(2,8):(2,8),
                         (3,0):(3,0),(3,1):(3,1),(3,2):(3,2),(3,3):(4,0),(3,4):(4,1),(3,5):(4,2),(3,6):(5,0),(3,7):(5,1),(3,8):(5,2),
                         (4,0):(3,3),(4,1):(3,4),(4,2):(3,5),(4,3):(4,3),(4,4):(4,4),(4,5):(4,5),(4,6):(5,3),(4,7):(5,4),(4,8):(5,5),
                         (5,0):(3,6),(5,1):(3,7),(5,2):(3,8),(5,3):(4,6),(5,4):(4,7),(5,5):(4,8),(5,6):(5,6),(5,7):(5,7),(5,8):(5,8),
                         (6,0):(6,0),(6,1):(6,1),(6,2):(6,2),(6,3):(7,0),(6,4):(7,1),(6,5):(7,2),(6,6):(8,0),(6,7):(8,1),(6,8):(8,2),
                         (7,0):(6,3),(7,1):(6,4),(7,2):(6,5),(7,3):(7,3),(7,4):(7,4),(7,5):(7,5),(7,6):(8,3),(7,7):(8,4),(7,8):(8,5),
                         (8,0):(6,6),(8,1):(6,7),(8,2):(6,8),(8,3):(7,6),(8,4):(7,7),(8,5):(7,8),(8,6):(8,6),(8,7):(8,7),(8,8):(8,8)}
        temp_list = []
        all_index_append = []
        
        dict_for_storing_index = {}
        input_list = self.L3[:]
        
        for items in self.L3:
            for itm in items:
                temp_list.append(itm)

        temp2_list = self.L3[:]
        
        #print(temp2_list)

        frequency = dict((x,temp_list.count(x)) for x in temp_list)
        if 0 in frequency.keys():
            del frequency[0]
        sorted_frequency_dict = OrderedDict(sorted(frequency.items(), key=itemgetter(1),reverse = True))
        sorted_keys = sorted_frequency_dict.keys()
        #print('sorted_frequency_dict',sorted_frequency_dict)
        #print('sorted_keys---->',sorted_keys)
        for items1 in sorted_keys:
            loopin_value = sorted_frequency_dict[items1]
            #print('loopin_value------------------------------------------------------>',loopin_value)
            for g in range(loopin_value):
                for i in range(len(temp2_list)):
                    for j in range(len(temp2_list[i])):
                        if items1 == temp2_list[i][j]:
                            key = list(index_mapping.values())[list(index_mapping.keys()).index((i,j))]
                            i1 = key[0]
                            j1 = key[1]
                            for k in range(len(all_indexes)):
                                for m in range(len(all_indexes[k])):
                                    #if all_indexes[k][m] == (i1,j1):
                                    all_index_append.append(all_indexes[i1])
                                    for n in range(len(all_indexes)):
                                        for p in range(len(all_indexes[n])):
                                            if all_indexes[n][p][0] == i:
                                                all_index_append.append(all_indexes[n][p])
                                            if all_indexes[n][p][1] == j:
                                                all_index_append.append(all_indexes[n][p])

                b_list = []
                d_list = []
                #here
                    #print('all_index_append begin',all_index_append)
                #print('for ------------------------------------------------------->', items1)
                for itm in all_index_append:
                    if type(itm) is list:
                        for sm in itm:
                            b_list.append(sm)
                    elif type(itm) is tuple:
                        b_list.append(itm)
                b_set = set(b_list)
                #print('b_set',b_set)
                #print('len(b_set)',len(b_set))

                for items in all_indexes:
                    for itm in items:
                        if itm not in b_set:
                            d_list.append(itm)
                #print('dlist first',d_list)
                #print('len(d_list)',len(d_list))

                e_list = []
                for items in d_list:
                    ft = items[0]
                    sn = items[1]
                    for i in range(len(input_list)):
                        for j in range(len(input_list)):
                            if (ft,sn) == (i,j):
                                if input_list[i][j] != 0:
                                    e_list.append(items)
                for items in e_list:
                    if items in d_list:
                        d_list.remove(items)
                #print('after removing d_list', d_list)
                #print(' after removing len(d_list)',len(d_list))

                e = []
                d = []

                for i in range(len(all_indexes)):
                    for j in range(len(all_indexes[i])):
                        if all_indexes[i][j] in d_list:
                            d.append(all_indexes[i][j])
                    e.append(d)
                    d = []
                inserting_index = 0
                for items in e:
                    if len(items) == 1:
                        inserting_index = items[0]

                for i in range(len(temp2_list)):
                    for j in range(len(temp2_list[i])):
                        if type(inserting_index) is tuple:
                            if inserting_index == (i,j):
                                temp2_list[i][j] = items1

                #print('all_indexes after removing',all_indexes)

                #print('e_list',e_list)
                #print('len(e_list)',len(e_list))

                #print('e---->', e)
                #print('len(e)', len(e))
                #print(inserting_index)

                #print('at last temp 2 list', temp2_list)
                

                all_indexes = original_all_indexes[:]
                del all_index_append[:]





        a, b = os.path.splitext(self.filename)
        tex_file_content = r'''\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline
% Line 1'''
        
        bare_tex_file = open(a+'_forced.tex', 'w+')
        bare_tex_file.write(tex_file_content)
        bare_tex_file.write('\n')
        counter  = 0
        for i in range(9):
            for j in range(9):
                if self.L3[i][j] == 0:
                    bare_tex_file.write(r'\N{}{}{}{}{} ')
                    counter+=1
                else:
                    st = r'\N{}{}{}{}{' + str(temp2_list[i][j]) + '} '
                    bare_tex_file.write(st)
                    counter+=1
                if counter % 9 != 0:
                    bare_tex_file.write(r'& ')
                else:
                    if counter in (27,54,81) :
                        
                        bare_tex_file.write(r'\\ \hline\hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                    else:
                        
                        bare_tex_file.write(r'\\ \hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                if counter%3==0:
                    bare_tex_file.write('\n')
        last_content = r'''\end{tabular}
\end{center}

\end{document}'''
        bare_tex_file.write(last_content)

        self.L4 = temp2_list[:]

    def marked_tex_output(self):
        self.forced_tex_output()
        #print(self.L4)
        numbers = [1,2,3,4,5,6,7,8,9]
        colomnnumbers = list(map(list, zip(*self.L4)))
        prem = []
        #print('my l4 --->',self.L4)
        for i in range(len(self.L4)):
            for j in range(len(self.L4[i])):
                #for row
                if self.L4[i][j] == 0:
                    for k in range(len(self.L4[i])):
                        try:
                            if self.L4[i][k] != 0:
                                numbers.remove(self.L4[i][k])
                        except ValueError:
                            continue
                #for colomn
                    for m in range(len(colomnnumbers[j])):
                        try:
                            if colomnnumbers[j][m] != 0 :
                                numbers.remove(colomnnumbers[j][m])
                        except ValueError:
                            continue
                #for first box
                    if i <= 2 and j <=2:
                        for n in range(0,3):
                            for p in range(0,3):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for second box
                    elif i <= 2 and j > 2 and j <= 5:
                        for n in range(0,3):
                            for p in range(3,6):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for third box
                    elif i <= 2 and j > 5 and j <= 8:
                        for n in range(0,3):
                            for p in range(6,9):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for forth box
                    elif i > 2 and i <= 5 and j <= 2:
                        for n in range(3,6):
                            for p in range(0,3):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for fifth box
                    elif i > 2 and i <= 5 and j > 2 and j <= 5:
                        for n in range(3,6):
                            for p in range(3,6):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for sixth box
                    elif i > 2 and i <= 5 and j > 5 and j <= 8:
                        for n in range(3,6):
                            for p in range(6,9):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for seventh box
                    elif i > 5 and j <= 2:
                        for n in range(6,9):
                            for p in range(0,3):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for eighth box
                    elif i > 5 and j > 2 and j <= 5:
                        for n in range(6,9):
                            for p in range(3,6):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                #for ninth box
                    elif i > 5 and j > 5:
                        for n in range(6,9):
                            for p in range(6,9):
                                try:
                                    if self.L4[n][p] != 0:
                                        numbers.remove(self.L4[n][p])
                                except ValueError:
                                    continue
                prem.append(numbers)
                numbers = [1,2,3,4,5,6,7,8,9]

        list_without_zero = []
        for items in prem:
            if items != [1,2,3,4,5,6,7,8,9]:
                    list_without_zero.append(items)
                    list_without_zero_part2 = list_without_zero[:]

        a, b = os.path.splitext(self.filename)
        tex_file_content = r'''\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline
% Line 1'''
        
        bare_tex_file = open(a+'_marked.tex', 'w+')
        bare_tex_file.write(tex_file_content)
        bare_tex_file.write('\n')
        counter  = 0
        
        #print('list_without_zero',list_without_zero)
        #print('self. l4 -->',self.L4)
        for i in range(9):
            for j in range(9):
                if self.L4[i][j] == 0:
                    firstbox, secondbox, thirdbox, forthbox = '', '', '', ''
                    if 1 in list_without_zero[0] and 2 not in list_without_zero[0]:
                        firstbox = '1'
                    if 2 in list_without_zero[0] and 1 not in list_without_zero[0]:
                        firstbox = '2'
                    if 1 in list_without_zero[0] and 2 in list_without_zero[0]:
                        firstbox = '1 2'
                    if 3 in list_without_zero[0] and 4 not in list_without_zero[0]:
                        secondbox = '3'
                    if 4 in list_without_zero[0] and 3 not in list_without_zero[0]:
                        secondbox = '4'
                    if 3 in list_without_zero[0] and 4 in list_without_zero[0]:
                        secondbox = '3 4'
                    if 5 in list_without_zero[0] and 6 not in list_without_zero[0]:
                        thirdbox = '5'
                    if 6 in list_without_zero[0] and 5 not in list_without_zero[0]:
                        thirdbox = '6'
                    if 5 in list_without_zero[0] and 6 in list_without_zero[0]:
                        thirdbox = '5 6'
                    if 7 in list_without_zero[0] and 8 not in list_without_zero[0] and 9 not in list_without_zero[0]:
                        forthbox = '7'
                    if 8 in list_without_zero[0] and 7 not in list_without_zero[0] and 9 not in list_without_zero[0]:
                        forthbox = '8'
                    if 9 in list_without_zero[0] and 7 not in list_without_zero[0] and 8 not in list_without_zero[0]:
                        forthbox = '9'
                    if 7 in list_without_zero[0] and 8 in list_without_zero[0] and 9 not in list_without_zero[0]:
                        forthbox = '7 8'
                    if 8 in list_without_zero[0] and 9 in list_without_zero[0] and 7 not in list_without_zero[0]:
                        forthbox = '8 9'
                    if 7 in list_without_zero[0] and 9 in list_without_zero[0] and 8 not in list_without_zero[0]:
                        forthbox = '7 9'
                    if 7 in list_without_zero[0] and 8 in list_without_zero[0] and 9 in list_without_zero[0]:
                        forthbox = '7 8 9'
                    at = r'\N{'+firstbox+'}{'+secondbox+'}{'+thirdbox+'}{'+forthbox+'}{} '
                    bare_tex_file.write(at)
                    list_without_zero.pop(0)
                    counter+=1
                else:
                    st = r'\N{}{}{}{}{' + str(self.L4[i][j]) + '} '
                    bare_tex_file.write(st)
                    counter+=1
                if counter % 9 != 0:
                    bare_tex_file.write(r'& ')
                else:
                    if counter in (27,54,81) :
                        
                        bare_tex_file.write(r'\\ \hline\hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                    else:
                        
                        bare_tex_file.write(r'\\ \hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                if counter%3==0:
                    bare_tex_file.write('\n')
        last_content = r'''\end{tabular}
\end{center}

\end{document}'''
        bare_tex_file.write(last_content)
                
            
        self.premptive_Set = prem
        #print('premtive set all-->',prem)
        #print('without zero--->',list_without_zero)

    def worked_tex_output(self):
        self.marked_tex_output()
        #print('worked tex premptive',self.premptive_Set)
        my_comparing_list = copy.deepcopy(self.premptive_Set)
        #print('length',len(self.premptive_Set))
        all_indexes = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)], [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
                       [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)], [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)], [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
                       [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)], [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)], [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]]
        
        index_mapping = {(0,0):(0,0),(0,1):(0,1),(0,2):(0,2),(0,3):(1,0),(0,4):(1,1),(0,5):(1,2),(0,6):(2,0),(0,7):(2,1),(0,8):(2,2),
                         (1,0):(0,3),(1,1):(0,4),(1,2):(0,5),(1,3):(1,3),(1,4):(1,4),(1,5):(1,5),(1,6):(2,3),(1,7):(2,4),(1,8):(2,5),
                         (2,0):(0,6),(2,1):(0,7),(2,2):(0,8),(2,3):(1,6),(2,4):(1,7),(2,5):(1,8),(2,6):(2,6),(2,7):(2,7),(2,8):(2,8),
                         (3,0):(3,0),(3,1):(3,1),(3,2):(3,2),(3,3):(4,0),(3,4):(4,1),(3,5):(4,2),(3,6):(5,0),(3,7):(5,1),(3,8):(5,2),
                         (4,0):(3,3),(4,1):(3,4),(4,2):(3,5),(4,3):(4,3),(4,4):(4,4),(4,5):(4,5),(4,6):(5,3),(4,7):(5,4),(4,8):(5,5),
                         (5,0):(3,6),(5,1):(3,7),(5,2):(3,8),(5,3):(4,6),(5,4):(4,7),(5,5):(4,8),(5,6):(5,6),(5,7):(5,7),(5,8):(5,8),
                         (6,0):(6,0),(6,1):(6,1),(6,2):(6,2),(6,3):(7,0),(6,4):(7,1),(6,5):(7,2),(6,6):(8,0),(6,7):(8,1),(6,8):(8,2),
                         (7,0):(6,3),(7,1):(6,4),(7,2):(6,5),(7,3):(7,3),(7,4):(7,4),(7,5):(7,5),(7,6):(8,3),(7,7):(8,4),(7,8):(8,5),
                         (8,0):(6,6),(8,1):(6,7),(8,2):(6,8),(8,3):(7,6),(8,4):(7,7),(8,5):(7,8),(8,6):(8,6),(8,7):(8,7),(8,8):(8,8)}
        
        yourlistrow = []
        
        final_list_row = []
        #final_list_changing = []
        for i in range(0,81):
            yourlistrow.append(self.premptive_Set[i])
            if (i + 1) % 9 == 0:
                final_list_row.append(yourlistrow)
                yourlistrow = []
        final_list_colomn = list(map(list, zip(*final_list_row)))
        #print('yourlistcolomn---->',final_list_colomn)

        #for making copy of 3d list
        final_list_changing = copy.deepcopy(final_list_row)
        temporary = copy.deepcopy(final_list_changing)
        

        #print('final list row',final_list_row)
        #print(len(final_list_row))
        mylist = []
        Box,Box1,Box2 = [],[],[]
        final_list_box = []
        merged = []
        merged1 = []
        merged2 = []
        for i in range(0,9):
            
            for j in range(0,9):
                if j < 3:
                    Box.append(final_list_row[i][j])
                elif j < 6:
                    Box1.append(final_list_row[i][j])
                else:
                    Box2.append(final_list_row[i][j])
            if i== 2 or i==5 or i == 8:
                    final_list_box.append(Box)
                    final_list_box.append(Box1)
                    final_list_box.append(Box2)
                    Box = []
                    Box1 = []
                    Box2 = []
        #print('final list box', final_list_box)
        cycle = 0
        while cycle >= 0:
            cycle += 1
            for i in range(len(final_list_row)):
                for j in range(len(final_list_row[i])):
                    #changed here
                    mylist = []
                    if final_list_row[i][j] != [1,2,3,4,5,6,7,8,9] :
                        #for box number
                        for p in range(len(all_indexes)):
                            for q in range(len(all_indexes[p])):
                                if all_indexes[p][q] == (i,j):
                                    boxnumber = p
                                    boxnumber1 = q
                        temp = (final_list_row[i][j])
                        #checking set in row
                        for k in range(9):
                            if set(final_list_row[i][k]) <= set(temp) and len(final_list_row[i][k]) != 1:
                                mylist.append(final_list_row[i][k])
                        if len(temp) != len(mylist):
                            mylist = []
                        else:
                            #operation
                            for t in range(len(final_list_row[i])):
                                if final_list_row[i][t] not in mylist and final_list_row[i][t] != [1,2,3,4,5,6,7,8,9] :
                                    for items in temp:
                                        if items in final_list_row[i][t] :
                                            final_list_row[i][t].remove(items)
                                            final_list_changing[i][t].remove(items)
                                            #final_list_colomn[t][i].remove(items)
                                            #checking box number to cut set from box list.
                                            #for x in range(len(all_indexes)):
                                            #    for y in range(len(all_indexes[x])):
                                            #        if all_indexes[x][y] == (i,t):
                                            #            boxnumber3 = x
                                            #            boxnumber4 = y

                                            #final_list_box[boxnumber3][boxnumber4].remove(items)
                        pass
                        #cutting from row, other place if we find any single element in list
                        count = -1
                        for x in final_list_row[i]:
                            count += 1
                            if len(x) == 1:
                                Singleton = x[0]
                                for r in range(len(all_indexes)):
                                    for s in range(len(all_indexes[r])):
                                        if all_indexes[r][s] == (i, count):
                                            boxnumber3 = r
                                            boxnumber4 = s
                                            break
                                for y in range(9):
                                    if Singleton in final_list_box[boxnumber3][y] and final_list_box[boxnumber3][y] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber3][y] != [Singleton] :
                                        final_list_box[boxnumber3][y].remove(Singleton)
                                        for r in range(len(all_indexes)):
                                            for s in range(len(all_indexes[r])):
                                                if all_indexes[r][s] == (boxnumber3, y):
                                                    boxnumber5 = r
                                                    boxnumber6 = s
                                                    break
                                        final_list_changing[boxnumber5][boxnumber6].remove(Singleton)

                                    #if Singleton in final_list_changing[y][j] and final_list_changing[y][j] != [1,2,3,4,5,6,7,8,9] and final_list_changing[y][j] != [Singleton]:
                                    #    final_list_changing[y][j].remove(Singleton)

                                    if Singleton in final_list_row[i][y] and final_list_row[i][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[i][y] != [Singleton] :
                                        final_list_row[i][y].remove(Singleton)
                                        if Singleton in final_list_changing[i][y] and final_list_changing[i][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[i][y] != [Singleton]:
                                            final_list_changing[i][y].remove(Singleton)

                                    if Singleton in final_list_colomn[count][y] and final_list_colomn[count][y] != [1,2,3,4,5,6,7,8,9] and final_list_colomn[count][y] != [Singleton]:
                                        final_list_colomn[count][y].remove(Singleton)
                                        #changed here
                                        if Singleton in final_list_changing[y][count] and final_list_changing[y][count] != [1,2,3,4,5,6,7,8,9] and final_list_changing[y][count] != [Singleton]:
                                            final_list_changing[y][count].remove(Singleton)
                                    for r in range(len(all_indexes)):
                                         for s in range(len(all_indexes[r])):
                                            if all_indexes[r][s] == (i,y):
                                                boxnumber9 = r
                                                boxnumber10 = s
                                    if Singleton in final_list_box[boxnumber9][boxnumber10] and final_list_box[boxnumber9][boxnumber10] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber9][boxnumber10] != [Singleton] :
                                        final_list_box[boxnumber9][boxnumber10].remove(Singleton)

                        #checking singleton in row
                        for a in range(9):
                            if final_list_row[i][a] != [1,2,3,4,5,6,7,8,9] :
                                merged.append(final_list_row[i][a])
                        merged_rows = list(itertools.chain(*merged))
                    
                        for items in merged_rows:
                            if merged_rows.count(items) == 1:
                                for b in range(len(final_list_row[i])):
                                    if items in final_list_row[i][b] and final_list_row[i][b] != [1,2,3,4,5,6,7,8,9]:
                                        j_index = b
                                        final_list_row[i][b] = [items]
                                        final_list_changing[i][b] = [items]
                                        final_list_colomn[b][i] = [items]

                                        for x in range(len(all_indexes)):
                                             for y in range(len(all_indexes[x])):
                                                if all_indexes[x][y] == (i,b):
                                                    boxnumber3 = x
                                                    boxnumber4 = y
                                        final_list_box[boxnumber3][boxnumber4] = [items]

                        #print('my first merged list',merged_rows)

                        merged = []
                        merged_rows = []


                        #cutting after finding singleton ---- removing from box and colomn
                        count = -1
                        for x in final_list_row[i]:
                            count += 1
                            if len(x) == 1:
                                Singleton = x[0]
                                for r in range(len(all_indexes)):
                                    for s in range(len(all_indexes[r])):
                                        if all_indexes[r][s] == (i, count):
                                            boxnumber3 = r
                                            boxnumber4 = s
                                            break
                                for y in range(9):
                                    if Singleton in final_list_box[boxnumber3][y] and final_list_box[boxnumber3][y] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber3][y] != [Singleton] :
                                        final_list_box[boxnumber3][y].remove(Singleton)
                                        for r in range(len(all_indexes)):
                                            for s in range(len(all_indexes[r])):
                                                if all_indexes[r][s] == (boxnumber3, y):
                                                    boxnumber5 = r
                                                    boxnumber6 = s
                                                    break
                                        final_list_changing[boxnumber5][boxnumber6].remove(Singleton)

                                    #if Singleton in final_list_changing[y][j] and final_list_changing[y][j] != [1,2,3,4,5,6,7,8,9] and final_list_changing[y][j] != [Singleton]:
                                    #    final_list_changing[y][j].remove(Singleton)

                                    if Singleton in final_list_row[i][y] and final_list_row[i][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[i][y] != [Singleton] :
                                        final_list_row[i][y].remove(Singleton)
                                        if Singleton in final_list_changing[i][y] and final_list_changing[i][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[i][y] != [Singleton]:
                                            final_list_changing[i][y].remove(Singleton)

                                    if Singleton in final_list_colomn[count][y] and final_list_colomn[count][y] != [1,2,3,4,5,6,7,8,9] and final_list_colomn[count][y] != [Singleton]:
                                        final_list_colomn[count][y].remove(Singleton)
                                    for r in range(len(all_indexes)):
                                         for s in range(len(all_indexes[r])):
                                            if all_indexes[r][s] == (i,y):
                                                boxnumber9 = r
                                                boxnumber10 = s
                                    if Singleton in final_list_box[boxnumber9][boxnumber10] and final_list_box[boxnumber9][boxnumber10] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber9][boxnumber10] != [Singleton] :
                                        final_list_box[boxnumber9][boxnumber10].remove(Singleton)


                        #checking set in colomn
                        #changed here
                        mylist = []
                        for m in range(9):
                            if set(final_list_colomn[j][m]) <= set(temp) and len(final_list_colomn[j][m]) != 1:
                                mylist.append(final_list_colomn[j][m])
                        if len(temp) != len(mylist) :
                            mylist = []
                        else:
                            #operation
                            for s in range(len(final_list_colomn[j])):
                                if final_list_colomn[j][s] not in mylist and final_list_colomn[j][s] != [1,2,3,4,5,6,7,8,9] :
                                    for items in temp:
                                        if items in final_list_colomn[j][s] :
                                            final_list_colomn[j][s].remove(items)
                                            final_list_changing[s][j].remove(items)
                                            #final_list_row[s][j].remove(items)

                                            #for x in range(len(all_indexes)):
                                            #    for y in range(len(all_indexes[x])):
                                            #        if all_indexes[x][y] == (s,j):
                                            #            boxnumber3 = x
                                            #            boxnumber4 = y

                                            #final_list_box[boxnumber3][boxnumber4].remove(items)


                        #cutting from colomn, other place if we find any single element in list
                        count = -1
                        for x in final_list_colomn[j]:
                            count +=1
                            if len(x) == 1:
                                Singleton = x[0]
                                for r in range(len(all_indexes)):
                                    for s in range(len(all_indexes[r])):
                                        if all_indexes[r][s] == (count,j):
                                            boxnumber3 = r
                                            boxnumber4 = s
                                            break

                                for a in range(9):
                                    if Singleton in final_list_box[boxnumber3][a] and final_list_box[boxnumber3][a] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber3][a] != [Singleton] :
                                    
                                        final_list_box[boxnumber3][a].remove(Singleton)

                                        for r in range(len(all_indexes)):
                                            for s in range(len(all_indexes[r])):
                                                if all_indexes[r][s] == (boxnumber3,a):
                                                    boxnumber7 = r
                                                    boxnumber8 = s
                                                    break
                                                    #yaad rakhiyo babua
                                        final_list_changing[boxnumber7][boxnumber8].remove(Singleton)
                                for y in range(9):
                                
                                    if Singleton in final_list_row[count][y] and final_list_row[count][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[count][y] != [Singleton] :
                                        final_list_row[count][y].remove(Singleton)
                                    if Singleton in final_list_changing[count][y] and final_list_changing[count][y] != [1,2,3,4,5,6,7,8,9] and final_list_changing[count][y] != [Singleton] :
                                        final_list_changing[count][y].remove(Singleton)

                                    if Singleton in final_list_colomn[j][y] and final_list_colomn[j][y] != [1,2,3,4,5,6,7,8,9] and final_list_colomn[j][y] != [Singleton]:
                                        final_list_colomn[j][y].remove(Singleton)
                                        if Singleton in final_list_changing[y][j] and final_list_changing[y][j] != [1,2,3,4,5,6,7,8,9] and final_list_changing[y][j] != [Singleton]:
                                            final_list_changing[y][j].remove(Singleton)

                                    for r in range(len(all_indexes)):
                                        for s in range(len(all_indexes[r])):
                                            if all_indexes[r][s] == (count,y):
                                                boxnumber9 = r
                                                boxnumber10 = s
                                    if Singleton in final_list_box[boxnumber9][boxnumber10] and final_list_box[boxnumber9][boxnumber10] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber9][boxnumber10] != [Singleton] :
                                        final_list_box[boxnumber9][boxnumber10].remove(Singleton)


                        #checking singleton in colomn
                        for d in range(9):
                            if final_list_colomn[j][d] != [1,2,3,4,5,6,7,8,9] :
                                merged1.append(final_list_colomn[j][d])
                        merged_colomn = list(itertools.chain(*merged1))
                        for items in merged_colomn:
                            if merged_colomn.count(items) == 1:
                                for e in range(len(final_list_colomn[j])):
                                    if items in final_list_colomn[j][e] and final_list_colomn[j][e] != [1,2,3,4,5,6,7,8,9] :
                                        i_index = e
                                        final_list_colomn[j][e] = [items]
                                        final_list_changing[e][j] = [items]
                                        final_list_row[e][j] = [items]

                                        for a in range(len(all_indexes)):
                                            for b in range(len(all_indexes[a])):
                                                if all_indexes[a][b] == (e,j):
                                                    boxnumber3 = a
                                                    boxnumber4 = b
                                        final_list_box[boxnumber3][boxnumber4] = [items]

                        merged1 = []
                        merged_colomn = []
                        #cutting singleton from row and box
                        count = -1
                        for x in final_list_colomn[j]:
                            count +=1
                            if len(x) == 1:
                                Singleton = x[0]
                                for r in range(len(all_indexes)):
                                    for s in range(len(all_indexes[r])):
                                        if all_indexes[r][s] == (count,j):
                                            boxnumber3 = r
                                            boxnumber4 = s
                                            break

                                for a in range(9):
                                    if Singleton in final_list_box[boxnumber3][a] and final_list_box[boxnumber3][a] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber3][a] != [Singleton] :
                                    
                                        final_list_box[boxnumber3][a].remove(Singleton)

                                        for r in range(len(all_indexes)):
                                            for s in range(len(all_indexes[r])):
                                                if all_indexes[r][s] == (boxnumber3,a):
                                                    boxnumber7 = r
                                                    boxnumber8 = s
                                                    break
                                                    #yaad rakhiyo babua
                                        final_list_changing[boxnumber7][boxnumber8].remove(Singleton)
                                for y in range(9):
                                
                                    if Singleton in final_list_row[count][y] and final_list_row[count][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[count][y] != [Singleton] :
                                        final_list_row[count][y].remove(Singleton)
                                    if Singleton in final_list_changing[count][y] and final_list_changing[count][y] != [1,2,3,4,5,6,7,8,9] and final_list_changing[count][y] != [Singleton] :
                                        final_list_changing[count][y].remove(Singleton)

                                    if Singleton in final_list_colomn[j][y] and final_list_colomn[j][y] != [1,2,3,4,5,6,7,8,9] and final_list_colomn[j][y] != [Singleton]:
                                        final_list_colomn[j][y].remove(Singleton)
                                        if Singleton in final_list_changing[y][j] and final_list_changing[y][j] != [1,2,3,4,5,6,7,8,9] and final_list_changing[y][j] != [Singleton]:
                                            final_list_changing[y][j].remove(Singleton)

                                    for r in range(len(all_indexes)):
                                        for s in range(len(all_indexes[r])):
                                            if all_indexes[r][s] == (count,y):
                                                boxnumber9 = r
                                                boxnumber10 = s
                                    if Singleton in final_list_box[boxnumber9][boxnumber10] and final_list_box[boxnumber9][boxnumber10] != [1,2,3,4,5,6,7,8,9] and final_list_box[boxnumber9][boxnumber10] != [Singleton] :
                                        final_list_box[boxnumber9][boxnumber10].remove(Singleton)



                        pass
                        #checking set in boxes
                        #changed here
                        mylist = []
                        for n in range(9):
                            if set(final_list_box[boxnumber][n]) <= set(temp) and len(final_list_box[boxnumber][n]) != 1:
                                mylist.append(final_list_box[boxnumber][n])
                        if len(temp) != len(mylist):
                            mylist = []
                        else:
                            #operation
                            for r in range(len(final_list_box[boxnumber])):
                                if final_list_box[boxnumber][r] not in mylist and final_list_box[boxnumber][r] != [1,2,3,4,5,6,7,8,9] :
                                    for items in temp:
                                        if items in final_list_box[boxnumber][r] :
                                            final_list_box[boxnumber][r].remove(items)

                                            value = list(index_mapping.keys())[list(index_mapping.values()).index((boxnumber,r))]
                                            i1 = value[0]
                                            j1 = value[1]
                                            #final_list_row[i1][j1].remove(items)
                                            #final_list_colomn[j1][i1].remove(items)
                                            #changed here
                                            #if items in final_list_changing[i1][j1] :
                                            #print('items',items)
                                            #print('values', i1,j1,boxnumber,r)
                                            #print('final_list_changing[i1][j1]',final_list_changing[i1][j1])
                                            final_list_changing[i1][j1].remove(items)
                        #cutting from box, other place if we find any single element in list
                        count2 = -1
                        for x in final_list_box[boxnumber]:
                            count2 += 1
                            if len(x) == 1:
                                Singleton = x[0]

                                for r in range(len(all_indexes)):
                                    for s in range(len(all_indexes[r])):
                                        if all_indexes[r][s] == (boxnumber,count2):
                                            boxnumber3 = r
                                            boxnumber4 = s

                                for y in range(9):
                                    if Singleton in final_list_row[boxnumber3][y] and final_list_row[boxnumber3][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[boxnumber3][y] != [Singleton]:
                                        final_list_row[boxnumber3][y].remove(Singleton)
                                        final_list_changing[boxnumber3][y].remove(Singleton)
                                    if Singleton in final_list_colomn[y][boxnumber3] and final_list_colomn[y][boxnumber3] != [1,2,3,4,5,6,7,8,9] and final_list_colomn[y][boxnumber3] != [Singleton]:
                                        final_list_colomn[y][boxnumber3].remove(Singleton)
                                        final_list_changing[boxnumber3][y].remove(Singleton)
                        #checking singleton in box
                        for f in range(9):
                            if final_list_box[boxnumber][f] != [1,2,3,4,5,6,7,8,9]:
                                merged2.append(final_list_box[boxnumber][f])
                        merged_box = list(itertools.chain(*merged2))
                        for items in merged_box:
                            if merged_box.count(items) == 1:
                                for g in range(len(final_list_box[boxnumber])):
                                    if items in final_list_box[boxnumber][g] and final_list_box[boxnumber][g] != [1,2,3,4,5,6,7,8,9] :
                                        j_index = g
                                        final_list_box[boxnumber][g] = [items]
                                        key = list(index_mapping.values())[list(index_mapping.keys()).index((boxnumber,g))]
                                        i2 = key[0]
                                        j2 = key[1]
                                        final_list_row[i2][j2]  = [items]
                                        final_list_colomn[j2][i2] = [items]
                                        final_list_changing[i2][j2] = [items]
                        merged2 = []
                        merged_box = []
                        #cutting singleton from colomn and row
                        count2 = -1
                        for x in final_list_box[boxnumber]:
                            count2 += 1
                            if len(x) == 1:
                                Singleton = x[0]

                                for r in range(len(all_indexes)):
                                    for s in range(len(all_indexes[r])):
                                        if all_indexes[r][s] == (boxnumber,count2):
                                            boxnumber3 = r
                                            boxnumber4 = s

                                for y in range(9):
                                    if Singleton in final_list_row[boxnumber3][y] and final_list_row[boxnumber3][y] != [1,2,3,4,5,6,7,8,9] and final_list_row[boxnumber3][y] != [Singleton]:
                                        final_list_row[boxnumber3][y].remove(Singleton)
                                        final_list_changing[boxnumber3][y].remove(Singleton)
                                    if Singleton in final_list_colomn[y][boxnumber3] and final_list_colomn[y][boxnumber3] != [1,2,3,4,5,6,7,8,9] and final_list_colomn[y][boxnumber3] != [Singleton]:
                                        final_list_colomn[y][boxnumber3].remove(Singleton)
                                        final_list_changing[boxnumber3][y].remove(Singleton)
                        merged2 = []
                        merged_box = []
                   
                    #print(i,j)
            Difference = [x for x in temporary if not x in final_list_changing]
            #print('cycle',cycle)
            if len(Difference) == 0:
                cycle = -1
            temporary=copy.deepcopy(final_list_changing)
        #print('final_list_changing---> ',final_list_changing)

        final_list = copy.deepcopy(final_list_changing)
        for i in range(9):
            for j in range(9):
                if final_list[i][j] == [1,2,3,4,5,6,7,8,9] :
                    final_list[i][j] = self.L4[i][j]
        #print('\n\n')
        #print('final_list----->',final_list)
                
        #print('my_comparing_list=============>',my_comparing_list)
        a, b = os.path.splitext(self.filename)
        tex_file_content = r'''\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline
% Line 1'''
        
        bare_tex_file = open(a+'_worked.tex', 'w+')
        bare_tex_file.write(tex_file_content)
        bare_tex_file.write('\n')
        counter  = 0
        counter1=-1
        #print('list_without_zero',list_without_zero)
        #print('self. l4 -->',self.L4)
        for i in range(9):
            for j in range(9):
                at = []
                counter1+=1
                if type(final_list[i][j]) is list and len(final_list[i][j]) != 1 :
                    counter+=1
                    at.append(r'\N')  
                    flag = -1
                    counter2 = 0
                    for items in my_comparing_list[counter1]:
                        if items ==1 or items == 2:
                            counter2+=1
                            flag = 0
                        if items in final_list[i][j] and items in [1,2]:
                            if 1 == items and 2 not in final_list[i][j] :
                                #firstbox = '1'
                                at.append('{1')
                            elif 2 == items and 1 not in final_list[i][j]:
                                #firstbox = '2'
                                at.append('{2')
                            elif 1 == items and 2 in final_list[i][j]:
                                #firstbox = '1 2'   #({cancel 1 cancel 2)
                                at.append('{1 2')
                        elif items in my_comparing_list[counter1] and items in [1,2]:
                            if counter2 == 1:
                                at.append('{\cancel{'+str(items)+'}')
                            else:
                                at.append(' \cancel{'+str(items)+'}')   
                    if flag == -1:
                        at.append('{')
                    at.append('}')

                                
                            #else:
                                #{}
                    flag = -1
                    counter2 = 0
                    for items in my_comparing_list[counter1]:
                        if items in [3,4]:
                            counter2+=1
                            flag = 0
                        if items in final_list[i][j] and items in [3,4]:
                        #    at.append('{}')
                            if 3 == items and 4 not in final_list[i][j]:
                                #secondbox = '3'     cancel
                                at.append('{3')
                            elif 4 == items and 3 not in final_list[i][j]:
                                #secondbox = '4'
                                at.append('{4')
                            elif 3 == items and 4 in final_list[i][j]:
                              #  secondbox = '3 4'
                              at.append('{3 4')
                        elif items in my_comparing_list[counter1] and items in [3,4]:
                             if counter2 == 1:
                                at.append('{\cancel{'+str(items)+'}')
                             else:
                                at.append(' \cancel{'+str(items)+'}')                     
                    if flag == -1:
                        at.append('{')
                    at.append('}')
                            #else:
                                #{}
                            #    at.append('{}')
                    flag = -1
                    counter2 = 0
                    for items in my_comparing_list[counter1]:
                        if items in [5,6]:
                            counter2+=1
                            flag = 0
                        if items in final_list[i][j] and items in [5,6]:
                            if 5 == items and 6 not in final_list[i][j]:
                                #thirdbox = '5'
                                at.append('{5')
                            elif 6 == items and 5 not in final_list[i][j]:
                                #thirdbox = '6'
                                at.append('{6')
                            elif 5 == items and 6 in final_list[i][j]:
                              #  thirdbox = '5 6'
                                at.append('{5 6')
                        elif items in my_comparing_list[counter1] and items in [5,6]:
                            if counter2 == 1:
                                at.append('{\cancel{'+str(items)+'}')
                            else:
                                at.append(' \cancel{'+str(items)+'}')     
                    if flag == -1:
                        at.append('{')
                    at.append('}')

                    flag = -1
                    counter2 = 0
                    for items in my_comparing_list[counter1]:
                        if items in [7,8,9]:
                            counter2 +=1
                            flag = 0
                        if items in final_list[i][j] and items in [7,8,9]:
                            #else:
                            #    at.append('{}')
                            if 7 == items and 8 not in final_list[i][j] and 9 not in final_list[i][j]:
                                #forthbox = '7'
                                at.append('{7')
                            elif 8 == items and 7 not in final_list[i][j] and 9 not in final_list[i][j]:
                                #forthbox = '8'
                                at.append('{8')
                            elif 9 == items and 7 not in final_list[i][j] and 8 not in final_list[i][j]:
                                #forthbox = '9'
                                at.append('{9')
                            elif 7 == items and 8 in final_list[i][j] and 9 not in final_list[i][j]:
                               # forthbox = '7 8'
                                at.append('{7 8')
                            elif 8 == items and 9 in final_list[i][j] and 7 not in final_list[i][j]:
                                #forthbox = '8 9'
                                at.append('{8 9')
                            elif 7 == items and 9 in final_list[i][j] and 8 not in final_list[i][j]:
                                #forthbox = '7 9'
                                at.append('{7 9')
                            elif 7 == items and 8 in final_list[i][j] and 9 in final_list[i][j]:
                                #forthbox = '7 8 9'
                                at.append('{7 8 9')
                        elif items in my_comparing_list[counter1] and items in [7,8,9]:
                            if counter2 == 1:
                                at.append('{\cancel{'+str(items)+'}')
                            else:
                                at.append(' \cancel{'+str(items)+'}')     
   
                    if flag == -1:
                        at.append('{')
                    at.append('}')
                     
                           # at = r'\N{\cancel{'+firstbox+'}}{\cancel{'+secondbox+'}}{\cancel{'+thirdbox+'}}{\cancel{'+forthbox+'}}{'+str(final_list[i][j][0])+'} '
                        #at.append('}')
                    #print(at)
                    at.append('{} ')
                    
                    for x in range(len(at)):
                        bare_tex_file.write(at[x])
                        



                    #list_without_zero.pop(0)
                    #counter+=1
                elif type(final_list[i][j]) is not int and len(final_list[i][j]) == 1:
                    at.append(r'\N')                   
                    if 1 in my_comparing_list[counter1] and 2 not in my_comparing_list[counter1]:
                        #firstbox = '1'
                        at.append('{\cancel{1}}')
                    elif 2 in my_comparing_list[counter1] and 1 not in my_comparing_list[counter1]:
                        #firstbox = '2'
                        at.append('{\cancel{2}}')
                    elif 1 in my_comparing_list[counter1] and 2 in my_comparing_list[counter1]:
                        #firstbox = '1 2'   #({cancel 1 cancel 2)
                        at.append('{\cancel{1} \cancel{2}}')
                    else:
                        #{}
                        at.append('{}')
                    if 3 in my_comparing_list[counter1] and 4 not in my_comparing_list[counter1]:
                        #secondbox = '3'     cancel
                        at.append('{\cancel{3}}')
                    elif 4 in my_comparing_list[counter1] and 3 not in my_comparing_list[counter1]:
                        #secondbox = '4'
                        at.append('{\cancel{4}}')
                    elif 3 in my_comparing_list[counter1] and 4 in my_comparing_list[counter1]:
                      #  secondbox = '3 4'
                      at.append('{\cancel{3} \cancel{4}}')
                    else:
                        #{}
                        at.append('{}')
                    if 5 in my_comparing_list[counter1] and 6 not in my_comparing_list[counter1]:
                        #thirdbox = '5'
                        at.append('{\cancel{5}}')
                    elif 6 in my_comparing_list[counter1] and 5 not in my_comparing_list[counter1]:
                        #thirdbox = '6'
                        at.append('{\cancel{6}}')
                    elif 5 in my_comparing_list[counter1] and 6 in my_comparing_list[counter1]:
                      #  thirdbox = '5 6'
                        at.append('{\cancel{5} \cancel{6}}')
                    else:
                        at.append('{}')
                    if 7 in my_comparing_list[counter1] and 8 not in my_comparing_list[counter1] and 9 not in my_comparing_list[counter1]:
                        #forthbox = '7'
                        at.append('{\cancel{7}}')
                    elif 8 in my_comparing_list[counter1] and 7 not in my_comparing_list[counter1] and 9 not in my_comparing_list[counter1]:
                        #forthbox = '8'
                        at.append('{\cancel{8}}')
                    elif 9 in my_comparing_list[counter1] and 7 not in my_comparing_list[counter1] and 8 not in my_comparing_list[counter1]:
                        #forthbox = '9'
                        at.append('{\cancel{9}}')
                    elif 7 in my_comparing_list[counter1] and 8 in my_comparing_list[counter1] and 9 not in my_comparing_list[counter1]:
                       # forthbox = '7 8'
                        at.append('{\cancel{7} \cancel{8}}')
                    elif 8 in my_comparing_list[counter1] and 9 in my_comparing_list[counter1] and 7 not in my_comparing_list[counter1]:
                        #forthbox = '8 9'
                        at.append('{\cancel{8} \cancel{9}}')
                    elif 7 in my_comparing_list[counter1] and 9 in my_comparing_list[counter1] and 8 not in my_comparing_list[counter1]:
                        #forthbox = '7 9'
                        at.append('{\cancel{7} \cancel{9}}')
                    elif 7 in my_comparing_list[counter1] and 8 in my_comparing_list[counter1] and 9 in my_comparing_list[counter1]:
                        #forthbox = '7 8 9'
                        at.append('{\cancel{7} \cancel{8} \cancel{9}}')
                    else:
                        at.append('{}')
                    at.append('{'+str(final_list[i][j][0])+'} ')
                   # at = r'\N{\cancel{'+firstbox+'}}{\cancel{'+secondbox+'}}{\cancel{'+thirdbox+'}}{\cancel{'+forthbox+'}}{'+str(final_list[i][j][0])+'} '
                    #print(at)
                    
                    for x in range(len(at)):
                        bare_tex_file.write(at[x])
                    

                    counter+=1
                else:
                    st = r'\N{}{}{}{}{' + str(final_list[i][j]) + '} '
                    bare_tex_file.write(st)
                    counter+=1
                if counter % 9 != 0:
                    bare_tex_file.write(r'& ')
                else:
                    if counter in (27,54,81) :
                        
                        bare_tex_file.write(r'\\ \hline\hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                    else:
                        
                        bare_tex_file.write(r'\\ \hline')
                        
                        if i <= 7:
                            bare_tex_file.write('\n\n')
                            st1 = r'% Line ' + str(i+2)
                            bare_tex_file.write(st1)
                if counter%3==0:
                    bare_tex_file.write('\n')
        last_content = r'''\end{tabular}
\end{center}

\end{document}'''
        bare_tex_file.write(last_content)

        pass



#a = Sudoku('sudoku_5.txt')
#a.forced_tex_output()
#a.marked_tex_output()
#a.worked_tex_output()
