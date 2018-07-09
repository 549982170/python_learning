#!/usr/bin/python
# coding: UTF-8
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print ' '.join(parts)
print ','.join(parts)
print ''.join(parts)
# 字符串拼接
a = 'Is Chicago'
b = 'Not Chicago?'
print a + ' ' + b
print ('{} {}'.format(a, b))
print a + ' ' + b

a = 'Hello' 'World'
print a

# 不推荐,因为每一次执行+=操作的时候会创建一个新的字符串对象
s = ''
for p in parts:
    s += p
# 利用生成器转换为字符并合并字符串
data = ['ACME', 50, 91.1]
print ','.join(str(d) for d in data)

c = 'c'
# 不推荐
print a + ':' + b + ':' + c  # Ugly
# 推荐
print ':'.join([a, b, c])  # Still ugly


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

for ca in sample():
    print ca
