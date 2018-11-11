# WA (Test case 4)
# The output seems to be a correct answer but scored as wrong
# I do not know where I made a mistake
def selection_sort(a, n):
    num_swap = 0
    a_len = len(a)
    for i in range(n - 1):
        if a_len == 0:
            break
        min_val = min(a[i + 1:])
        min_idx = a.index(min_val)
        if a[i] > min_val:
            tmp_val = a[i]
            a[i] = min_val
            a[min_idx] = tmp_val
            # Record the number of swapping
            num_swap += 1
    return a, num_swap


def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    a, num_swap = selection_sort(a, n)
    # Output
    print(" ".join(map(str, a)))
    print(num_swap)


if __name__ == '__main__':
    main()