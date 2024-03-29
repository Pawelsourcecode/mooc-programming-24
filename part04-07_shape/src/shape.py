# Copy here code of line function from previous exercise and use it in your solution
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
def shape(size,triangle_char,rect_height,rect_char):
    d = 1
    while d <= size:
        line(d, triangle_char)
        d += 1
    for _ in range(rect_height):
        line(size,rect_char)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")