def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


x = countdown(5)

print(x)
for i in x:
    print(i)