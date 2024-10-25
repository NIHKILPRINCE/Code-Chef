# cook your dish here
x=int(input())
for i in range(0,x):
    m,n,o= map(int, input().split())
    if(m+n==o):
        print("YES")
    else:
        print("NO")
