# Write your solution here


list = []

while True:
    words = input("Word: ")
    if words in list:
        print(f"You typed in {len(list)} different words")
        break  
    list.append(words)

