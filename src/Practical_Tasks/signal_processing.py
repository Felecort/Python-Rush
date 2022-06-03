from cmath import exp, pi
import numpy as np
import matplotlib.pyplot as plt

# noise_rate, signal, 1
def gen_signal(noise_rate, delays, *args):
    signal = np.zeros(len(delays))
    signal += noise_rate * (np.random.rand(len(delays)) - 0.5)
    print(f"noise {signal = }")
    print(f"sin = {np.sin(delays * args[0])}")
    for freq in args:
        signal += np.sin(delays * freq)
    return signal


# def fft_(p):
#     n = len(p)
#     if n == 1:
#         return p
#     w = exp((2 * pi * 1j) / n)
#     p_e, p_0 = p[::2], p[1::2]
#     y_e, y_0 = fft_(p_e), fft_(p_0)
#     y = [0] * n
#     for i in range(n // 2):
#         y[i] = y_e[i] + (w ** 1j) * y_0[i]
#         y[i + n // 2] = y_e[i] - (w ** 1j) * y_0[i]
    
#     return y


# def ifft_(p):
#     n = len(p)
#     if n == 1:
#         return p
#     w = (1 / n) * exp((-2 * pi * 1j) / n)
#     p_e, p_0 = p[::2], p[1::2]
#     y_e, y_0 = ifft_(p_e), ifft_(p_0)
#     y = [0] * n
#     for i in range(n // 2):
#         y[i] = y_e[i] + (w ** 1j) * y_0[i]
#         y[i + n // 2] = y_e[i] - (w ** 1j) * y_0[i]
    
#     return y


if __name__ == "__main__":
    noise_rate = 0
    counts = 2 ** 12
    time_len = 20
    
    delays = np.linspace(0, time_len, counts)
    
    signal = gen_signal(noise_rate, delays, 20)
    
    plt.plot(delays, signal)
    plt.show()
    
    spector = np.fft.fft(signal)
    freq = np.fft.fftfreq(delays.shape[-1])
    plt.plot(freq, spector.real, freq, spector.imag)
    plt.show()
