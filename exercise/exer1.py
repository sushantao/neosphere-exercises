num=2000
list1=[]
while num<3201:
    if num%7==0 and num%5!=0:
        list1.append(num)
        print(list1)
    num+=1
