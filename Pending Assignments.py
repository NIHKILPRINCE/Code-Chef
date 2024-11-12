# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if(a*b>c*24*60):
        print("NO")
    else:
        print("YES")
