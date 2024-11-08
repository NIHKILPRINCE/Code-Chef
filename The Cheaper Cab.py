# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a>b):
        print("SECOND")
    if(a==b):
        print("ANY")
    if(a<b):
        print("FIRST")
