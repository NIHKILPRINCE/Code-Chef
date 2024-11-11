# cook your dish here
temp=0
for _ in range(int(input())):
    a=int(input())
    while(a!=0):
        b=a%10
        temp=temp+b
        a=a//10
    print(temp)
    temp=0
