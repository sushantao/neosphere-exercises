# total=1
# n=8
# while(n>0):
#     total=total*n
#     n-=1
# print(total)

n=4
total=1
for i in range(1,n+1):
    total=total*i
print(total)

def fact(n):

    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
    
    