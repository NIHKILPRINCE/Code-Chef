# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if(a>b and a>c):
        print("Alice")
    if(b>a and b>c):
        print("Bob")
    if(c>b and a<c):
        print("Charlie")
