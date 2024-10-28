# cook your dish here
x=int(input())
for i in range(x):
    m,n=map(int,input().split())
    if(m>n):
        print("0")
    else:
        print(n-m)
