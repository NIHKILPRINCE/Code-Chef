# cook your dish here
x=int(input())
for i in range(0,x):
    m,n=map(int,input().split())
    if(n<=m):
        print("No")
    else:
        print("YES")
