# Write your solution here
def greatest_number(a,b,c):
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c)

    return max(list1)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)