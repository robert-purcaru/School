import numpy as np
from matplotlib import pyplot as plt 
from scipy import signal
import math

pos_file = 'x_pos_pixels.csv'
time_file = 'times.csv'

meter_per_px = 0.8128 / 1920
origin_px = 1920/2

length = 1.53

def get_relative_x_m(x_px):
    return (x_px-origin_px)*meter_per_px

def get_duplicate_indeces(arr):
    dups = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            dups.append(i)
    return dups

def main():
    x_px = np.genfromtxt(pos_file, delimiter=',')
    x = get_relative_x_m(x_px)
    theta = np.asarray([math.asin(x_curr/length) for x_curr in x])
    print('theta ', len(theta))
    t = np.genfromtxt(time_file, delimiter=',')

    duplicate_indeces = get_duplicate_indeces(theta)
    theta = np.delete(theta, duplicate_indeces)
    t = np.delete(t, duplicate_indeces)
 
    amp_pos_ind = signal.argrelextrema(theta, np.greater, order = 5)
    amp_neg_ind = signal.argrelextrema(theta, np.less, order = 5)

    print('amp', amp_pos_ind)

    amp_pos = theta[amp_pos_ind]
    t_amp_pos = t[amp_pos_ind]
    amp_neg = theta[amp_neg_ind]
    t_amp_neg = t[amp_neg_ind]

    # init_amp = amp_pos[0]
    # T = sum(np.diff(t_amp_pos, 1)[:20])/20
    # print("period: ", T)

    # Q = 0
    # for amp in amp_pos:
    #     if amp < math.exp(-math.pi)*init_amp:
    #         break
    #     Q += 1

    # print("Q: ", Q)

    # initial_amp = amp_pos[0]
    # print("iA: ", initial_amp)
    # initial_theta = theta[0]
    # print("iT: ", initial_theta)
    # phase_constant = math.acos(initial_theta/initial_amp)
    # print("phi: ", phase_constant)

    """
    for i in range(len(t)):
        print("time: ", t[i])
        print("t: ", theta[i])
        a1 = initial_amp*math.cos((2*math.pi*t[i]/T) + phase_constant)
        print("a1: ", a1)
        a2 = theta[i]/a1
        print("a2: ", a2)
        print(math.log(a2))
        tau = -t[i]/np.log(a2)
        print("tau: ", tau)
        #Q2 = math.pi*(tau/T)
        #print("Q2:", Q2)
    """
    
    plt.plot(t, theta)
    plt.plot(t_amp_pos, amp_pos)
    plt.plot(t_amp_neg, amp_neg)
    plt.show()

if __name__ == "__main__":
    main()

