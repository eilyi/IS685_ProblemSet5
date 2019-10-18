#deniro_pd.py 

import pandas as pd
import math
import csv

#need to consolidate any columns that aren't empty in column 4 into column 
#If Column 4 is NOT NULL, concatenate it into Column 3
df = pd.read_csv("deniro.csv")
#df['new_col'] = range(1, len(df) + 1)

for row in range(0, len(df)):
	#print(type(df.loc[row][3]))
	if type(df.loc[row][3]) is str:
		title = str(df.loc[row][2])
		title += str(df.loc[row][3])
		df.ix[row, 2] = "Title" 
		#slice= df.ix[:len(df), 0:3]	
	#print(df)

#Print the score for Heat
print(df.loc[df["Title"] == "Heat"])

#Print all movies from 1992 

print(df.loc[df['Year'] == '1992'])
#print(df.head(10))