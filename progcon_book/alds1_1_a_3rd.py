# Accepted
# Ref: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def insertation_sort(a, n):
    print(' '.join(a))
    for i in range(1, n):
        # Temporary memorize the current value
        # because the value vanishes if shiftings (a[i] = a[i-1]) is executed.
        current_val = a[i]
        # Search the destination of the value
        position = i
        while position > 0 and a[position - 1] > current_val:
            a[position] = a[position - 1]
            position -= 1
        # Insert the current value to the destination
        a[position] = current_val
        print(' '.join(a))


def main():
    # Input
    n = int(input())
    a = input().split()
    # Sort
    insertation_sort(a, n)


if __name__ == '__main__':
    main()