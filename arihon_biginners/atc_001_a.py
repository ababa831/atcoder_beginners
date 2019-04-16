class DFSTool(object):
    def __init__(self, H, W, stage_info):
        self.already_passed = []
        self.H = H
        self.W = W
        # Information of a stage map gotten from inputs
        # e.g.[[p_00,...,p_0W-1],...,[p_H-10,...,p_H-1W-1]]
        self.stage_info = stage_info

    def is_not_in_road(self, x, y):
        out_of_w = x >= self.W or x < 0
        out_of_h = y >= self.H or y < 0
        if out_of_w or out_of_h:
            return True
        # 2 stage condition branching to avoid ValueError
        elif self.stage_info[y][x] == '#':
            return True
        else:
            return False

    def is_goal(self, x, y):
        return self.stage_info[y][x] == 'g'

    def dfs(self, x, y):
        if self.is_not_in_road(x, y):
            return
        elif self.is_goal(x, y):
            print('Yes')
            exit()
        elif [x, y] in self.already_passed:
            return
        else:
            self.already_passed.append([x, y])
            self.dfs(x+1, y)
            self.dfs(x-1, y)
            self.dfs(x, y+1)
            self.dfs(x, y-1)


if __name__ == "__main__":
    # RE
    H, W = map(int, input().split())
    # Register the stage infomation and the start point
    stage_info = []
    x_s, y_s = None, None
    for y_i in range(H):
        row = list(input())
        if 's' in row:
            x_s = row.index('s')
            y_s = y_i
        stage_info.append(row)
    # DFS Start
    dfstool = DFSTool(H, W, stage_info)
    dfstool.dfs(x_s, y_s)
    # If you cannot find the paths to goal
    print('No')
