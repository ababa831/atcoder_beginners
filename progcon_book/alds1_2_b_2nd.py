# Accepted
def selection_sort(a, n):
    num_exchange = 0
    for i in range(n - 1):
        min_j = i
        for j in range(i, n):
            if a[j] < a[min_j]:
                min_j = j
        tmp = a[i]
        a[i] = a[min_j]
        a[min_j] = tmp
        if i != min_j:
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