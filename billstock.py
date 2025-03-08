#Buy and sell stock.
#Given a list of ending bell stock prices for n days, compute the maximum profit from buying on a day and selling on any day after the buy operation.

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
