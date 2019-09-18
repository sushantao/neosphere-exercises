import sys

def test_func(*args):
    for a in args:
        print(a)

test_func(sys.argv)


