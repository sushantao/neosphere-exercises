def countdown(num):
    for a in range(num):
        yield a


b=countdown(5)
print(next(b))

for i in b:
    print(i)