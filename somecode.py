def solve_riddle():
    for candies in range(100):
        if candies % 2 == 1 and candies % 3 == 1:
            return candies

result = solve_riddle()
print(f'the gnome has {result} candy(ies)')