# answers of programming probrems written in 
# "プログラミングコンテスト攻略のためのアルゴリズムとデータ構造"

# 2.2 Top 3
# 10人分のプレイヤーの得点が記録されたデータを読み込んで，
# その中から上位3人の得点を順に出力してください．ただし，得点は100点満点とします．
# 入力例： 25 36 4 55 71 18 0 71 89 65
# 出力例： 89 71 71
scores = sorted(map(int, input().split()), reverse=True)
print(scores[0], scores[1], scores[2])
