class TestClass:
    def __init__(self,name):
        self.name=name
        print("init called")

    def testFun(self):
        print("testfun called")

obj1=TestClass("roshan")
obj2=TestClass("sushanta")

print(obj1.name)
print(obj2.name)

obj2.testFun()