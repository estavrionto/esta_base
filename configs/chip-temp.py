#!/usr/bin/env python3
import subprocess
import re


# sensors|grep edge|sed -e 's/.*  +\(.*\)°C  .*/\1/'

def sh(Command):
    return subprocess.check_output(Command,shell=True,universal_newlines=True,
    # stderr=None,
    stderr=subprocess.STDOUT,
    )

t = sh(['sensors'])
t = t.split('\n\n')

cpus = ['k10temp','coretemp']
gpus = ['amdgpu']


for i in t:
    j = i.split('\n')[0]
    for d in cpus:
        if d in j:
            # print('cpu',j)
            str_cpu = i
    for d in gpus:
        if d in j:
            # print('gpu',j)
            str_gpu = i
    # print([i[0]])
# print([t])



# t = sh(['sensors'])
# t = t.split('\n')
# t = [i for i in t if 'edge' in i][0]
# t = t.split('+')[1]
# GPU = t.split('°C ')[0]

# t = sh(['sensors'])
# t = t.split('\n')
# t = [i for i in t if 'Package id 0:' in i][0]
# t = t.split('+')[1]
# CPU = t.split('°C ')[0]

# p = f'cpu:{CPU}°C, gpu:{GPU}°C'
# # print(GPU,CPU)
# print(p)


# r'-?\d+(?:\.\d+)?\s*°\s*c'
def extract_T(s):
    # s = s.split('\n')
    s = re.split(' |\n', s)
    s = [i for i in s if '°C' in i]

    # s = s.split('°C')
    # print(s)
    return s[0]

# s = 'This is some temperature 30° c - 50 ° c  2°c  34.5 °c 30°c - 40 °c and "30° - 40, and -45.5° - -56.5° range' 
# tb = r'-?\d+(?:\.\d+)?(?:\s*°(?:\s*c)?)?'
# rx = r'{0}(?:\s*-\s*{0})?'.format(tb)
# results = re.findall(rx, str_gpu)
# print(results)

print(f'cpu:{extract_T(str_cpu)}, gpu:{extract_T(str_gpu)}')
