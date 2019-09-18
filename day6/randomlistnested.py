import random

list_a = []

list_b = []

list_c = []

#length_a = int(input('enter the length of first list: '))

#length_b = int(input('enter the length of second list: '))

length_a = 50000

length_b = 50000

random_low = 0

random_high = 20000

while length_a > 0:

    list_a.append(random.randint(random_low, random_high))

    length_a -= 1

while length_b > 0:

    list_b.append(random.randint(random_low, random_high))

    length_b -= 1


for i in list_a:

    for j in list_b:

        if i == j and i not in list_c:

            list_c.append(i)

print("Common: ", len(list_c))

