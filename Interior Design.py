# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if((a+b)<(c+d)):
        print(a+b)
    else:
        print(c+d)
