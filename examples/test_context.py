from scopr import scope

a = 1

def test():
    return "Hello, World!"

with scope():
    b = 1
    a = 2

    def test():
        return "Goodbye, World!"

    print(test())

print("a: {}".format(a))
print(test())
print("b: {}".format(b))
