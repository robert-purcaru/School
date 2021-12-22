import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt
from scipy import signal
import math

pos_file = 'x_pos_pixels.csv'
time_file = 'times.csv'
corrected_pos_file = 'x_pos_pixels_corrected.csv'
corrected_time_file = 'times_corrected.csv'
# corrected_pos_file = 'first_1000_x_pos_pixels.csv'
# corrected_time_file = 'first_1000_times.csv'
xerror = 1/29.97

in_per_px = 31.875/1920
cm_per_in = 2.54

yerror = 0.02

def my_func(t,a,tau,T,phi):
    return a*np.exp(-t/tau)*np.cos(2*np.pi*t/T+phi)
# this is the function we want to fit. the first variable must be the
# x-data (time), the rest are the unknown constants we want to determine

def fitfunction(t):  
    return a*np.exp(-t/tau)*np.cos(2*np.pi*t/T+phi)
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

def initialize():
    global xdata, ydata, a, tau, T, phi, u_a, u_tau, u_T, u_phi, times, positions, corrected_times, corrected_positions, theta 
    
    times = np.genfromtxt(time_file, delimiter=',')
    positions = np.genfromtxt(pos_file, delimiter=',')
    corrected_times = np.genfromtxt(corrected_time_file, delimiter=',')
    corrected_positions = np.genfromtxt(corrected_pos_file, delimiter=',')


    theta =[]
    theta = np.asarray([math.asin((x * in_per_px * cm_per_in)/ 184.5) for x in corrected_positions])
    
    xdata=corrected_positions
    ydata=corrected_times
    xerror= 1
    yerror= 1

    popt, pcov = optimize.curve_fit(my_func, xdata, ydata)

    a=popt[0]
    tau=popt[1]
    T=popt[2]
    phi=popt[3]
    # best fit values are named nicely
    u_a=pcov[0,0]**(0.5)
    u_tau=pcov[1,1]**(0.5)
    u_T=pcov[2,2]**(0.5)
    u_phi=pcov[3,3]**(0.5) 
    # uncertainties of fit are named nicely

def graph_raw():
    global times, positions

    plt.plot(times - times[0], positions)
    plt.xlabel("Time Since First Identified Mass in Frame (s)")
    plt.ylabel("Position of Center of Identified Contour (px)")
    plt.title("Horizontal Position of Mass Found by OpenCV vs Time")
    plt.show()

def graph_corrected():
    global corrected_times, corrected_positions

    plt.plot(corrected_times - corrected_times[0], theta)
    plt.xlabel("Time Since First Identified Mass in Frame (s)")
    plt.ylabel("Amplitude (rad)")
    # plt.errorbar(corrected_times - corrected_times[0], theta, xerr=xerror, yerr=yerror, color = 'blue', ecolor = 'orange', capsize = 3)
    plt.title("Corrected Horizontal Position of Mass Found by OpenCV vs Time")
    plt.show()

def graph_short():
    
    short_times = np.genfromtxt('first_200_times.csv', delimiter=',')
    short_positions = np.genfromtxt('first_200_x_pos_pixels.csv', delimiter=',')

    plt.plot(short_times - times[0], short_positions)

    plt.errorbar(short_times - times[0],short_positions,yerr=yerror,xerr=xerror,fmt=".")
    plt.show()

def graph_short():
    global time_arr, amp_arr
    
    amp_pos_ind = signal.argrelextrema(theta, np.greater, order = 8)

    amp_arr = theta[amp_pos_ind]
    time_arr = corrected_times[amp_pos_ind]

    # print(time_arr)
    interval = []

    for i in range(1, len(time_arr)):
        interval.append(time_arr[i] - time_arr[i-1])
    i = 0
    while(i < len(interval)):
        if(abs(interval[i] - 2.7) > 0.5):
            interval.pop(i)
            i-= 1
        i += 1

    # np.savetxt("testintervals.csv", interval, delimiter=",")


    plt.plot(time_arr, amp_arr)
    plt.plot(corrected_times, theta, alpha = 0.3)

    plt.show()


def decay(t,a,tau):
    return a*np.exp(-t/tau)

def series_quad(theta, A, B, C):
    return A + B * theta + C * theta ** 2

def series_cube(theta, A, B, C, D):
    return A + (B * theta) + C * (theta ** 2) + D * (theta ** 3)

def series_quart(theta, A, B, C, D, E):
    return A + (B * theta) + C * (theta ** 2) + D * (theta ** 3) + E * (theta ** 4)

def series_quint(theta, A, B, C, D, E, F):
    return A + (B * theta) + C * (theta ** 2) + D * (theta ** 3) + E * (theta ** 4) + F * (theta ** 5)

if __name__ == '__main__':
    initialize()
    # graph_raw()
    # graph_corrected()
    graph_short()
    # # graph_tau()
    # params, cov = optimize.curve_fit(decay, time_arr, amp_arr)
    # print(params)
    # print(cov)
    # print(cov[1,1]**0.5)
    # plt.plot()
    # start=min(time_arr)
    # stop=max(time_arr)    
    # xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
    # zeros=[]
    # for x in xs:
    #     zeros.append(0)
    # curve=decay(xs, params[0], params[1])


    # # np.savetxt("thetas.csv", amp_arr, delimiter=",")
    # # np.savetxt("notThetas.csv", time_arr, delimiter=",")


    # plt.errorbar(time_arr, amp_arr, xerr=xerror, yerr=yerror, color = 'green', ecolor = 'orange', capsize=3, errorevery=5)
    # plt.plot(xs, curve, color = 'red')
    # plt.plot(time_arr, amp_arr, color = 'green')
    # plt.xlabel("Time Since First Identified Mass in Frame (s)")
    # plt.ylabel("Amplitude (rad)")
    # plt.title("Local Maximums Across Recording Period With Regression")
    # plt.show()

    # residuals = amp_arr - decay(time_arr, params[0], params[1])
    # plt.xlabel("Time Since First Identified Mass in Frame (s)")
    # plt.ylabel("Residuals Between Data and Curve (rad)")
    # plt.title("Residuals Between Data and Curve Throughout Analysis Period")
    # plt.plot(xs, zeros, color = 'black')
    # plt.errorbar(time_arr, residuals, xerr=xerror, yerr=yerror, color = 'blue', ecolor='orange', capsize=3, errorevery=5)
    # plt.plot(time_arr, residuals)
    # plt.show()

    # plt.plot()

    intervals = np.genfromtxt('intervals.csv', delimiter=',')
    thetas = np.genfromtxt('thetasForIntervals.csv', delimiter =',')

    thetas = np.sort(thetas)

    zeroes = []
    for i in range(len(thetas)):
        zeroes.append(0)

    # guess = [2.7, 0, 0]
    params, cov = optimize.curve_fit(series_quad, thetas, intervals)
    u_A=cov[0,0]**(0.5)
    u_B=cov[1,1]**(0.5)
    u_C=cov[2,2]**(0.5)
    print(params)
    print(u_A, u_B, u_C)

    paramsD, covD = optimize.curve_fit(series_cube, thetas, intervals)
    u_AD=covD[0,0]**(0.5)
    u_BD=covD[1,1]**(0.5)
    u_CD=covD[2,2]**(0.5)
    u_DD=covD[3,3]**(0.5)
    print(paramsD)
    print(u_AD, u_BD, u_CD, u_DD)

    paramsQ, covQ = optimize.curve_fit(series_quart, thetas, intervals)
    u_AQ=covQ[0,0]**(0.5)
    u_BQ=covQ[1,1]**(0.5)
    u_CQ=covQ[2,2]**(0.5)
    u_DQ=covQ[3,3]**(0.5)
    u_EQ=covQ[4,4]**(0.5)
    print(paramsQ)
    print(u_AQ, u_BQ, u_CQ, u_DQ, u_EQ)

    paramsR, covR = optimize.curve_fit(series_quint, thetas, intervals)
    u_AR=covR[0,0]**(0.5)
    u_BR=covR[1,1]**(0.5)
    u_CR=covR[2,2]**(0.5)
    u_DR=covR[3,3]**(0.5)
    u_ER=covR[4,4]**(0.5)
    u_FR=covR[5,5]**(0.5)
    print(paramsR)
    print(u_AR, u_BR, u_CR, u_DR, u_ER, u_FR)

    start=min(thetas)
    stop=max(thetas)   
    xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
    zeros=[]
    for x in xs:
        zeros.append(0)
    curve = series_quad(xs, params[0], params[1], params[2])
    curveD = series_cube(xs, paramsD[0], paramsD[1], paramsD[2], paramsD[3])

    plt.figure(figsize=(12,5))
    plt.subplot(1,1,1)
    plt.ylabel("Period (s)")
    plt.xlabel("Amplitude (rad)")
    plt.title("Period of Pendulum vs Measured Amplitude Modeled Against Quadratic Power Series") 
    plt.plot(xs, curve, color="green")
    plt.scatter(thetas, intervals, marker='.', color = "blue", alpha = 0.5)
    plt.errorbar(thetas, intervals, xerr = 0.002, yerr=0.2, color = 'blue', ecolor='orange', ls = 'none', capsize=3, errorevery = 1, alpha = 0.8)
    plt.ylim((2.2, 3.2))
    plt.show()

    plt.figure(figsize=(12,5))
    plt.subplot(1,1,1)
    plt.xlabel("Amplitude (rad)")
    plt.ylabel("Residuals Between Data and Model (s)")
    plt.title("Residuals Between Data and Quadratic Power Series Throughout Analysis Period")
    residuals = intervals - series_quad(thetas, params[0], params[1], params[2])
    plt.scatter(thetas, residuals, s=10)
    plt.plot(thetas, zeroes, color = 'gray')
    plt.errorbar(thetas, residuals, xerr = 0.002, yerr=0.2, color = 'blue', ecolor='orange', capsize=3, errorevery = 1, ls = 'none', alpha = 0.8)
    plt.show()


    plt.figure(figsize=(12,5))
    plt.subplot(1,1,1)
    plt.ylabel("Period (s)")
    plt.xlabel("Amplitude (rad)")
    plt.title("Period of Pendulum vs Measured Amplitude Modeled Against Cubic Power Series") 
    plt.plot(xs, curveD, color="red")
    plt.scatter(thetas, intervals, marker='.', color = "blue", alpha = 0.5, s=10)
    plt.errorbar(thetas, intervals, xerr = 0.002, yerr=0.2, color = 'blue', ecolor='orange', capsize=3, errorevery = 1, ls = 'none', alpha = 0.8)
    plt.ylim((2.2, 3.2))
    plt.show()

    plt.figure(figsize=(12,5))
    plt.subplot(1,1,1)
    plt.xlabel("Amplitude (rad)")
    plt.ylabel("Residuals Between Data and Model (s)")
    plt.title("Residuals Between Data and Cubic Power Series Throughout Analysis Period")
    residuals = intervals - series_cube(thetas, paramsD[0], paramsD[1], paramsD[2], paramsD[3])
    plt.scatter(thetas, residuals, s=10)
    plt.plot(thetas, zeroes, color = 'gray')
    plt.errorbar(thetas, residuals, xerr = 0.002, yerr=0.2, color = 'blue', ecolor='orange', ls = 'none', capsize=3, errorevery = 1, alpha = 0.8)
    plt.show()
