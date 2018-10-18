# Accepted
x, y, z = map(int, input().split())

tmp_sitnum = int(x / (z + y))
if x % (z + y) >= z:
    print(tmp_sitnum)
else:
    print(tmp_sitnum - 1)