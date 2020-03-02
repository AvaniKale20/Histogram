# create an empty dataframe
import pandas as pd
dataFrame=pd.DataFrame()
print("Empty dataframe =",dataFrame)

# Example one
# create dataframe from single list
print()
list=[0,1,2,3,4,5,5,6]
dataFrame=pd.DataFrame(list)
print("create dataframe from single list=")
print(dataFrame)

# Example Two
print()
listOfNameAndMarks=[['avani',100],['john',100],['khalesi',76],['snow',80]]
dataFrame=pd.DataFrame(listOfNameAndMarks,columns=['Name','Marks'])
print("list of students marks =")
print(dataFrame)

# Example Three
# we can also provide datatype
print()
listOfNameAndMarks=[['avani',100],['john',100],['khalesi',76],['snow',80]]
dataFrame=pd.DataFrame(listOfNameAndMarks,columns=['Name','Marks'],dtype=float)
print("list of students marks =")
print(dataFrame)
print()

# --------------------------------------------------------------------------------------------------------------------

# Create a DataFrame from Dict of ndarrays / Lists
dataOfNameAndAge={'Name':["avi","khalesi","john","bro"],'Age':[23,21,43,54]}
dataFrame=pd.DataFrame(dataOfNameAndAge)
print(dataFrame)

print()
print("using index variable in dataframe=")
dataOfNameAndAge={'Name':["avi","khalesi","john","bro"],'Age':[23,21,43,54]}
dataFrame=pd.DataFrame(dataOfNameAndAge,index=['rank1','rank2','rank3','rank4'])
print(dataFrame)

# ----------------------------------
# Create a DataFrame from List of Dicts
print()
print("Create a DataFrame from List of Dicts")
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print (df)


