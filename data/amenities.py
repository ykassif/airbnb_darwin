import numpy as np
import pandas as pd
import re
from pandas import DataFrame, Series

dataset = pd.read_csv("listings.csv", header = 0)

data = pd.read_csv('data.csv', header = 0)

mem = []
for row in dataset.itertuples():
	am = str(row.amenities).strip('{')
	am = am.strip('}')
	am = am.split(',')
	for a in am:
		a = a.strip('"')
		if a not in mem and 'ther' not in mem and '_49' not in a and 'Stair g' not in a and ' hoist' not in a and 'corner guar' not in a and a != '' and '_50' not in a:
			mem.append(a)
for i in range(len(mem)):
	mem[i] = [mem[i], [0]]
for row in dataset.itertuples():
	am = str(row.amenities).strip('{')
	am = am.strip('}')
	am = am.split(',')
	for m in mem:
		flag = False
		for a in am:
			a = a.strip('"')
			if a == m[0]:
				flag = True
		if flag == False:
			if len(m) < 3:
				m.append('count')
			else:
				m[1].append(0)
		else:
			if len(m) < 3:
				m.append('count')
				m[1] = [1]
			else:
				m[1].append(1)
hitlist = []
for i in range(len(mem)-1):
	att = mem[i]
	if sum(att[1]) < 250:
		hitlist.append(i)
hitlist = sorted(hitlist, reverse=True)
for x in hitlist:
	del mem[x]
for m in mem:
	print(len(m[1]))
	for i in m[1]:
		if i != 1 and i != 0:
			print(i)
	data[m[0]] = Series(m[1], index= data.index)
print(data.head())
