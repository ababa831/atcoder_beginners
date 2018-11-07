# Accepted
def bubble_sort(a_list, n):
    num_reverse = 0
    for i in range(n):
        for j in range(n - i - 1):
            # With a for roop (reversed order), 
            # index starts  -1, -2 ,...,
            # NOT -0, -1, ...
            if a_list[-j - 2] > a_list[-j - 1]:
                tmp_elem = a_list[-j - 1]
                a_list[-j - 1] = a_list[-j - 2]
                a_list[-j - 2] = tmp_elem
                num_reverse += 1
    return a_list, num_reverse


def main():
    # Input
    n = int(input())
    a_list = list(map(int, input().split()))
    # Sort
    a_list_reversed, num_reverse = bubble_sort(a_list, n)
    # Output
    print(" ".join(map(str, a_list_reversed)))
    print(num_reverse)


if __name__ == '__main__':
    main()