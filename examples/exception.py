from scopr import scope

a = 1

try:
    with scope():
        a = 2
        raise RuntimeError
except RuntimeError:
    print("Oops there was an error")

print(a)
