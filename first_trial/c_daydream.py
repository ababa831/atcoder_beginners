# I coudn't find out at sight
# Use replace function and remove canditate strings to check S=T
# You shoudn't remove "dream" or "dreamer" in first
# e.g.  dreameraser
s = input().replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")
if s:
    print("NO")
else:
    print("YES")