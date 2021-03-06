# Accepted
# Memo:
# - a land -> 'YES'
# - two or more lands ->
#   Convert a sea point to a land one
#   and check if there is a land on the map using DFS
from collections import deque
from copy import deepcopy


class FillUpper(object):
    def __init__(self, landsea_map, one_side=10):
        self.stack = deque()
        self.searched_points = []
        self.one_side = one_side
        self.landsea_map = landsea_map
        """
        If DFS was finished and map_for_dfs == land_sea_map
        -> 'YES'
        """
        # DO NOT WRITE map_for_dfs as:
        # self.map_for_dfs = [['x'] * one_side] * one_side
        self.map_for_dfs = [['x'] * one_side for _ in range(one_side)]
        self.n_fillupped = 0

    def fillup(self, point):
        if not self._is_land_point(point):
            self.landsea_map[point[1]][point[0]] = 'o'
            self.n_fillupped += 1

    def DFS(self):
        point = self.stack.pop()
        if not self._is_in_the_map(point):
            return
        elif not self._is_land_point(point):
            return
        elif point in self.searched_points:
            return
        else:
            self.map_for_dfs[point[1]][point[0]] = 'o'
            self.searched_points.append(point)
            self.stack.append([point[0] + 1, point[1]])
            self.stack.append([point[0] - 1, point[1]])
            self.stack.append([point[0], point[1] + 1])
            self.stack.append([point[0], point[1] - 1])

    def clear_map_for_dfs(self):
        self.map_for_dfs = [['x'] * one_side] * one_side

    def _is_in_the_map(self, point):
        in_the_xrange = 0 <= point[0] < self.one_side
        in_the_yrange = 0 <= point[1] < self.one_side
        if in_the_xrange and in_the_yrange:
            return True
        else:
            return False

    def _is_land_point(self, point):
        if self.landsea_map[point[1]][point[0]] == 'o':
            return True
        else:
            return False


if __name__ == "__main__":
    # 1. Input
    one_side = 10
    landsea_map = [list(input()) for _ in range(one_side)]
    # 2. Full search and DFS to judge there is a land for every points
    for x in range(one_side):
        for y in range(one_side):
            map_for_fullsearch = deepcopy(landsea_map)
            fu = FillUpper(map_for_fullsearch, one_side)
            fu.fillup([x, y])
            filluped_map = deepcopy(fu.landsea_map)

            if map_for_fullsearch[y][x] == 'x':
                errmsg = 'The "fillup" method is not working!'
                assert map_for_fullsearch != filluped_map, errmsg

            fu.stack.append([x, y])
            while fu.stack:
                fu.DFS()

            if fu.map_for_dfs == filluped_map and fu.n_fillupped > 0:
                print('YES')
                exit()

    print('NO')
