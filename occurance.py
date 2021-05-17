inp=input('Please enter a string \n')
alphabet=set(inp)
out_put={}
c=0
for _ in alphabet:
    for i in inp:
        if i==_:
            c=c+1
    out_put[_]=c
    c=0
print(out_put)
