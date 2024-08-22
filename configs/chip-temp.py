#!/usr/bin/env python3
import subprocess


# sensors|grep edge|sed -e 's/.*  +\(.*\)°C  .*/\1/'

def sh(Command):
    return subprocess.check_output(Command,shell=True,universal_newlines=True)




t = sh(['sensors'])
t = t.split('\n')
t = [i for i in t if 'edge' in i][0]
t = t.split('+')[1]
GPU = t.split('°C ')[0]

t = sh(['sensors'])
t = t.split('\n')
t = [i for i in t if 'Package id 0:' in i][0]
t = t.split('+')[1]
CPU = t.split('°C ')[0]

p = f'cpu:{CPU}°C, gpu:{GPU}°C'
# print(GPU,CPU)
print(p)