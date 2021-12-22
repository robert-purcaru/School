import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt
from scipy import signal
import math
import copy

xerror = 0
yerror = 0.02

in_per_px = 31.875/1920
cm_per_in = 2.54
frames_per_sec = 29.92

average_times = []
stdevs_M = [0.632, 0.471, 0.516, 0.316, 0.527, 0.483]
stdevs = []
string_lengths = [0.694, 0.947, 1.179, 1.479, 1.691, 1.940]
# masses = [118.2, 178.2, 239.4, 274.9, 363.9, 430.7, 508.97]
masses = [118.2, 178.2, 239.4, 274.9, 363.9, 508.97]



def initialize_file(filename):
    global times, frames, trial, stdevs
    
    frames = np.genfromtxt(filename, delimiter=',')
    times = copy.deepcopy(frames)
    trial = []
    for i in range(len(times)):
        times[i] = frames[i] / frames_per_sec
        trial.append(i)

    average_times.append(np.average(times))
    stdevs.append(np.std(times))
    # print(average_times)

def initialize_array(arr):
    global trial, times
    # trial = []
    for i in range(len(arr)):
        arr[i] = 2 * arr[i]
    times = arr

    

################################################################################

def graph_with_curve(x_values, y_values, x_error, y_error, title, y_label, x_label, model):

    plt.figure(figsize=(10,5))
    plt.subplot(1,1,1)
    params, cov = optimize.curve_fit(model, x_values, y_values)
    curve = model(x_values, params[0], params[1], params[2])

    print(params)
    err0 = (cov[0,0] ** 0.5)
    err1 = (cov[1,1] ** 0.5)
    err2 = (cov[2,2] ** 0.5)

    print(err0, err1, err2)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x_values, curve, color = 'green')
    plt.scatter(x_values, y_values, facecolors = 'r', s=15)
    plt.errorbar(x_values, y_values, xerr = x_error, yerr=y_error, color = 'blue', ecolor='blue', ls = 'none', capsize=3, errorevery = 1, alpha = 0.7)
    plt.show()

def graph_with_line(x_values, y_values, x_error, y_error, title, y_label, x_label, model):

    plt.figure(figsize=(10,5))
    plt.subplot(1,1,1)
    params, cov = optimize.curve_fit(model, x_values, y_values)
    curve = model(x_values, params[0])

    print(params)
    err0 = (cov[0,0] ** 0.5)

    print(err0)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x_values, curve, color = 'green')
    plt.scatter(x_values, y_values, facecolors = 'r', s=15)
    plt.errorbar(x_values, y_values, xerr = x_error, yerr=y_error, color = 'blue', ecolor='blue', ls = 'none', capsize=3, errorevery = 1, alpha = 0.7)
    plt.show()

def graph_log(x_values, y_values, x_error, y_error, title, y_label, x_label, model):

    params, cov = optimize.curve_fit(model, x_values, y_values)
    curve = model(x_values, params[0], params[1], params[2])

    print(params)
    err0 = (cov[0,0] ** 0.5)
    err1 = (cov[1,1] ** 0.5)
    err2 = (cov[2,2] ** 0.5)

    print(err0, err1, err2)

    plt.figure(figsize=(10,5))
    plt.subplot(1,1,1)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x_values, curve, color = 'green')
    plt.scatter(x_values, y_values, facecolors = 'r', s=15)
    plt.errorbar(x_values, y_values, xerr = x_error, yerr=y_error, color = 'blue', ecolor='blue', ls = 'none', capsize=3, errorevery = 1, alpha = 0.7)
    plt.show()

def graph(x_values, y_values, x_error, y_error, title, y_label, x_label, average = False):

    plt.figure(figsize=(10,5))
    plt.subplot(1,1,1)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.scatter(x_values, y_values)
    plt.errorbar(x_values, y_values, xerr = x_error, yerr=y_error, color = 'blue', ecolor='orange', ls='none', capsize=3, errorevery = 1, alpha = 0.7)

    if average:
        average_value = np.average(y_values)
        print(average_value)
        average_arr = []
        for i in range(len(x_values)):
            average_arr.append(average_value)
        plt.plot(x_values, average_arr, color = 'purple')
        

    plt.show()


################################################################################

def string_equation(L, k, L_0, n):
    return (k * ((L_0 + L) ** n))

def line(A, B):
    return A * 0 + B

################################################################################

if __name__ == '__main__':
    initialize_file('LengthTest_69.6cm_time.csv')
    # graph(trial, times, xerror, 1 / frames_per_sec, 'Times measured for Half Period with 69.4cm String and 508.9g Mass', 'Duration of one half cycle (s)', 'Trial Number', average = True)

    initialize_file('LengthTest_94.4cm_time.csv')
    # graph(trial, times, xerror, 1 / frames_per_sec, 'Times measured for Half Period with 94.7cm String and 508.9g Mass', 'Duration of one half cycle (s)', 'Trial Number', average = True)

    initialize_file('LengthTest_117.1cm_time.csv')
    # graph(trial, times, xerror, 1 / frames_per_sec, 'Times measured for Half Period with 117.9cm String and 508.9g Mass', 'Duration of one half cycle (s)', 'Trial Number', average = True)

    initialize_file('LengthTest_147.4cm_time.csv')
    # graph(trial, times, xerror, 1 / frames_per_sec, 'Times measured for Half Period with147.9cm String and 508.9g Mass', 'Duration of one half cycle (s)', 'Trial Number', average = True)

    initialize_file('LengthTest_169.5cm_time.csv')
    # graph(trial, times, xerror, 1 / frames_per_sec, 'Times measured for Half Period with 169.1cm String and 508.9g Mass', 'Duration of one half cycle (s)', 'Trial Number', average = True)

    initialize_file('LengthTest_194.2cm_time.csv')
    # graph(trial, times, xerror, 1 / frames_per_sec, 'Times measured for Half Period with 194.0cm String and 508.9g Mass', 'Duration of one half cycle (s)', 'Trial Number', average = True)

    initialize_array(average_times)
    graph_with_curve(string_lengths, times, xerror, 1/frames_per_sec, 'Period of Pendulum at Various String Lengths Modeled Against Power Law Function', 'Period (s)', 'String Length (m)', string_equation)
    graph_log(string_lengths, times, xerror, 1/frames_per_sec, 'Period of Pendulum at Various String Lengths Modeled Against Power Law Function', 'Period (s)', 'String Length (m)', string_equation)


    average_times = []
    initialize_file("MassTest_118.26g_time.csv")
    # graph(trial, times, xerror, 1/frames_per_sec, 'Times Measured for Half Period with 118.3g Mass and String Length 194.0cm', "Duration of One Half Period (s)", 'Trial Number', average = True)
    
    initialize_file("MassTest_178.20g_time.csv")
    # graph(trial, times, xerror, 1/frames_per_sec, 'Times Measured for Half Period with 178.2g Mass and String Length 194.0cm', "Duration of One Half Period (s)", 'Trial Number', average = True)
    
    initialize_file("MassTest_239.36g_time.csv")
    # graph(trial, times, xerror, 1/frames_per_sec, 'Times Measured for Half Period with 239.4g Mass and String Length 194.0cm', "Duration of One Half Period (s)", 'Trial Number', average = True)
    
    initialize_file("MassTest_274.90g_time.csv")
    # graph(trial, times, xerror, 1/frames_per_sec, 'Times Measured for Half Period with 274.9g Mass and String Length 194.0cm', "Duration of One Half Period (s)", 'Trial Number', average = True)

    initialize_file("MassTest_363.95g_time.csv")
    # graph(trial, times, xerror, 1/frames_per_sec, 'Times Measured for Half Period with 363.9g Mass and String Length 194.0cm', "Duration of One Half Period (s)", 'Trial Number', average = True)

    # initialize_file("MassTest_430.66g_time.csv")
    # graph(trial, times, xerror, 1/frames_per_sec, 'Times Measured for Half Period with 430.7g Mass and String Length 194.0cm', "Duration of One Half Period (s)", 'Trial Number', average = True)

    initialize_file("MassTest_508.97g_time.csv")
    # graph(trial, times, xerror, 1/frames_per_sec, 'Times Measured for Half Period with 508.9g Mass and String Length 194.0cm', "Duration of One Half Period (s)", 'Trial Number', average = True)

    initialize_array(average_times)
    graph(masses, times, xerror, 1/frames_per_sec, 'Period of Pendulum at Various Masses with 190.4cm String Length', 'Period (s)', 'Mass (g)')
    print(times)
    for i in range(len(times)):
        times[i] = times[i] - 2.92335
    print(times)
    graph(masses, times, xerror, 1/frames_per_sec, 'Residuals in Period of Pendulum at Various Masses with 190.4cm String Length about Linear Regression', 'Period (s)', 'Mass (g)', line)