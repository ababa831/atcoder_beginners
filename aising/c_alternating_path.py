class RouteController(object):
    def __init__(self, h, w, s_list):
        h_list = list(range(h))
        w_list = list(range(w))
        self.passable_point = \
            set([(val_h, val_w) for val_h in h_list for val_w in w_list])
        self.color_info = s_list
        self.answers = []

    def count_answer(self, start_black, end_white):
        # start_black -> next_white
        # if not passed point -> continue to pass
        #   if the white is not passed -> add an anser
        # white -> black
        # repeat
        passed_point = []
        next_points = self.get_next_passable(start_black)
        new_next_points = [next_p for next_p in next_points
                           if next_p not in passed_point]
        for new_next_point in new_next_points:
            while new_next_points is not None:
                # deep search
                pass

    def is_duplicated(self, curr_point):
        pass

    def is_passable(self, point):
        if point in self.passable_point:
            return True
        else:
            return False

    def del_passable(self, target_point):
        self.passable_point = \
            self.passable_point - set([target_point])

    def get_next_passable(self, curr_point):
        next_canditates = [(curr_point[0] + 1, curr_point[1] + 0),
                           (curr_point[0] - 1, curr_point[1] + 0),
                           (curr_point[0], curr_point[1] + 1),
                           (curr_point[0], curr_point[1] - 1)]
        next_passable = [p_i for p_i in next_canditates
                         if self.is_passable(p_i) is True]
        return next_passable

    def is_diff_color(self, curr_point, next_point):
        curr_color = self.get_color(curr_point)
        next_color = self.get_color(next_point)
        if curr_color is not next_color:
            return True
        else:
            return False

    def get_color(self, point):
        return self.color_info[point[0]][point[1]]
