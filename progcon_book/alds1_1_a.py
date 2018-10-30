# Accepted
# O(N^2) algorithm
def insertation_sort(a, n):
    # print initial order
    print(" ".join(map(str, a)))
    for i in range(1, n):
        """
        v: insertation target
        j: one element of conparision pair
        j+1: index of insertation target

        Visualization reference: https://visualgo.net/en/sorting
        """
        # Sorting
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v

        # Output of result (in progress)
        print(" ".join(map(str, a)))


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    insertation_sort(a_list, n)


if __name__ == '__main__':
    main()