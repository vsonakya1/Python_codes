from csv import reader
from operator import index
import pandas as pd


df= pd.read_csv("100_Sales_Records.csv")
df1= pd.read_csv("100_Sales_Records_1.csv")

#-------------------------- R e a d - d a t a --------------------------
'''
print(len(df),"\n---------")                      #number of rows
print(df.columns,"\n---------")                   #Header
print(df.head(3),"\n---------")                   #Header
print(df['Region'],"\n---------")                 #column values
print(df['Region'].unique(),"\n---------")        #distinct column values
print(df[['Region','Country']],"\n---------")     #Visualize two columns column values
print(df.iloc[1],"\n---------")                   #Visualize first row in a file
print(df.iloc[0:5],"\n---------")                 #Visualize first 5 rows in a file
print(df.iloc[2,0],"\n---------")                 #Visualize cell value, it is Europe

for index, row in df.iterrows():
    print(index,row)                              # row one by one

print(df.loc[df['Region']=="Europe"])             # find all rows where column =Region and value = Europe
print(len(df.loc[df['Region']=="Europe"]))        # count find all rows where column =Region and value = Europe
print(df.sort_values("Region"))                     # Sort data in Acending order
print(df.sort_values("Region",ascending=False)  )   # Sort data in decending order
print(df.sort_values(["Region","Country"],ascending=[1,1]))   # Sort 2 columns data


# print(df.sort_values(["Region","Country"]))   # Sort 2 columns data
# print(df.to_string([["Region","Country"]]))   # Sort 2 columns data
#-------------------------- Analyzing - d a t a --------------------------

# print(df["Region"])

# print(df.loc[(df["Region"] =="Europe") | (df["Region"] =="Asia")])    # find all rows where column =Region and value = Europe and Asia


# print(df.loc[(df["Region"] =="Europe") & (df["Country"] =="Russia")])    # find all rows where column =Region and value = Europe and Asia

# print(df)
# print(df1)
x= df.compare(df1)                                  # compare 2 files (dataframe) verical
print(x) 


x= df.compare(df1,align_axis=1)                     # compare 2 files (dataframe) horizontal
print(x) 

'''
x= df.compare(df1).rename(index={"self":"df1","other":"df2"},level=-1)             # compare 2 files (dataframe) horizontal
print(x)





