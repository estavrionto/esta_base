#!/usr/bin/env python3
import subprocess

def sh(Command):
    return subprocess.check_output(Command,shell=True,universal_newlines=True)
import sys
import json

# print('test')

t = 'du -h -d 1 .|sort -h -r'
t = [i.split('\t') for i in sh(t).split('\n')]
t = [[j for j in i if j != ''] for i in t]
t = [i for i in t if i !=[]]
# for i in t:
#     print(i)    
# exit()

total = t[0][0]
t = t[1:]
s ={i[1][2:]: i[0] for i in t}


# for i in s:
#     print(s[i],i)
# print()
# exit()

# for files
t = 'ls -Alh --sort=size | grep -v "^d"'
t = [i.split(' ') for i in sh(t).split('\n')]
# print(t)

t = [[j for j in i if j != ''] for i in t]
f = [i for i in t if len(i)>5]


# for i in f:
#     print(i)
# print()
# exit()

t = 'ls -Alh | grep "^d"| sort -h'
t = [i.split(' ') for i in sh(t).split('\n')]
t = [[j for j in i if j != ''] for i in t]
t = [i for i in t if len(i)>5]
t = [i[:8]+[' '.join(i[8:])] for i in t]
# for i in t:
#     print(i)
# print()
# exit()

d = {i[-1]:i for i in t}

# for i in d:
#     print(d[i],i)
# print()
# exit()


a = []
for i in s:
    ii = d[i]
    ii = ii[:4]+[s[i]]+ii[5:]
    a.append(ii)

a = a+f

print(f'total {total}')

for i in a:
    print('\t'.join(i))
