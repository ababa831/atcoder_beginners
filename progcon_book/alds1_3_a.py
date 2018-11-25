# In progress:
# 1 2 + 3 4 - * -> 3 (-3 is the correct answer)
# Something wrong
class Stack(object):
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.current_size = 0
        self.stacked = []

    def push(self, elem):
        if self.is_full():
            print('stack is full!')
        else:
            self.stacked.append(elem)

    def pop(self):
        if self.is_empty():
            print('stack is empty!')
            return None
        else:
            self.current_size = len(self.stacked)
            last_elem = self.stacked[self.current_size - 1]
            del self.stacked[self.current_size - 1]
            return last_elem

    def is_empty(self):
        if self.stacked is []:
            return True
        else:
            return False

    def is_full(self):
        if self.current_size >= self.stack_size:
            return True
        else:
            return False


def calc(val_1, val_2, operator):
    answer = None
    val_1, val_2 = map(int, [val_1, val_2])
    if operator == '+':
        answer = val_1 + val_2
    elif operator == '-':
        answer = val_1 - val_2
    else:
        answer = val_1 * val_2
    return str(answer)


def main():
    # Input
    operation = input().split()
    # Operate
    stack = Stack(stack_size=len(operation))
    operators = set(['+', '-', '*'])
    mid_answer = None
    for elem in operation:
        if elem not in operators:
            stack.push(elem)
        else:
            val_1 = stack.pop()
            val_2 = stack.pop()
            mid_answer = calc(val_1, val_2, elem)
            print(mid_answer)
            stack.push(mid_answer)
    # Output
    answer = stack.pop()
    print(answer)


if __name__ == '__main__':
    main()