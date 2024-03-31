# Write your solution here

def sum_of_positives(my_list:list):
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i
    return sum

    