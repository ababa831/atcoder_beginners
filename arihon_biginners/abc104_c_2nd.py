D, G = map(int, input().split())
problems = [list(map(int, input().split())) for i in range(D)]


# bit search (1,,,,D)
# May be ascending
for i in range(1 << D):
    for j in range(D):
        # If all problems are solved
        if (i >> j) & 1:
            # WIP
            tmp_score = j * 100 * problems[j][0] + problems[j][1]
            pass
        # If all problems are not solved
        else:
            # WIP
            pass
