# cook your dish here
x=int(input())
for i in range(x):
    w,x,y,z=map(int,input().split())
    if((w+(y*z))>x):
        print("overflow")
    if((w+(y*z))==x):
        print("filled")
    if((w+(y*z))<x):
        print("unfilled")
