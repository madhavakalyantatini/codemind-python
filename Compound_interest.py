def compound_interest(o, r, t):
	Amount = o * (pow((1 + r / 100) ,t))
	print(f"{Amount:.2f}")
   
o,r,t=map(int,input().split())
# compound_interest(o, r, t)
Amount = o * (pow((1 + r / 100) ,t))
print(f"{Amount:.2f}")
