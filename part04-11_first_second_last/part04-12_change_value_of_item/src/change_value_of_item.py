# Write your solution here

my_list = [1, 2, 3, 4, 5]
index = 0
while index >= 0:
    index = int(input("Index: "))
    val = int(input("New value: "))
    my_list[index] = val
    if index == -1:
        break
    print(my_list)