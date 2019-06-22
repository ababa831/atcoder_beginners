import numpy as np
MAX_X = 10 ** 8

n, k =  map(int, input().split())
x_positions = list(map(int, input().split()))


class Updator(object):
    
    def __init__(self, x_positions, n, k):
        self.n = n
        self.k = k
        self.x_t = 0
        self.t = 0
        self.x_positions = __get_route_list(x_positions, k)
        self.x_states = self.__get_init_state(self.x_positions)
    
    def __get_init_state(self, x_positions):
        """Return initial every candle states as list"""
        return [False] * len(x_positions)
        
    def __plus_1(self):
        self.x_t += 1
        self.t += 1
    
    def __minus_1(self):
        self.x_t -= 1
        self.t += 1

    def __is_candle_exist(self):
        if self.x_t in self.x_positions:
            return True
        else: 
            False
    
    def __fire(self, x_t):
        """
        Fire the candle and update x_states
        """
        x_t_idx = self.x_states.index(x_t)
        if self.x_states[x_t_idx] == False:
            self.x_states[x_t_idx] = True
    
    def __get_route_list(self, x_positions, k):
        """
        Get optimized route (list) which takes minimum time.
        """
        route_list = []
        for i in range(k):
            abs_positions = list(map(abs, x_positions))
            argmin_x = np.argmin(abs_positions)
            route_list.append(x_positions[argmin_x])
            x_positions[argmin_x] = MAX_X
        
        return route_list

    def update(self):
# Give up!