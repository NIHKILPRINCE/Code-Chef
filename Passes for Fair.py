# cook your dish here
x=int(input())
for i in range(x):
    m,n=map(int,input().split())
    if(n>m):
        print("YES")
    else:
        print("NO")
