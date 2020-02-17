import pandas as pd
import numpy as np
sat_scores=pd.read_csv("SAT.txt", sep='\t', dtype={0:'str', 1:'str', 2:'str'})
enrollment=pd.read_csv("ENROLLMENT.txt", sep='\t', dtype={0:'str', 1:'str'})
df=pd.DataFrame(sat_scores)
df1=pd.DataFrame(enrollment)

def missing_Data():
	print("MISSING DISTRICT CODE:")
	print ( df.query('DIST_CODE != DIST_CODE'))
	#print (df.query('SCH_CODE != SCH_CODE'))
	#print (df.query('N_STUDENTS_SCORED != N_STUDENTS_SCORED'))
	print("ZERO STUDENTS WERE SCORED:")
	print(df.loc[df['N_STUDENTS_SCORED'] == 0])
	print("ZERO STUDENTS SCORING ABOVE 1550")
	print(df.loc[df['SAT_1550'] == 0])
	print("SCORES TOO HIGH OR TOO LOW")
	print((df.loc[df['MATHEMATICS'] > 800]) | (df.loc[df['MATHEMATICS'] < 200]))
	print((df.loc[df['CRITICAL_READING'] > 800]) | (df.loc[df['CRITICAL_READING'] < 200]))
	print((df.loc[df['WRITING'] > 800]) | (df.loc[df['WRITING'] < 200]))
	
missing_Data()


def convert_long_to_wide():
	"""Concatenate the three code columns and to create a single ID column."""
	df['DIST_CODE'] = df.DIST_CODE.fillna('')
	df['ID']=df['CO_CODE']+df['DIST_CODE']+df['SCH_CODE']

	"""change name from enrollment to OVERALL_ENROL and join the two dataframes"""
	"""df1.rename(columns={"enrollment" : "OVERALL_ENROL"}, inplace=True)
	result = pd.concat([df, df1], axis=1, sort=False)
	replace all NaN with 0 to be able to make calculations
	result['OVERALL_ENROL']=result['OVERALL_ENROL'].fillna(0)
	result['state_id']=result['state_id'].fillna(0)
	
	Calculate the percentage of students taking the SAT at each school. Store that value
	irregularities in a separate column, PERC_TAKING_SAT, noting any irregularities in the result.
	result['PERC_TAKING_SAT'] = result['N_STUDENTS_SCORED'].astype(int)/result['OVERALL_ENROL'].astype(int)
	result['PERC_TAKING_SAT'] = result['PERC_TAKING_SAT']*100
	print(result) """

	"""reshape the SAT file from a wide format to a normalized (or long) structure
	with the following three columns: ID, DATA_TYPE, and VALUE."""
	df['indx']=df.index
	print(df)
	pd.melt(df, id_vars='ID', value_vars=['MATHEMATICS'],['CRITICAL_READING'],['WRITING'],['SAT_1550'],['TOTAL'])
	print(df)

convert_long_to_wide()
