# cook your dish here
a,b=map(float,input().split())
c=b-a
if(a%5==0 and c>=0.5):
    print(b-(a+0.5))
else:
    print(b)
