# WA
def selection_sort(a, n):
    num_exchange = 0
    for i, val in enumerate(a):
        # Get a argmin idx
        min_val = min(a[i:])
        min_idx = a.index(min_val)
        if val > min_val:
            # Exchange values for two indexes(min_idx, i)
            tmp_val = val
            a[i] = a[min_idx]
            a[min_idx] = tmp_val
            # Calculate the number of exchanges
            num_exchange += 1
    return a, num_exchange


def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    a, num_exchange = selection_sort(a, n)
    # Output
    print(" ".join(map(str, a)))
    print(num_exchange)


if __name__ == '__main__':
    main()