# WA
# Ref: https://qiita.com/ymr-39/items/257e8b9b49d891137d56
# Is this really a insertation sort algorithm ?
def insertation_sort(a, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] >= a[j - 1]:
                break
            else:
                a[j], a[j - 1] = a[j - 1], a[j]
                print(' '.join(a))
    return a


def main():
    # Input
    n = int(input())
    a = input().split()
    # Sort
    insertation_sort(a, n)


if __name__ == '__main__':
    main()