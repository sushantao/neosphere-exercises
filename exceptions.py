def test(x,y):
    try:
        return x/y
    except:
        # print("error")
        return "Noo"
a,b=2,4
# print(test(2,0))
print(f'{a},{b}=> {test(a,b)}')
