# Accepted
def get_new_lucas(l_i_1, l_i_2):
    """
    get a new Lucas number L_i

    l_i_1: L_(i-1),
    l_i_2: L_(i-2)
    """
    return l_i_1 + l_i_2


def main():
    n = int(input())
    tmp_l_i_1 = 1
    tmp_l_i_2 = 2
    for i in range(n):
        if i == 0:
            new_lucas_num = 1
        if i >= 1:
            new_lucas_num = get_new_lucas(tmp_l_i_1, tmp_l_i_2)
            tmp_l_i_2 = tmp_l_i_1
            tmp_l_i_1 = new_lucas_num
        
    print(new_lucas_num)


if __name__ == '__main__':
    main()