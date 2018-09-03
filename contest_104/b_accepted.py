"""
Accepted, but awkward thinking and I could not recall how to:
- count specific characters such as "A", "C"
- filter strings which do not have upper letter without "A", "C"

The solutions were searched.
"""
s = list(input())

if "A" != s[0]:
    print("WA")
    exit()
s_extracted = s[2:-1]
if s_extracted.count("C") != 1:
    print("WA")
    exit()

# Get Upper characters without "A", "C"
s_upper = [
    chara for chara in s if chara != "C" and chara != "A" and chara.isupper()
]
if len(s_upper) > 0:
    print("WA")
    exit()

print("AC")

# A sample answer using regular expression
"""
import re
print("AC" if re.match("A[a-z]+C[a-z]+$",input()) else "WA")
"""