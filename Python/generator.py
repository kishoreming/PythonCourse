def dis():
    for i in range(6):
        yield i

o=dis()
for i in o:
    print(i)
