# cook your dish here
x=int(input())
for i in range(x):
    m,n=map(int,input().split())
    if((m*1.07)>=n):
        print("YES")
    else:
        print("NO")
        
