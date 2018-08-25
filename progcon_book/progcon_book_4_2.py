# answers of programming probrems written in 
# "プログラミングコンテスト攻略のためのアルゴリズムとデータ構造"

# 4.2 ALDS1_3_A: Stack (reverse Polish notation)
input_list = list(input().split())
operator = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: float(x) / y
}
stack = []
for val in input_list:
    if val not in ["+", "-", "*", "/"]:
        stack.append(int(val))
    else:
        # Note: Last In First Out (Be aware of the order) 
        y = stack.pop()
        x = stack.pop()
        stack.append(operator[val](x, y))
print(stack[0])