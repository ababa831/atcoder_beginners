# WIP
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for i in range(D)]


# bit search (1,,,,D)
# May be ascending
min_num_solved_problems = 1000000
for i in range(1 << D):
    tmp_score = 0
    num_solved_problems = 0
    for j in range(D):
        # If all problems are solved
        if (i >> j) & 1:
            tmp_score += j * 100 * problems[j][0] + problems[j][1]
        num_solved_problems += problems[j][0]
    # Judge if you reach the target score
    if num_solved_problems >= G:
        min_num_solved_problems = \
            min(min_num_solved_problems, num_solved_problems)
    else:
        # TODO: write codes of solving problems halfway
        pass

print(num_solved_problems)
