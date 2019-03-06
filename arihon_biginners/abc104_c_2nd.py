# WIP
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for i in range(D)]


# bit search (1,,,,D)
# May be ascending
min_num_solved_probrems = 1000000
for i in range(1 << D):
    tmp_score = 0
    num_solved_probrems = 0
    for j in range(D):
        # If all problems are solved
        if (i >> j) & 1:
            tmp_score += j * 100 * problems[j][0] + problems[j][1]
        # If all problems are not solved
        else:
            tmp_score += 0
        num_solved_probrems += 1
    # Judge if you reach the target score
    if num_solved_probrems >= G:
        min_num_solved_probrems = \
            min(min_num_solved_probrems, num_solved_probrems)
    else:
        # TODO: write codes of solving problems halfway
        pass
