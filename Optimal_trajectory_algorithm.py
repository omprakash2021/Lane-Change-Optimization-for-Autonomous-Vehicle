import numpy as np
import matplotlib.pyplot as plt
import math
from Collision_avoidance_algorithm import total_LaneChangeTime as Total_time
from scipy.optimize import minimize

'''
Trajectory, y_n = lateral position of SV
    x_nf = final longitudinal position of SV
    y_nf = final lateral position of SV(Center line of target lane)
    x_n = input longitudinal position of SV
    y_n = output lateral position of SV
    theta_i = course angle at the initial point of each time step

'''
def y_n(x_nf, y_nf, x_n, theta_i):
    theta_i = theta_i
    a_0 = 0
    a_1 = np.tan(theta_i)
    a_2 = (3*y_nf - 2*x_nf*np.tan(theta_i))/(x_nf**2)
    a_3 = (x_nf*np.tan(theta_i) - 2*y_nf)/(x_nf**3)
    y_coord = a_0 + a_1*x_n + a_2*(x_n**2) + a_3*(x_n**3)
    # print(f"y_n: {y_coord :.4f}, a1: {a_1 :.4f}, a2: {a_2 :.4f}, a3: {a_3 :.4f}")
    return y_coord

# def dy_dx_n(x_nf, y_nf, x_n, theta_i):
#     a_0 = np.tan(theta_i)
#     a_1 = ((6*y_nf) - (4*x_nf*np.tan(theta_i))/(x_nf**2))
#     a_2 = ((3*x_nf*np.tan(thata_i)) - (6*y_nf))/(x_nf**3)
    
#     return a_0 + a_1*x_n + a_2*(x_n**2)


'''
Side acceleration a_sf, at final position x_nf
u_ni = initial velocity of SV in the moving direction of SV
K = curvature of the function, here y_n

'''

def a_sf(u_ni, x_nf, theta_i, y_nf):
    theta_i = theta_i
    K = abs((2*x_nf*np.tan(theta_i) - 6*y_nf)/(x_nf**2))
    return (u_ni**2)*K


''' 
Testing the const function and it's nature
'''
#assumming t_amax = 6 sec
#a_smax = 3 m^2/sec
#weight = omega = 0.75
#tau = 0.7 sec

t_amax = 6
a_smax = 3
tau = 0.7

'''
Cost function for comfort and efficiency

    t_a = total time taken to finish the lange changing process
    t_amax = maximum lane changin time in all trajectories
    a_smax = maximum side acceleration in all trajectories

'''

def cost_j(x_nf, u_ni, weight, theta_i, y_nf = 7, t_amax = 6, a_smax = 3, tau = 0.7):

    t_a = Total_time(x_nf, y_nf, theta_i, u_ni)
    a = a_sf(u_ni, x_nf, theta_i, y_nf) 
    comfort = weight * ((a/a_smax)**2)
    efficiency = (1 - weight)*t_a/t_amax

    return comfort + efficiency

def cost_j2(bnd2, theta_i, y_nf = 7, t_amax = 6, a_smax = 3, tau = 0.7):
    x_nf, u_ni, weight = bnd2[0], bnd2[1], bnd2[2]
    t_a = Total_time(x_nf, y_nf, theta_i, u_ni)
    a = a_sf(u_ni, x_nf, theta_i, y_nf) 
    comfort = weight * ((a/a_smax)**2)
    efficiency = (1 - weight)*t_a/t_amax

    return comfort + efficiency

def cost_j3(bnd3, theta_i, y_nf = 7, t_amax = 6, a_smax = 3, tau = 0.7):
    x_nf, u_ni, weight = bnd3[0], bnd3[1], bnd3[2]
    t_a = Total_time(x_nf, y_nf, theta_i, u_ni)
    a = a_sf(u_ni, x_nf, theta_i, y_nf) 
    comfort = weight * ((a/a_smax)**2)
    efficiency = (1 - weight)*t_a/t_amax

    return comfort + efficiency

def getOptimalXnf1(x_nf, u_ni, weight, theta_i, y_nf):
    bnds = [(0.0000001, np.inf)]
    res = minimize(cost_j, x_nf, args = (u_ni, weight, theta_i, y_nf), bounds = bnds, method = "SLSQP")
    # print(f"1) get-opt, x_nf: {x_nf:.2f}, u: {u_ni:.2f}, w: {weight:.2f}, ang: {theta_i:.2f}, y_nf: {y_nf:.2f}, cost: {res.fun:.2f}, x_opt: {res.x[0]:.2f}")
    return res.x[0]

def getOptimalXnf2(velRange, weightRange, x_foRange, low_up_bnd, x_nf, u_ni, weight, theta_i, y_nf):

    bnds = [x_foRange, (velRange[0], u_ni), weightRange]
    lb = low_up_bnd[1]
    ub = low_up_bnd[2]
    res = minimize(cost_j2, x0 = [x_nf, u_ni, weight], args = (theta_i, y_nf), bounds = bnds, method = "SLSQP")
    if res.x[0] <= ub and res.x[0] >= lb:
        return ["optimal", res.x]
    else:
        return ["not optimal"]

def getOptimalXnf3(velRange, weightRange, x_foRange, low_up_bnd, x_nf, u_ni, weight, theta_i, y_nf):

    bnds = [x_foRange, (u_ni, velRange[1]), weightRange]
    lb = low_up_bnd[1]
    ub = low_up_bnd[2]
    res = minimize(cost_j3, x0 = [x_nf, u_ni, weight], args = (theta_i, y_nf), bounds = bnds, method = "SLSQP")
    if res.x[0] >= lb and res.x[0] <= ub:
        return ["optimal", res.x]
    else:
        return ["not optimal"]