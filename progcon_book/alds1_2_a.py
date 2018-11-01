# Accepted
def bubble_sort(a, n):
    # If a reversed neighbor element exists
    exist_rev_neighbor = True
    num_exchanged = 0
    while exist_rev_neighbor:
        exist_rev_neighbor = False
        for i in reversed(range(1, n)):
            if a[i] < a[i - 1]:
                # exchange elements
                tmp_a_i = a[i]
                a[i] = a[i - 1]
                a[i - 1] = tmp_a_i

                exist_rev_neighbor = True
                num_exchanged += 1
    return a, num_exchanged


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    rev_a, num_exchanged = bubble_sort(a_list, n)
    print(" ".join(map(str, rev_a)))
    print(num_exchanged)


if __name__ == '__main__':
    main()