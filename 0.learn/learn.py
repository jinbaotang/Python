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
    sum = 0
#    print(k,v)

#列表生成式
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def add(x, y, f):
    return f(x) + f(y)

f = abs
x = -6
y = -5
from functools import reduce

def normalize(name):
    #name=name[0].upper() + name[1:].lower()
    name=name.capitalize()
    return name
def prod(x, y):
    return  x*y
z = reduce(prod, [1,8,30,4])

from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    def str2int(x, y):
        return x*10 + y
    def char2num(s):
        return DIGITS[s]
    s = s.replace('.', '')
    return reduce(str2int, map(char2num, s))

s = "125553.456"
str_len = len(s)
float_number = 0
'''
if s.find(".") == -1:
    print(str2float(s))
else:
    dot_index = s.find(".")
    float_number = str2float(s)/(10**(str_len - dot_index-1))
    print(float_number)
'''
'''
g = (x*x for x in range(10))
for n in g:
    print(n)
'''
def fib(max):
    n,a,b = 0,1,1
    while n < max:
        yield a
        a,b = b,a+b
        n = n + 1
    return "done"
g = fib(8)


def triangles():
    L = [1]
    yield L
    while True:
        #L = [1] + [L[x] + L[x + 1] for x in range(len(L) - 1)] + [1]
        L1 = []
        for x in range(len(L) - 1):
            L1.append(L[x] + L[x+1])
        L = [1] + list(L1) + [1]
        yield L
n = 0
for L in triangles():
    #print(L)
    n = n + 1
    if n == 10:
        break

import random

# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')
#筛选素数。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        #print(n)
        x = 1
    else:
        break

#回数
def is_palindrome(n):
    user_str = str(n)
    str_len = len(user_str)
    for i in range(0, int(str_len/2)):
        if user_str[i] != user_str[str_len - i-1]:
            return 0
    return 1

#print(list(filter(is_palindrome, range(0, 1000))))

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
i = 0
def creatcounter():
    def counter_increase():
        global i
        i = i + 1
        return i
    return counter_increase


creatcounter2 = creatcounter()

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print("2019-5-19")


print(int("12345"))