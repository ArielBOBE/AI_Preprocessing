# to do - for true dataset 
"""
1. Load all csv, and eliminate all rows except for the last row (to get true dataset) DONE 
2. Melt each wide dataset and make it into long dataset, making value_vars = [all col] 
3. Merge all 5 datasets

-- BASIC DESCRIPTIVE STATISTICS
4. Get distribution of the classes
5. Get mean and mode 
"""

# to do - for measure of agreement between the two graders
"""
1. drop last row
2. Melt each wide dataset and make it into long dataset, making value_vars = [all col]
3. Merge all datasets 

-- COHEN KAPPA's
4. Get occurence of all classes for each grader
5. Get observed agreement -> number of agreement/total data size
6. Get expected agreement -> sum of the product of proportion of classes for each rater  
7. Compute cohen kappa's statistic by (Po - Pe) / (1 - Pe)
""" 