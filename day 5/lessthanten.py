
listItem=[2,4,5,12,32,6]
b=[]
for each in listItem:
    if each<10:
        b.append(each)
print(b)


######teacher's way

a=[1,2,3,4,5,643,5656,4]
b=[item for item in a if item<10]
print(b)
for p in b:
    print(p)