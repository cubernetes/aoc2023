t,d=[int(''.join(l.split()[1:]))for l in open(0)]
f=lambda n:int((n<0)+t/2+n*(t*t/4-d)**.5)
print(1+f(1)-f(-1))
