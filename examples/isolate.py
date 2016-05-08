from scopr import scope

a = 1

with scope():
    b = 0
    a = b

print(a)

a = [1, 2, 3, 4]

with scope():
    a.append(8)

print(a)

a = [1, 2, 3, 4]

with scope(isolate=True):
    a.append(8)

print(a)
