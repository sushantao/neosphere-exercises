# Create the dictionary and print
user = {"Name": "Christine", "Age": 23}
print(user)
# Add a new item and print
user["Height"] = 154
print(user)

for k, v in user.items(): #tuple
    print (f'Key: {k}, value: {v}')