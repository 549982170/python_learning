#!user/bin/python
# encoding:utf-8
# print'\n'.join([''.join([('PYTHON!'[(x-y)%7]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])
#
# print'\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else' 'for x in range(-80,20)])for y in range(-20,20)])

# _=[__import__('sys').stdout.write("\n".join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n===\n") for vec in __import__('itertools').permutations(xrange(8)) if 8 == len(set(vec[i]+i for i in xrange(8))) == len(set(vec[i]-i for i in xrange(8)))]

print sum(map(int, str(2**1000)))
