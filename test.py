from LIF.LIF import LIF
parameters = {
    'C': 1,
    'R': 6.25,
    'u_rest': 20,
    'I': 3,
    'threshold': 350,
    'start_time': 5,
    'end_time': 100,
    'dt': 0.1,
    'a': 2,
    'b': 2,
    'tau_w': 5
}

# test = LIF(**parameters)
if __name__ == '__main__':
    # model = LIF(parameters)
    # func = lambda u, u_rest: -(u - u_rest)** 2
    # V = model.simulate(func)
    model1 = LIF(parameters, a=2, b=3, tau_w=5)
    v = model1.simulate_adaptive()
    print(v)

