# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if(a==max(a,b,c)):
        print("SETTER")
    if(b==max(a,b,c)):
        print("TESTER")
    if(c==max(a,b,c)):
        print("EDITORIALIST")
