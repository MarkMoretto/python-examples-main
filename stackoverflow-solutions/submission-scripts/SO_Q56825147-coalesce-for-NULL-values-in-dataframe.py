
## https://stackoverflow.com/questions/56825147/how-can-we-use-coalesce-in-python-for-multiple-data-frames-using-pandas
import pandas as pd

ddict1 = {
    'EmpID':[1,2],
    'Emp_Name':['',''],
    'Dept_id':[1,2],
    'DeptName':['',''],
}

ddict2 = {
    'EmpID':[1,2],
    'Emp_Name':['XXXXX','YYYYY'],
    'Dept_id':[1,2],
    'DeptName':['Sciece','Maths'],
}

df1 = pd.DataFrame(ddict1)
df2 = pd.DataFrame(ddict2)


def replace_df_values(df_A, df_B):
    ## Select object dtypes
    for i in df_A.select_dtypes(include=['object']):
        ### Check to see if column contains missing value
        if len(df_A[df_A[i].str.contains('')]) > 0:
            ### Create mask for zero-length values (or null, your choice)
            mask = df_A[i] == ''
            ### Replace on 1-for-1 basis using .loc[]
            df_A.loc[mask, i] = df_B.loc[mask, i]

### Pass dataframes in reverse order to cover both scenarios
replace_df_values(df1, df2)
replace_df_values(df2, df1)

#df1.loc[mask, 'Emp_Name'] = df2.loc[mask, 'Emp_Name']





