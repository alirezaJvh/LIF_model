from LIF.LIF import LIF

parameters = {
    'C': 1,
    'R': 6.25,
    'u_rest': 20,
    'I': 3,
    'threshold': 350,
    'start_time': 5,
    'end_time': 100,
    'dt': 0.1
}

# test = LIF(**parameters)
if __name__ == '__main__':
    model = LIF(parameters)
    V = model.simulate()


