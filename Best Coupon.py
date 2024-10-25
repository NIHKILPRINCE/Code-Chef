#cook your dish here
x = int(input())
for i in range(x):
    m = int(input())
    y = m //10
    z = min(m, 100)
    print(max(y, z))
