# Write your solution here
number = int(input("Please type in a positive integer: "))

for number in range(-number,number+1,1):
    if number != 0:
        print(number)

