# Accepted
def bubble_sort(a, n):
    a_b = a.copy()
    for i in range(n):
        for j in range(n - 1, i, -1):
            # Do not miss [1] on the comparisons
            if a_b[j][1] < a_b[j - 1][1]:
                a_b[j], a_b[j - 1] = a_b[j - 1], a_b[j]
    return a_b


def selection_sort(a, n):
    a_s = a.copy()
    for i in range(n - 1):
        tmp_a = [elem[1] for elem in a_s[i + 1:]]
        min_i = min(tmp_a)
        argmin = tmp_a.index(min_i)
        # Do not miss [1] on the comparisons
        if a_s[i][1] > a_s[argmin + i + 1][1]:
            # Note: an argmin index is counted from a_s[0] 
            # -> Correct indexing: "argmin + i + 1"
            a_s[i], a_s[argmin + i + 1] = a_s[argmin + i + 1], a_s[i]
    return a_s


def main():
    # Input
    n = int(input())
    a = list(input().split())
    # Sort
    a_bubbled = bubble_sort(a, n)
    a_selectioned = selection_sort(a, n)
    # Output
    print(" ".join(a_bubbled))
    print("Stable")  # Bubble sort is always stable
    print(" ".join(a_selectioned))
    # Judge if the selection sort is stable
    if a_selectioned == a_bubbled:
        print("Stable")
    else:
        print("Not stable")


if __name__ == '__main__':
    main()