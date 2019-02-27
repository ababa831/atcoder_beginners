D, G = map(int, input().split())
problems = [list(map(int, input().split())) for i in range(D)]


# TODO:
# bit search (1,,,,D)
# May be ascending
for i in range(1 << D):
    for j in range(D):
        # If all problems are solved
        
        # If all problems are not solved
