t=int(input())
container=[]
for i in range(t):
    a,b,c=map(int,input().split())
    if a+b==c or a+c==b or b+c==a:
        container.append("YES")
    else:
        container.append("NO")
for i in container:
    print(i)
