x = int(input())
for i in range(x):
    m, n, o = map(int, input().split())
    if m > o:
        print("0")
    elif m + n <= o:
        print("2")
    else:
        print("1")
