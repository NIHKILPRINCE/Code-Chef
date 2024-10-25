# cook your dish here
x=int(input())
for i in range(0,x):
    m=int(input())
    if(m<3):
        print("LIGHT")
    if(m>=3 and m<7):
        print("MODERATE")
    if(m>=7):
        print("HEAVY")
