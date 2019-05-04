def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = n + sum
    return  sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k,v)

