def insertation_sort(a, n):
    for i in range(n):
        # Memorize the val for the insertation
        target_val = a[i]
        target_idx = i
        # Shift values until an insertation destination is detected
        while target_idx > 0 and a[target_idx - 1] > target_val:
            a[target_idx] = a[target_idx - 1]
            target_idx -= 1
        # Insert the memorized target value
        a[target_idx] = target_val
        # Show a progress result
        print(' '.join(map(str, a)))

def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    insertation_sort(a, n)


if __name__ == '__main__':
    main()