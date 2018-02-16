

"Read the CSV file and the split the file based on CR"

file_list= open("US_births_1994-2003_CDC_NCHS.csv", 'r').read().split("\r")

#print(file_list)


"Creating a function read_csv that reads ina file and converts all the values inside the cell into a int"

def read_csv(filename):
    data=open(filename).read()
    data_list=data.split("\r")[1:]
    final_list=[]
    for row in data_list:
        int_fields=[]
        string_fields=row.split(",")
        
        for cell in string_fields:
            int_fields.append(int(cell))
    
        final_list.append(int_fields)
    return final_list


#print(read_csv("US_births_1994-2003_CDC_NCHS.csv"))

"Calculating no of births by month"

def month_birth(intergerList):
    births_per_month={}
    
    for row in intergerList:
        day_of_month=row[1]
        births=row[4]
        
        if day_of_month in births_per_month.keys():
            births_per_month[day_of_month]=births_per_month[day_of_month]+ births
        else:
            births_per_month[day_of_month]=births
            
    return births_per_month


# f=read_csv("US_births_1994-2003_CDC_NCHS.csv")
# print(month_birth(f))
            
"Create a function named dow_births() that takes a single, required argument (a list of lists) and returns a dictionary containing the total number of births for each unique value of the day_of_week column."

def dow_birth(intergerList):
    
    final_list={}
    for row in intergerList:
        day_of_week=row[3] 
        births=row[4]
        
        if day_of_week in final_list.keys():
            final_list[day_of_week]=final_list[day_of_week] + births
        else:
            final_list[day_of_week]=births
        
    return final_list


# f=read_csv("US_births_1994-2003_CDC_NCHS.csv")
# print(dow_birth(f))      
        
        
"Instead of the two functions create a new function which is more user friendly"

def cal_count(data, column):
    
    final_list={}
    for row in data:
        columnRequested=row[column]
        births=row[4]
        
        if columnRequested in final_list.keys():
            final_list[columnRequested]=final_list[columnRequested] + births
        else:
            final_list[columnRequested]=births
    return final_list

f=read_csv("US_births_1994-2003_CDC_NCHS.csv")
#print(cal_count(f,0))  


"Merging CDC file with SSA"

import pandas as pd
fileCDC=pd.read_csv("US_births_1994-2003_CDC_NCHS.csv")
fileSSA=pd.read_csv("US_births_2000-2014_SSA.csv")
fileSSA=fileSSA.dropna(axis=1)
merged=fileCDC.merge(fileSSA, on='title')



        