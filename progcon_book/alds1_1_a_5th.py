# Accepted
def insertation_sort(a, n):
    for i in range(n):
        # Memorize the a[i] for an insetation
        target_val = a[i]
        target_idx = i
        while target_idx > 0 and a[target_idx - 1] > target_val:
            # Shift up the value
            a[target_idx] = a[target_idx - 1]
            target_idx -= 1
        # Insert to the destination
        a[target_idx] = target_val
        # Show the swapped list "a"
        print(" ".join(map(str, a)))


def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    insertation_sort(a, n)


if __name__ == '__main__':
    main()
