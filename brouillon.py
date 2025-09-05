def foo(arg, /):
    print(arg)

try:
    foo(arg=3)
except:
    print(4)