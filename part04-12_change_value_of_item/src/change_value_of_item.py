# Write your solution here

my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    
    if index == -1:
        break
    if index < 0 or index >= len(my_list):
        print("Out of range")
        continue
    val = int(input("New value: "))
    my_list[index] = val
    print(my_list)