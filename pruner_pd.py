#pruner

import pandas as pd
import json  

#1. Change dataset from json file before putting in dataframe? > add numbered column, omit "top" part 

with open('baby_names.txt') as json_file:
	df = pd.read_json('baby_names.txt', orient='column')

	df.reset_index(inplace=True)			#get the numbered column 
	df.columns = ['Name', 'Count']
	#df= json_normalize(nested, record_path = 'data_frame')

	
	#1. Remove all rows with names that contain the letter "v"
	#2. Remove any instances of the following names: Gary, Aaron, Luke, Winston, Avery (already removed)

	names = ["Gary", "Aaron", "Luke", "Winston", "Avery"]
	for row in range(0, len(df)):
		if df.loc[row][0] in names or 'v' in df.loc[row][0] or df.loc[row][1] == 28:#
			df = df.drop(row)

	#Reset the index 
	#Add the name & count for 'Ron'
	df.reset_index(inplace=True, drop=True)
	df.loc[len(df)] = ['Ron', 5]
	print(df)






