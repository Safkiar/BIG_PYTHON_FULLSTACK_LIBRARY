num_list = [1,2,3,4,5]
status = 0

'''
For Loops:
'''

for x in num_list:
    print(x)


'''
While loops:
'''

while status < 5:
    status += 1
    if status == 4:
        pass
    if status == 5:
        continue
    if status == 6:
        break
    print(status)



# loop through dictionary
new_dictionary = {}
# through keys
for x in  new_dictionary:
    pass
# through keys and values
for x,y in new_dictionary.items():
    pass