x=[1,2,3, "Abc"]
print(x[0])

x.append("newVal")
print(x)
x.extend([1,2,3])
print(x)

x.insert(1, "ok")
print(x)

x.remove("ok")
print(x)

x.pop(2)
print(x)

op=x.count("ok")
print(op)

x.reverse()
print(x)