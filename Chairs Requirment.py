# cook your dish here
x=int(input())
for i in range(0,x):
    m,n=map(int,input().split())
    if(m>=n):
        print(m-n)
    else:
        print("0")
