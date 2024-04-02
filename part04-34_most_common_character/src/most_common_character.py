# Write your solution here

def most_common_character(stringg):
    most_common = stringg[0]
    for character in stringg:
        if stringg.count(character) > stringg.count(most_common):
            most_common = character
        
    return most_common


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))