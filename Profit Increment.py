for _ in range(int(input())):
    a,b=map(int,input().split())
    c=a+(a*0.10)
    print(int(c-(a-b)))
