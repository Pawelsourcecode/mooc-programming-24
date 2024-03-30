# Write your solution here

list = []

while True:
    word = int(input("New item: "))
    list.append(word)
    if word == 0:
        print("Bye!")
        break
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")
    