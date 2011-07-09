# -*- coding: utf-8 -*-
#Call Option class
class CallOption:
    def __init__(self, K, T):
        self.K = K
        self.T = T
    def payoff(self, underlying_path):
        return max(underlying_path[-1] - self.K, 0)