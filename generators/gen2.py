def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

x=PowTwoGen(5)

for i in x:
    print(i)