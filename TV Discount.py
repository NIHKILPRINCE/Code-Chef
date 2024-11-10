# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    e,f=(a-c),(b-d)
    if(e<f):
        print("FIRST")
    if(e>f):
        print("SECOND")
    if(e==f):
        print("ANY")
