# Accepted
n = int(input())

spoken_words = []
for i in range(n):
    word = input()
    if i >= 1:
        if word in spoken_words or spoken_words[-1][-1] != word[0]:
            print("No")
            exit()
    spoken_words.append(word)
print("Yes")