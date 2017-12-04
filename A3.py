# Insert your code here
import re
import itertools
import sys
from collections import defaultdict
import operator

try:
    string_of_letters = (input("Enter between 3 and 10 lowercase letters: "))
    if bool(re.search(r'\d', str(string_of_letters))) == True :
        raise ValueError
    elif string_of_letters.islower() == False:
        raise ValueError
    elif len(string_of_letters.replace(" ", "")) < 3:
        raise ValueError
    elif len(string_of_letters.replace(" ", "")) > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()
#List_of_all_words = []
matched_words = []
set_of_matched_words = []
sum_of_words = []
sum = 0
i = 1
List_of_all_words = {}
with open('wordsEn.txt','r') as words:
	for items in words:
		List_of_all_words[items.strip('\n')] = 1
		#List_of_all_words.append(items.strip('\n'))

#print(List_of_all_words)
words_value = {'a':2,'b':5,'c':4,'d':4,'e':1,'f':6,'g':5,'h':5,'i':1,'j':7,'k':6,'l':3,'m':5,'n':2,'o':3,'p':5,'q':7,'r':2,'s':1,'t':2,'u':4,'v':6,'w':6,'x':7,'y':5,'z':7}

list_of_all_generated_words = []
#if string_of_letters.islower() and bool(re.search(r'\d', string_of_letters)) == False and len(string_of_letters) >=3 and len(string_of_letters.replace(" ", "")) <= 10:
#	print('done')
stripped_string = str(string_of_letters).replace(" ", "")
for i in range(len(stripped_string), 0,-1):
	a = [''.join(p) for p in itertools.permutations(stripped_string,i)]
	list_of_all_generated_words=list_of_all_generated_words+a
	#while i<=len(stripped_string):
	#	it = itertools.permutations(stripped_string,i)
	#	for y in it:
	#		list_of_all_generated_words.append("".join(y))
	#	i+=1
list_of_all_generated_words1 = set(list_of_all_generated_words)
for items in list_of_all_generated_words1:
	if items in List_of_all_words:
		matched_words.append(items)
set_of_sorted_matched_words = sorted(list(set(matched_words)))
for items in set_of_sorted_matched_words:
	for i in range(len(items)):
		letter = items[i]
		sum = sum + words_value.get(letter)
	sum_of_words.append(sum)
	sum = 0
	if len(sum_of_words)>0:
		max_ele = max(sum_of_words)
mydict = defaultdict(list)
list1 = defaultdict(list)
list2 = []
#mylastdict = defaultdict(list)
for i in range(len(set_of_sorted_matched_words)):
	for j in range(i,len(sum_of_words)):
		mydict[set_of_sorted_matched_words[i]].append(sum_of_words[j])
		break
mylastdict = sorted(mydict.items(), key=operator.itemgetter(1))
for i in range(len(mylastdict)):
	for j in range(len(mylastdict[i])):
		if max_ele == ((mylastdict[i])[1])[0]:
			list1[(mylastdict[i])[0]].append(((mylastdict[i])[1])[0])
			break
if len(list1) == 1:
	print(f'The highest score is {max_ele}.')
	for word, sum in list1.items():
		if max_ele in sum:
			#print(word)
			print(f'The highest scoring word is {word}')
elif len(list1) == 0:
	print('No word is built from some of those letters.')
else:
	print(f'The highest score is {max_ele}.')
	for word, sum in list1.items():
		if max_ele in sum:
			list2.append(word)
	print(f'The highest scoring words are, in alphabetical order:')
	for items in list2:
		#print('\t')
		print('   ',items)
	#print(f'words is {word}')
#print('stripped string--->',stripped_string)
#print('list_of_all_generated_words--->',list_of_all_generated_words)
#print(re.search(r'\d', inputString))
#print('string_of_letters',string_of_letters)
#print('set of sorted matched words--->',set_of_sorted_matched_words)
#print('sum of words', sum_of_words)
#print('dict of sum and words--->',mydict)
#print('my last dict--->',mylastdict)
#print(max_ele)
#print(list2)
