# Write your solution here
def same_chars(word,a,b):
    if a >= len(word) or b >= len(word):
        return False
    return word[a] == word[b]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))