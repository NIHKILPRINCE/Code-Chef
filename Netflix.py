# cook your dish here
x=int(input())
for i in range(0,x):
    a,b,c,d=map(int,input().split())
    if(a+b>=d or a+c>=d or c+b>=d):
        print("YES")
    else:
        print("NO")
