list = ["red", "green", "green", "yellow", "red"]
print("Original list is ",list)
char_count = {}

for color in list:
    if color in char_count:
        char_count[color] += 1
    else:
        char_count[color] = 1

list = [color for color in list if char_count[color] == 1]
print("Final list is ",list)
