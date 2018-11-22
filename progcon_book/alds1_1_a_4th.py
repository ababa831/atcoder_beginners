# Accepted
def insertation_sort(a, n):
    for i in range(n):
        selected_val = a[i]
        search_idx = i
        while search_idx > 0 and a[search_idx - 1] > selected_val:
            a[search_idx] = a[search_idx - 1]
            search_idx -= 1
        a[search_idx] = selected_val
        print(' '.join(map(str, a)))


def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    insertation_sort(a, n)


if __name__ == '__main__':
    main()
