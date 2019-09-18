def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(a, x):
    result = a(x)
    return result

print(operate(inc,3))
print(operate(dec,3))
############################
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")


make_pretty(ordinary)()

#############################
def make__pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make__pretty
def oordinary():
    print("I am ordinary")


#############################

def smart_divide(func):
   def inner(a,b):
      print(f"I am going to divide {a} and {b}")
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
