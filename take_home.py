import pandas as pd
import numpy as np
sat_scores=pd.read_csv("SAT.txt", sep='\t', dtype={0:'str', 1:'str', 2:'str'})

df=pd.DataFrame(sat_scores)

"""
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
"""

def convert_long_to_wide():
	df['DIST_CODE'] = df.DIST_CODE.fillna('')
	df['ID']=df['CO_CODE']+df['DIST_CODE']+df['SCH_CODE']
	
	new_table=pd.melt(df, id_vars['ID'], value_vars=['TOTAL'],var_name='DATE_TYPE') #,['MATHEMATICS'],['CRITICAL_READING'],['WRITING'],['SAT_1550'], 
	print(new_table)
	return(new_table)

convert_long_to_wide()
