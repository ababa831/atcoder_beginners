# Accepted
def bubble_sort(a_list, len_list):
    num_reverse = 0
    for i in range(1, len_list + 1):
        for j in range(len_list - i):
            if a_list[-j - 2] > a_list[-j - 1]:
                tmp_elem = a_list[-j - 2]
                a_list[-j - 2] = a_list[-j - 1]
                a_list[-j - 1] = tmp_elem
                num_reverse += 1
    return a_list, num_reverse


def main():
    # Input
    n = int(input())
    a_list = list(map(int, input().split()))
    # Do bubble sort
    a_list_rev, num_reverse = bubble_sort(a_list, n)
    # Output
    print(" ".join(map(str, a_list_rev)))
    print(num_reverse)


if __name__ == '__main__':
    main()