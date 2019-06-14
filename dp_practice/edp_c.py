# AC
N = int(input())

a_sum_last, b_sum_last, c_sum_last = 0, 0, 0
for _ in range(N):
    a_today, b_today, c_today = map(int, input().split())
    a_tomorrow = a_today + max(b_sum_last, c_sum_last)
    b_tomorrow = b_today + max(a_sum_last, c_sum_last)
    c_tomorrow = c_today + max(a_sum_last, b_sum_last)
    
    # Update
    a_sum_last = a_tomorrow
    b_sum_last = b_tomorrow
    c_sum_last = c_tomorrow

print(max(a_sum_last, b_sum_last, c_sum_last))
