# Write your solution here

def no_vowels(my_string:str):
    vowels = ["a","e","i","o","u"]
    word = ""
    for i in my_string:
        if i in vowels:
            i = ""
        word += i
    return word


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))