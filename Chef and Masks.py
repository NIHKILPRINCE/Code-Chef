# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if((a*100)<(b*10)):
        print("DISPOSABLE")
    else:
        print("CLOTH")
