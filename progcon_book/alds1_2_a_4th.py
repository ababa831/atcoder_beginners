# Accepted
def bubble_sort(a, n):
    num_swap = 0
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                num_swap += 1
    return a, num_swap


def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    a_sorted, num_swap = bubble_sort(a, n)
    # Output
    print(" ".join(map(str, a_sorted)))
    print(num_swap)


if __name__ == '__main__':
    main()