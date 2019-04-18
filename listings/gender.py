import numpy as np
import pandas as pd
import re
from pandas import DataFrame, Series

dataset = pd.read_csv("austin_listings.csv", header = 0)

import gender_guesser.detector as gender

d = gender.Detector()

genders = []
comp = []
comp.append("rent")
comp.append("Rent")
comp.append("propert")
comp.append("Propert")
comp.append("vacation")
comp.append("Vacation")
comp.append("LLC")
comp.append("llc")
comp.append("estate")
comp.append("Estate")
comp.append("The")
comp.append('manag')
comp.append("Manag")

compound = []

compound.append('and')
compound.append('And')
compound.append('+')
compound.append('&')

for row in dataset.itertuples():
	name = str(row.host_name)
	gender = d.get_gender(row.host_name)
	if gender == 'male' or gender == 'female' or gender == 'mostly_male' or gender == 'mostly_female':
		genders.append(gender)
		continue
	try:
		list_name = name.split()
	except:
		genders.append('nonsense')
	flag = False
	for thing in comp:
		x = re.search(thing, name)
		if x:
			flag=True
	if 'and' in name or 'And' in name or '&' in name or '+' in name:
		gender = 'couple'
	elif len(list_name) >= 3:
		gender = "company"
	elif flag:
		gender = "company"

	genders.append(gender)

dataset['host_gender'] = Series(genders, index=dataset.index)

thing = dataset['host_name']
result = DataFrame(thing)

result['host_gender'] = Series(genders, index=dataset.index)

result.to_csv('out1.csv')