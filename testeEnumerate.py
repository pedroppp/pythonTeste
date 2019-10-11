
l = [100,200,300,400]
print(enumerate(l))
print(list(enumerate(l)))
for idx, item in enumerate(l):
    l[idx] += 10
print(l)