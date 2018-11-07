def selection_sort(a, n):
    for i, val in enumerate(a):
        # Get a argmin idx
        min_idx = argmin(a[i:])
        # Exchange values for two indexes(min_idx, i)
        tmp_val = val
        a[i] = a[min_idx]
        a[min_idx] = tmp_val
        # Calculate the number of exchange
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