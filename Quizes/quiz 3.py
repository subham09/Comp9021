# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by Subham Anand for COMP9021

import sys
import os
import csv
from collections import defaultdict
import operator

Con_Values=[]
agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []

year_1, year_2 = None, None

##Insert your code here

z=list(years)
year_1=str(z[0])
year_2=str(z[1])
#print(z)
fields = [year_1,year_2]
index=[]
index1 = []
colomn=[]
colomn1 = []
colomn2 = []
colomn3 = []
j=0
k=0
j1 = 0
k1 = 0
q=0
mydict = defaultdict(list)
country = []
difference1 =[]
difference2 = []
ratio = []
with open(agricultural_land_filename, 'rt',encoding='utf-8') as f:
	b=csv.reader(f,delimiter=',',quotechar='"')
	for row in b:
		index = row
		index1 = row
		country_index = row
		for i in range(len(index)):
		#print(index)
			if fields[0] == index[i]:
				j = i
				#print(j)
				#print(index[j])
		for m in range(len(index1)):
			if fields[1] == index1[m]:
				k = m
				#print(k)
		for n in range(len(country_index)):
			if 'Country Name' == country_index[n]:
				q=n
		for i in range(5,len(country_index)):
			country.append((country_index[0]))
			break
		for i in range(5,len(index)):
			colomn.append(index[j])
			break
		for i in range(5,len(index)):
			colomn1.append(index[k])
			break
	for i in range(len(colomn)):
		for j in range(i,len(colomn1)):
			if colomn1[j] != '' and colomn[i] != '':
				if float(colomn1[j]) >= float(colomn[i]):
					difference2.append(float(colomn1[j]) - float(colomn[i]))
				else:
					difference2.append(0)
			else:
				difference2.append(0)
			break
	
	#print('difference2--->',difference2)			   
	#print(mydict)
	#print('colomn--->',colomn)
	#print('colomn1--->',colomn1)
	#print('country--->',country)

with open(forest_filename, 'r',encoding='utf-8') as f1:
	b1=csv.reader(f1)
	for row in b1:
		index3 = row
		index4 = row
		for i in range(len(index3)):
			if fields[0]==index3[i]:
				j1 = i
		for m in range(len(index4)):
			if fields[1] == index4[m]:
				k1 = m
		for i in range(5,len(index3)):
			colomn2.append(index3[j1])
			break
		for i in range(5,len(index4)):
			colomn3.append(index4[k1])
			break
	for i in range(len(colomn2)):
		for j in range(i,len(colomn3)):
			if colomn3[j] != '' and colomn2[i] != '':
				if float(colomn3[j]) >= float(colomn2[i]):
					difference1.append(float(colomn3[j]) - float(colomn2[i]))
				else:
					difference1.append(0)
			else:
				difference1.append(0)
			break
	#print('difference1--->',difference1)
	#print('colomn2--->',colomn2)
	#print('colomn3--->',colomn3)

for i in range(len(difference2)):
	for j in range(i,len(difference1)):
		if difference1[j] != 0:
			ratio.append(round(difference2[i]/difference1[j],2))
		else:
			ratio.append(0)
		break
for i in range(len(country)):
	for s in range(i,len(ratio)):
		mydict[country[i]].append(ratio[s])
		break
sorted_dict = sorted(mydict.items(), key=operator.itemgetter(1))
top_n_countries = (sorted_dict[-top_n:])[::-1]
#print(top_n_countries)
for items in top_n_countries:
	for i in range(len(items)):
		a = items[0] + ' ' +'('+ str(f'{items[1][0]:.2f}') + ')'
		countries.append(a)
		break
#print('sorted_dict--->',sorted_dict)
#print('mydict--->',mydict)
#print('ratio--->',ratio)
#print('ratio--->',len(ratio),'sorted_dict--->',len(sorted_dict),'mydict--->',len(mydict))
#print('colomn--->',len(colomn),'colomn1--->',len(colomn1),'difference2--->',len(difference2),'difference1--->',len(difference1),'country--->',len(country))
#print('top n countries--->',top_n_countries)
print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
