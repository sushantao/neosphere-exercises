l1=[1,2,3,4,5]

l2=['a','b','c','d','e']

l3=[101,102,103,104]
# index=0
# for i in l1:
#     print(i)
#     print(l2[index])
#     print(l3[index])
#     index+=1

for i,j,k in zip(l1,l2,l3):
    print(i)
    print(j)
    print(k)