# Write your solution here

def no_shouting(my_list:list):
    newlist = []
    for i in my_list:
        if i.isupper():
            continue
        else:
            newlist.append(i)
    return newlist

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
