
"""
Purpose: SO Answer
Date created: 2021-11-01

https://stackoverflow.com/questions/69791808/get-row-when-certain-condition-is-changed-in-dataframe?noredirect=1#comment123365393_69791808

Contributor(s):
    Mark M.

Desc -
I am looking for a solution to get row when certain condition is changed.

Here is example of my dataframe.
     ts  fdw     time_stamp
0     n  [0, 0]  1635211605896
1     n  [0, 0]  1635211606896
2     l  [0, 0]  1635211607896
3     l  [0, 0]  1635211608896
4     l  [0, 0]  1635211609896
5     l  [0, 0]  1635211609896
6     n  [0, 0]  1635211609896


On the above dataframe, I want to extract row when column name ts is changed such as
n to l or l to n.

Here is my expected output.

     ts  fdw     time_stamp
1     n  [0, 0]  1635211606896
2     l  [0, 0]  1635211607896
5     l  [0, 0]  1635211609896
6     n  [0, 0]  1635211609896

Comment: "When the column name ts 's value is different from previous value. For example,
        ignored the row when ts has same value with previous, and extract row when ts is
        changed."
"""


import pandas as pd

df = pd.DataFrame({"ts": ["n", "n", "l", "l", "l", "l", "n"]})
df["fdw"] = "[0,0]"
df["time_stamp"] = [0] * df.shape[0]
df.loc[0, "time_stamp"] = 1635211605896
df.loc[1, "time_stamp"] = 1635211606896
df.loc[2, "time_stamp"] = 1635211607896
df.loc[3, "time_stamp"] = 1635211608896
df.loc[4, "time_stamp"] = 1635211609896
df.loc[5, "time_stamp"] = 1635211609896
df.loc[6, "time_stamp"] = 1635211609896


# df["time_stamp"].shift(periods = 1, fill_value = df.loc[1, "time_stamp"]) != df["time_stamp"]
df["ts"].shift() != df["ts"]
df["ts"].shift(fill_value = df.loc[1, "ts"]) != df["ts"]


df.loc[:df.shape[0]-2, "ts"] - df.loc[1:, "ts"]


df.drop(columns=["ts", "time_stamp"], axis=1)
df.drop_duplicates(subset="time_stamp")

df.drop_duplicates(subset=["ts", "time_stamp"], keep="last")

df.groupby(["ts", "time_stamp"]).size().cumsum()
df.groupby(["ts"]).count().cumsum()

df.groupby(["ts", "time_stamp"]).cumcount()