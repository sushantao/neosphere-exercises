#Write a program which accepts a sequence of comma-separated numbers from
#  console and generate a list and a tuple which contains every number.

num=input("Enter a number")
a=num.split(',')

print(a)

print(tuple(a))


##########teacher solution
num=input("Enter a number")
a=num.split(',')
#a = [item for item in a]
#print(a)
#print(type(a))
m = []
for x in a:
    z = int(x)
    m.append(z)
    
print(m)