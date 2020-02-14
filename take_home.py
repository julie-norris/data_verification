import pandas as pd
import numpy as np

sat_scores=pd.read_csv("C:\\Users\\julie.norris\\Documents\\Python_Scripts\\GreatSchools\\SAT.txt", sep=r'\t', engine='python')
df=pd.DataFrame(sat_scores)

print(0 in df.values)

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