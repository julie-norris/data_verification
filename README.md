Take home challenge - 

The file will run from the command line (python take_home.py). The python file and two txt files should all be saved in the dame directory. The results will be printed in the terminal. 


**Data Quality Assurance**

Please describe your findings, process, and include
code/diagrams as necessary.

In looking at the SAT file, I first looked at the entire data set to understand what I was looking at confirming my understanding of the data 
with the descriptions in the layout.xlsx file.

I then looked for obvious areas of irregularities and wrote some code to standardize the process of identifying all of the rows with errors.
I looked for rows with missing district code, school code, or number of N_Students_Scored. Only the district code column had missing data.
When the query ran to find schools with N_Students_Scored, 7 schools were returned. Within that group, 2 schools were from District Codev3150 and 
3 schools were in District Code 4010. The School Codes for District Code 4010 were irregular in that three of them were single digit. This is 
something I would investigate more to confirm accuracy.

I looked for any scores that were outside the given range of 200-800 in each of the academic areas, Mathematics, Critical Reading, and Writing. There were no inaccuracies noted. The query does return the same 7 schools that have no students scored.

I tested for rows where zero students scored above 1550. While this data does not determine errors or inaccuracies, they are outliers 
and I would want to know more to confirm that the data is correct.


**Data Transformation**

1. Concatenate the three code columns and to create a single ID column.
2. Create a new column OVERALL_ENROL by joining the SAT.txt and the supplied
enrollment.txt file.

The first two parts of this section were fairly straightforward and I added documentation in the file.


3. Calculate the percentage of students taking the SAT at each school. Store that value in a separate column, PERC_TAKING_SAT, noting any irregularities in the result.

The irregularities are that many of the results showed schools where greater than 100% were taking the SAT. When I joined the two files it was concerning that there was no common foreign key on which to join them so there is no way to know for sure that the schools in the SAT file are matching their state_id and enrollment numbers on the Enrollment file.  This may be the cause of the irregularities. 


4. Now reshape the SAT file from a wide format to a normalized (or long) structure with the following three columns: ID, DATA_TYPE, and VALUE.





