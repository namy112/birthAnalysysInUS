#Reading a file

f = open("births.csv", 'r')
text = f.read()
#print(text)

#split row by \n and convert it into a list
lines_list=text.split("\r")
#print(lines_list)

    
    
#create a dictionary

dict_result=dict() 
new_list_no_header=lines_list[1:len(lines_list)]
#SSSprint(new_list_no_header)
"""
Iterate through this new list,
Split each line on the comma delimiter,
Extract the day_of_week value and the births value for each line,
If the day_of_week value already exists as a key in the dictionary, add the births value to the existing, associated value.
If the day_of_week value doesn't exist as a key, add it to the dictionary and set the associated value to the births value for that line.
"""
for row in new_list_no_header:
    split_list=row.split(",")
    day_of_week=split_list[3]
    no_of_birth=int(split_list[4])
    
    if day_of_week in dict_result:
        dict_result[day_of_week] = dict_result[day_of_week] +  no_of_birth
    else:
        dict_result[day_of_week] = no_of_birth
        
print(dict_result)
    