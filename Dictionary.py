# # Dictionary is a collection of key-value pairs, where each unique key maps to a value. Dictionaries are optimized for retrieving the values

# # Dictionary is a built-in data type of Python that stores collections of key:value pairs. It is similar to an array, but instead of

# # A DIctionary is a Data-Structure, the Data is arranged in form of Table i.e Rows & Columns
# # It has a property like - Ordered / Mutable & Not Alloe Duplicates
# # Dictionaries are used to store data as Key Value pairs
# # Creating dictionary 
# dict1 = {'name': 'John', 'age':25}
# print(type(dict1))
# print(dict1)

# # Accessing value from key
# value = dict1['name']
# print("Value: ", value)


# # Updating Dictionary
# dict1['city'] = "New York"
# print(dict1)
# # Deleting Element From Dictionary
# del dict1["age"]
# print(dict1)
# # # Check if element exists or not using In operator
# # if "city" in dict1 :
# #     print("Key Exists")
# # else:
# #     print("Key Doesn't Exist")
    
# # # Adding new elements to dictionary
# # dict1["address"]="USA"
# # print(dict1)

# # # Getting all keys and values of dictionary
# # keys_values = list(dict1.items())
# # print(keys_values)

# # # Getting all Keys only
# # keys = list(dict1.keys())
# # print(keys)

# # # Getting all Values Only
# # values = list(dict1.values())
# # print(values)

# # # Using for loop to iterate through dictionary
# # for key , value in dict1.items():
# #     print(key," : ",value)

# # # Nested dictionaries
# nestedDict = {
#     "personalDetails":{
#         "Name":"John",
#         "Age":30,
#         "City":"NYC"
#     },
#     "professionalDetails":{
#         "JobTitle":"Software Engineer",
#         "Company":"ABC Corp.",
#         "Location":"San Francisco"
#     }
# }
# # # Accessing nested dictionary
# print(nestedDict["personalDetails"])

# # # Accessing inner dictionary from outer one
# print(nestedDict["professionalDetails"])

# # # Accessing individual items from the nested dictionary
# print(nestedDict["professionalDetails"]["JobTitle"])






a = {'name':'None','USN':'None','age': 0,'course':['cs','AIML']}
print(a)

print(a['course'])

a['name'] = 'PAVAN'
print(a)

a['USN'] = '3BR21AI014'
print(a)

name = input("Enter name :")
a['name'] = name
print(a)

# 