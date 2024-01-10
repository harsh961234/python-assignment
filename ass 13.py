def sum_between_2(x,y):
    if(x==y):
        return x
    else:
        return x+ sum_between_2((x-1),y)


a=int(input("Enter a first value:"))
b=int(input("Enter the second value:"))

if(a>b):
    print("sumof value between",a,"and",b,"is",sum_between_2(a,b))
else:
    print("sumof value between",a,"and",b,"is", sum_between_2(b,a))
