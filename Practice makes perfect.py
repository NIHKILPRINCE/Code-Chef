# cook your dish here
a=list(map(int,input().split()))
c=0
for i in range(4):
    if a[i]>=10:
        c+=1
print (c)
