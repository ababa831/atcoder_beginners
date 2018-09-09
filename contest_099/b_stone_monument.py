# Accepted, But long thinking
a, b = map(int, input().split())

for t_a in range(1, 1000):
    # Tower A hight
    h_a = sum([t_part for t_part in range(t_a + 1)])
    # A canditate of snow hight
    s_a = h_a - a
    if s_a >= 1:
        t_b = t_a + 1
        # Tower B hight
        h_b = sum([t_part for t_part in range(t_b + 1)])
        s_b = h_b - b
        if s_b >= 1:
            if s_a == s_b:
                print(s_a)
                exit()