import numpy as np
import matplotlib.pyplot as plt


class generator_1:
    def __init__(self):
        self.states = np.zeros(10, dtype=int)
        self.reset()

    def reset(self):
        self.states = np.ones(10, dtype=int)

    def cycle(self):
        x3 = self.states[2]
        x10 = self.states[9]

        self.states[1:] = self.states[:9]
        self.states[0] = int((x3 + x10) % 2)

        return x10


class generator_2:
    def __init__(self):
        self.states = np.zeros(10, dtype=int)
        self.reset()

    def reset(self):
        self.states = np.ones(10, dtype=int)

    def cycle(self):
        x2 = self.states[1]
        x3 = self.states[2]
        x6 = self.states[5]
        x8 = self.states[7]
        x9 = self.states[8]
        x10 = self.states[9]

        self.states[1:] = self.states[:9]
        self.states[0] = int((x2 + x3 + x6 + x8 + x9 + x10) % 2)

        return int((x3 + x8) % 2)


class CA_code:
    def __init__(self):
        self.output = []
        self.g1 = generator_1()
        self.g2 = generator_2()

    def generate(self, n_cycles):
        for i in range(n_cycles):
            if not (i % 1023):
                print(f"Cycle {i} - reset")
                self.g1.reset()
                self.g2.reset()
            out_g1 = self.g1.cycle()
            out_g2 = self.g2.cycle()
            self.output.append(int((out_g1 + out_g2) % 2))

        print(f"Register g_1 after {n_cycles} cycles : {self.g1.states}")
        print(f"Register g_2 after {n_cycles} cycles : {self.g2.states}")

        return np.array(self.output, dtype=int)


if __name__ == "__main__":

    ca = CA_code()
    output_4 = ca.generate(1023*2) * 2 - 1
    output_1 = ca.generate(1023) * 2 - 1

    x_corr = np.correlate(output_1, output_4, mode="full")

    fig, ax = plt.subplots()

    ax.plot(np.abs(x_corr))

    plt.show()
