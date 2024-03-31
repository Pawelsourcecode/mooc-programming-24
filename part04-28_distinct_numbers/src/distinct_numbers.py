# Write your solution here

def distinct_numbers(my_list:list):
    results = []
    for i in my_list:
        if i not in results:
            results.append(i)

    results.sort()
    return results

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]