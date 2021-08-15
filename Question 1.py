#Question 1

#import dependencies
import pandas as pd
import pandasql as ps
import numpy as np

# read testfile 
csv_filepath = "q1.csv"
#csv_filepath = input("Please enter your csv filepath: ")
df = pd.read_csv(csv_filepath)
# convert manager id to int
df["manager_id"] = df["manager_id"].fillna(0).astype(int)

'''FOR PART a'''
# merge a copy of the same table to get manager's salary for comparison later
df2 = df.copy()
df3 = pd.merge(df,df2, left_on = "manager_id", right_on = "id", how = "left", copy = False, suffixes = ("_employee","_manager"))

# higher_than_manager column provides boolen value if employee is paid higher than manager
x = np.where(df3["Salary_manager"] < df3["Salary_employee"], True ,False)
df3["higher_than_manager"] = x
print(df3[["id_employee","Salary_employee","Salary_manager","higher_than_manager"]])

'''FOR PART b'''
# get unique list of managers
df4 = df.copy()
df4.drop_duplicates(subset="manager_id", inplace = True)

#add column to show rows with no manager
df["no_manager"] = df["id"].isin(df4["manager_id"])==False

print (df)



