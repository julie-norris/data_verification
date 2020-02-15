# data_verification

Data Quality Assurance

Please describe your findings, process, and include
code/diagrams as necessary.

In looking at the SAT file, I first looked at the entire data set to understand what I was looking at confirming my understanding of the data 
with the descriptions in the layout.xlsx file.

I then looked for obvious areas of irregularities and wrote some code to standardize the process of identifying all of the rows with errors.
I looked for rows with missing district code, school code, or number of N_Students_Scored. Only the district code column had missing data.
When the query ran to find schools with N_Students_Scored, 7 schools were returned. Within that group, 2 schools were from District Codev3150 and 
3 schools were in District Code 4010. The School Codes for District Code 4010 were irregular in that three of them were single digit. This is 
something I would investigate more to confirm accuracy.

In lines 19-21 of the python file I look for any scores that were outside the given range of 200-800 in each of the academic areas, Mathematics, 
Critical Reading, and Writing. There were no inaccuracies determined. The query does return the same 7 schools that have no students scored.

Line 17 searches for rows where zero students scored above 1550. While this data does not determine errors or inaccuracies, they are outliers 
and I would want to know more to confirm that the data is correct.

