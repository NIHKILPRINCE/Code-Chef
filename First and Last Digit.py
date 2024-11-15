#cook your dish here
for _ in range(int(input())):
    n = int(input())
    first_digit = int(str(n)[0])
    last_digit = n % 10
    print(first_digit+last_digit)
