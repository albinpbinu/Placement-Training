n=int(input())
l=[]
i=1
while(i<=n):
    m=int(input())
    l.append(m)
    i=i+1
tsum=sum(l)
avg=float(tsum/n)
print("The average is: {:.2f}".format(avg))
