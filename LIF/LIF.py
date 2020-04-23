import numpy as np
class LIF:
    def __init__(self, parameters):
        self.C = parameters['C']
        self.R = parameters['R']
        self.u_rest = parameters['u_rest']
        self.I = parameters['I']
        self.threshold = parameters['threshold']
        self.start_time = parameters['start_time']
        self.end_time = parameters['end_time']
        self.dt = parameters['dt']                    # step size (ms)


    def tau_m(self):
        return self.C * self.R

    def time_length(self):
        return self.end_time - self.start_time

    def interval(self):
        return self.tau_m() * (np.log((self.R * self.I) / (self.R * self.I - self.threshold)))

    def make_time_array_steps(self):
        return np.arange(0, self.end_time + self.dt, self.dt)

    def simulate(self):
        time = self.make_time_array_steps()
        u_history = np.empty(len(time))
        spike = 0
        u_history[0] = self.u_rest
        for i in range(1, len(time)):
            if time[i] < self.start_time:
                u_history[i] = self.u_rest
                print(1)
            else:
                # tau_m * (du/dt) = -(u - u_rest) + (R * I)
                du = self.tau_m() * ((-u_history[i-1] + self.u_rest) + (self.R * self.I))
                # print(du)
                # print('****')
                u_history[i] = u_history[i-1] + du * self.dt
                print(u_history[i])

            if u_history[i] > self.threshold:
                u_history[i] = self.u_rest
                u_history[i-1] = self.threshold
                spike = spike + 1

        print(spike)
        return {"u": u_history, "time": time}

    def time_I_info(self):
        pass




