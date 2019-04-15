import numpy as np
import pandas as pd

from pandas import DataFrame, Series

dataset = pd.read_csv("austin_listings.csv", header = 0)

import gender_guesser.detector as gender

d = gender.Detector()

genders = []
for row in dataset.itertuples():
	gender = d.get_gender(row.host_name)
	genders.append(gender)
dataset['host_gender'] = Series(genders, index=dataset.index)
print(dataset.head())
#print(dataset.shape)