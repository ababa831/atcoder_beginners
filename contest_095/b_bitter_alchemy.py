n, x = map(int, input().split())
m_list = list(map(int, [input() for _ in range(n)]))

m_sum = sum(m_list)
x_residue = x - m_sum
n_add_donuts = int(x_residue / min(m_list))

print(n + n_add_donuts)