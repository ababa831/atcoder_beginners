# In progress
# I do not know how to code `is_stable` for sorting algorithms
def bubble_sort(a, n):
    for i in range(n - 1):
        len_aj = len(a[i:])
        for j in reversed(range(i, n)):
            if j <= len_aj:
                if a[j] < a[j + 1]:
                    tmp_aj = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = a[j]
    return a


def selection_sort(a, n):
    for i in range(1, n - 1):
        min_val = min(a[i + 1])
        min_idx = a.index(min_val)
        if min_val < a[i]:
            tmp_ai = a[i]
            a[i] = min_val
            a[min_idx] = tmp_ai
    return a


def main():
    # Input
    n = int(input())
    a = list(map(int, input().split()))
    # Sort
    a_bubble_sorted = bubble_sort(a, n)
    a_selection_sorted = selection_sort(a, n)
    # out
    print(" ".join(map(str, a_bubble_sorted)))
    # TODO:print(is_stable)
    print(" ".join(map(str, a_selection_sorted)))
    # TODO:print(is_stable)



if __name__ == '__main__':
    main()