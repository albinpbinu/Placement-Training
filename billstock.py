prices=[]
n=int(input("Enter the number of days: "))
for i in range(n):
    k=float(input())
    prices.append(k)
minprice=float('inf')
maxprofit=0
for i in prices:
    minprice=min(minprice,i)
    maxprofit=max(maxprofit,i-minprice)
print(maxprofit)
