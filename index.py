from support import *
import time as t
k=input("Enter A String : ").upper()
l=0
for i in range(len(k)):
    if(i%11==0 and i>0):
        l=l+1
    tab(120*(i%11)-700,150-l*150)
    if i==0:
        t.sleep(1)
    if k[i]==' ':
        continue
    eval(k[i]+'()')
    
t.sleep(2)
