def insertation_sort(a_list, n):
    for i in range(1, n):
        target_val = a_list[i]
        j = i - 1
        while j >= 0 and a_list[j] >= target_val:
            a_list[j + 1] = a_list[j]
            j -= 1
        a_list[j + 1] = target_val


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    insertation_sort(a_list, n)


if __name__ == '__main__':
    main()