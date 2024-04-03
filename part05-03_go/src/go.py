# Write your solution here

def who_won(game_board:list):
    counter1 = 0
    counter2 = 0
    for i in game_board:
        for j in i:
            if j == 1:
                counter1 += 1
            elif j == 2:
                counter2 += 1
    if counter1 > counter2:
        return 1
    elif counter2 > counter1:
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    go = [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(who_won(go))