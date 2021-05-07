n=int(input("enter the value "))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(str(a)+"\n"+str(b))
    for i in range(n-2):
        f=int(a+b)
        a=b
        b=f
        print(f)
