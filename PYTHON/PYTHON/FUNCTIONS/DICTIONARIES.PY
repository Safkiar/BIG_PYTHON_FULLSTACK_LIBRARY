'''

'''



example_dictionary = {
    'string':'string',
    'num': 10,
}


# get value from dictionary
example_dictionary.get("string")

# add value to dictionary
example_dictionary["new value"] = True

# remove value from dictionary
example_dictionary.pop('num')

# clear all values fom dictionary
example_dictionary.clear()

# delete entirely dictionary
del example_dictionary

# Copied value dic = dic2 
# values from dic2 will be also altered in dic

# Copy dictionary
clone_dictionary = new_dictionary.copy()