# In progress
def insertation_sort(a, n):
    sorted_list = a[0]
    for i in rang(1, n):
        v = a[i]
        for j, val in enumerate(sorted_list):
            if val > v:
                sorted_list = sorted_list[:j] + [v] + sorted_list[j:]
                a = sorted_list + a[i:]
        print(' '.join(a))
    return a


def main():
    # Input
    n = int(input())
    a = input().split()
    # Sort
    a = insertation_sort(a, n)
    # Output (final result)
    print(" ".join(a))

if __name__ == '__main__':
    main()
