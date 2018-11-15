# In progress
def bubble_sort(a, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


def selection_sort(a, n):
    for i in range(n - 1):
        min_i = min(a[i:])
        argmin = a.index(min_i)
        a[i], a[argmin] = a[argmin], a[i]
    return a


def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    a_bubbled = bubble_sort(a, n)
    a_selectioned = selection_sort(a, n)
    # Output
    print(" ".join(map(str, a_bubbled)))
    print(" ".join(map(str, a_selectioned)))


if __name__ == '__main__':
    main()