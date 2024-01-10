a=int(input('Enter number for number series:-'))
c=0
s=0
for i in range(0,a):
    c=(c*10)+2
    if i<a-1:
        print(c,end="+")
    else:
         print((c*10)+2,end="=")
    s=s+c
print(s)
    
