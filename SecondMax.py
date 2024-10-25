x=int(input())
for i in range(0,x):
    a, b, c = map(int, input().split())
    print(sorted([a, b, c])[-2])

