d = dict(a = 1,b=2,c=3)

print(d.keys())
print(d.values())
print(d.items())

for i in d.items():
    print(type(i),i[0])

print(['a','b'] ==['a','b'])