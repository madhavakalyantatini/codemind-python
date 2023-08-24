n=int(input())
sm = 0
total = 0
for i in range(1,n+1):
    sm+=(i*i)
    total+=i
sm = (total*total) - sm
print(sm)
    