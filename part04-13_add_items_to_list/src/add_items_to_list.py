# Write your solution here
size = int(input("How many items: "))
list = []
i = 1
while i <= size:
    item = int(input(f"item{i}: "))
    list.append(item)
    i += 1
    if i > size:
        break
print(list)