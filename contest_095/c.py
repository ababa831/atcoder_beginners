# AC

A, B, C, X, Y = map(int, input().split())

cost = 0
if A + B > 2 * C:
    n_purchase_surplus = 2 * max(X, Y)
    cost_surplus = n_purchase_surplus * C
    if X >= Y:
        n_purchase = 2 * Y
        cost = n_purchase * C
        n_remaining = X - Y
        cost += n_remaining * A
    else:
        n_purchase = 2 * X
        cost = n_purchase * C
        n_remaining = Y - X
        cost += n_remaining * B
    # select minimum cost
    cost = min(cost_surplus, cost)
else:
    cost = (X * A) + (Y * B)
print(cost)
