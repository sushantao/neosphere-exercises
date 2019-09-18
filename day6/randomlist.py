

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

#print("First randomly generated list is: ", ListA)

#print("Second randomly generated list is: ", ListB)

for each in list_a:

    if each in list_b and each not in list_c:

        list_c.append(each)

# print("Common values between two list is: ", list_c)

print("Common: ", len(list_c))

