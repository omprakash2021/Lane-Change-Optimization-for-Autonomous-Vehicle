#tau = Reaction time of the lab vehicle
#v_ni = longitudinal velocity of Subject vehicle at initial point of the trajectory
#v_(n-1)_i = v_pvi = longitudinal velocity of Preceding vehicle at initial point of the trajectory
#b_n, b_(n-1) = b_n, b_pv = maximum deceleration of Subject vehicle and Preceding vehicle

#v_(n+1)_i = v_lvi = logitudinal velocity of Lab vehicle at initial point of the trajectory
#b_(n+1) = b_lv = maximum deceleration of Lag Vehicle
#newton's law of motion V^2 = u^2 + 2*a*S

import numpy as np
from scipy.integrate import quad

tau = 0.7
b_n = 3.5
b_pv = 3.5
b_lv = 3.5

#=============================================================================
#total lane change time calculating
def curvature_length(x, x_nf, y_nf, theta_i):
    x_n = x
    c = np.tan(theta_i)
    a_0 = (6*y_nf - 4*x_nf*np.tan(theta_i))/(x_nf**2)
    a_1 = (3*x_nf*np.tan(theta_i) - 6*y_nf)/(x_nf**3)
    dy_dx = c + a_0*x_n + a_1*(x_n**2)
    curvature = np.sqrt(1 + dy_dx**2)
    return curvature
    
def total_LaneChangeTime(x_nf, y_nf, theta_i, u_ni):
    global tau
    x_fo = x_nf
    theta_i = theta_i
    time_1 = quad(curvature_length, 0, x_fo, args=(x_nf, y_nf, theta_i))[0] / u_ni
    time_2 = tau

    t_a = time_1 + time_2
    return t_a

#=============================================================================
#b_n = b_lv = b_pv = 3.5
def S_p(v_pvi, v_ni):
    global tau, b_n, b_pv, b_lv
    return v_ni*tau + ((v_ni**2)/(2*b_n)) - ((v_pvi**2)/(2*b_pv))

def S_l(v_lvi, v_ni):
    global tau, b_n, b_pv, b_lv
    return v_lvi*tau + ((v_lvi**2)/(2*b_lv)) - ((v_ni**2)/(2*b_n))

def get_Collision_Avoidance_Range(x_ni, x_nf, y_nf, theta_i, x_pvi, v_pvi, x_lvi, v_lvi, u_ni):
    t_a = total_LaneChangeTime(x_nf, y_nf, theta_i, u_ni)
    # print(f"2) t_a: {t_a :.3f}\n")
    v_ni = u_ni * np.cos(theta_i) 
    s_f = S_p(v_pvi, v_ni)
    s_r = S_l(v_lvi, v_ni)

    x_lvf = x_lvi + v_lvi * t_a 
    x_pvf = x_pvi + v_pvi * t_a

    length_pv = 4.5
    lowerLimit = x_lvf + s_r - x_ni
    upperLimit = x_pvf - s_f - length_pv - x_ni

    print(f"1) [lb]: s_r: {s_r:.3f}, x_lvf: {x_lvf:.3f}, limit: {lowerLimit :.3f}\n[ub]: s_f: {s_f:.3f}, x_pvf: {x_pvf:.3f}, limit: {upperLimit:.3f}\n")

    return [lowerLimit, upperLimit]

    