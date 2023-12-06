t,d=[int(''.join(l.split()[1:]))for l in open(0)]
print(1+int(t/2+(t*t/4-d)**.5)-int(1+t/2-(t*t/4-d)**.5))
