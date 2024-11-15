# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if(10*a>=b):
        print(b*c)
    else:
        print((10*a)*c)
