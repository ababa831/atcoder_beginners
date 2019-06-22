n, x = map(int, input().split())
x_list = list(map(int, input().split()))

# Search all patterns of dumping (1 ~ N-1)
for n_dump in range(1, n):
    # 検索対象が何個あるかわからない（未定，可変）場合の実装法がわからん
    # こういう場合．乱数で係数生成して，逐一勾配方向求めて，最適化計算しないといけないのでは？
    # それか何かしらの数理的法則性を求めるか・・・
    for i in range()