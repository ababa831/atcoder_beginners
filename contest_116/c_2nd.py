# AC
from collections import deque

N = int(input())
hhh = list(map(int, input().split()))

# Initial settings
stack = deque()
stack.append(hhh)
n_operation = 0


def operation():
    global stack, n_operation

    flower_heights = stack.pop()
    args_zero_height = [i for i, v in enumerate(flower_heights) if v == 0]
    
    if args_zero_height == []:  # If there is no zero elem.
        flower_heights_minus1 = list(map(lambda x: x-1, flower_heights))
        n_operation += 1
        stack.append(flower_heights_minus1)
    else:  # If there are zero elems
        last_arg_zero = -1
        for i, arg in enumerate(args_zero_height):
            if i == 0:
                # Rightside
                non_zero_heights = flower_heights[:arg]
            else:
                # Middle
                non_zero_heights = flower_heights[last_arg_zero+1:arg]

            if non_zero_heights != []:
                non_zero_heights_minus1 = \
                    list(map(lambda x: x-1, non_zero_heights))
                n_operation += 1
                stack.append(non_zero_heights_minus1)
            last_arg_zero = arg
        # Add leftside
        if last_arg_zero < len(flower_heights)-1:
            non_zero_heights = flower_heights[last_arg_zero+1:]
            # The fucking code (DRY)
            non_zero_heights_minus1 = \
                list(map(lambda x: x-1, non_zero_heights))
            n_operation += 1
            stack.append(non_zero_heights_minus1)


# Do operations while stack is not empty
while stack:
    operation()

print(n_operation)
