from scopr import scope

a = 1

def test():
    return "Hello, World!"

with scope():
    a = 2
    with scope():
        print(a)
        a = 3
    print(a)
print(a)
