from collections import deque


class IslandableChecker(object):
    def __init__(self, geo_map, start_point=(0, 0)):
        # 10 x 10
        self.geo_map = [list(input()) for _ in range(10)]
        self.stack = deque()
        self.start_point = start_point

    def check(self, redefined_start_point=None):
        """
        Check if the map can unite as a new island
        when a sea point is converted to a land one.
        """
        if redefined_start_point is not None:
            self.start_point = redefined_start_point

        # TODO:
        # 1. Search "oxo"(two lands and a sea sandwitches)
        land_pairs = None
        for row_idx, row_val in enumerate(self.geo_map):
            for col_idx, col_val in enumerate(row_val):
                if col_val == 'x':
                    land_pairs = \
                        self.get_land_pairs(col_idx, row_idx)

        # 2. Check if there are pairs which can reach each other via DFS
        # 3. "The reachable pair" detected -> "YES", or -> "NO"
        for land_pair in land_pairs:
            # WIP
            pass

    def get_land_pairs(self, sea_point):
        """
        Check if there are pairs which describe
        "oxo"(two lands and a sea sandwitches)

        Returns
        -------
        land_pairs: list
            - Yes: pairs (e.g. [[(1, 2), (2, 3)]])
            - No: empty list
        """
        land_pairs = []

        x, y = sea_point[0], sea_point[1]
        # TODO:
        # Check if the canditates exist
        canditates1, canditates2 = None, None
        if self.is_existing(x, y + 1) and self.is_existing(x, y - 1):
            canditates1 = [self.geo_map[y + 1][x], self.geo_map[y - 1][x]]
        if self.is_existing(x + 1, y) and self.is_existing(x - 1, y):
            canditates2 = [self.geo_map[y][x + 1], self.geo_map[y][x - 1]]

        if self.is_land_pair(canditates1):
            land_pairs.append([(y + 1, x), (y - 1, x)])
        if self.is_land_pair(canditates2):
            land_pairs.append([(y, x + 1), (y, x - 1)])
        return land_pairs

    def is_existing(self, point):
        if 0 <= point[0] < 10 and 0 <= point[1] < 10:
            return True
        else:
            return False

    def is_land_pair(self, canditates):
        if canditates[0] == 'o' and canditates[1] == 'o':
            return True
        else:
            return False

    def can_reach_each_other(self, pairs_list):
        """Check if there are pairs which can reach each other via DFS"""
        pass

    def dfs(self, dfs_start_point):
        pass