# Accepted
a, b, k = map(int, input().split())

n_takahashi = a
n_aoki = b
for i in range(k):
    if i % 2 == 0:
        # Takahashi
        if n_takahashi % 2:
            n_takahashi -= 1
        n_aoki += n_takahashi / 2
        n_takahashi = n_takahashi / 2
    else:
        if n_aoki % 2:
            n_aoki -= 1
        n_takahashi += n_aoki / 2
        n_aoki = n_aoki / 2

print(int(n_takahashi), int(n_aoki))