# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a<b):
        print("REPAIR")
    if(a>b):
        print("NEW PHONE")
    if(a==b):
        print("ANY")
