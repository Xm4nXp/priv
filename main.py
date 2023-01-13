import re,os,time,sys
from concurrent.futures import ThreadPoolExecutor
print("SCRIPT BY XM4NXP")
print("TELE : @xm4nxp")
def t():
    x = input('File : ')
    c = open(x,'r',).read().splitlines()
    with ThreadPoolExecutor(max_workers=40) as (bf):
        bf.submit(gas,c)

def gas(c):
    for v in c:
        z = v.split('.')
        if len(z) == 3:
            h = f'{z[1]}.{z[2]}'
            open('result-1.txt','a').write(h+'\n')
            print(h)
        elif len(z) == 4 or len(z) == 5:
            h = f'{z[2]}.{z[3]}'
            open('again.txt','a').write(v+'\n')
        else:
            h = f'{z[0]}.{z[1]}'
            open('result-1.txt','a').write(h+'\n')
            print(h)
if __name__ == '__main__':
    t()