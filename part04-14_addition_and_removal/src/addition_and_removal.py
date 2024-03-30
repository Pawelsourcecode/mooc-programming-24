# Write your solution here

list = []
while True:
    print(f"The list is now {list}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == "d":
        # Value of item is length of list + 1
        item = len(list) + 1
        list.append(item)
    elif option == "r":
        list.pop(len(list) - 1)
    elif option == "x":
        print("Bye!")
        break
    else:
        continue

