# cook your dish here
x=int(input())
for i in range(x):
    m=int(input())
    if(m<=70):
        print("0")
    elif(m>70 and m<=100):
        print("500")
    else:
        print("2000")
