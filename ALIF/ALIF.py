from LIF.LIF import LIF
import numpy as np

class ALIF(LIF):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.a = parameters['a']
        self.b = parameters['b']
        self.tau_w = parameters['tau_w']
        self.spike = 0


    # def simulate(self, func=None):
    #     time, u_history = self.__setup()
    #     w = np.zeros(len(time))
    #     for i in range(1, len(time)):
    #         if time[i] < self.start_time:
    #             u_history[i] = self.u_rest
    #             self.I_history[i] = 0
    #         else:
    #             if func is None:
    #                 du = (1 / self.__tau_m()) * (-(u_history[i - 1] - self.u_rest) + (self.R * self.I))
    #             else:
    #                 pass
    #     return 10
