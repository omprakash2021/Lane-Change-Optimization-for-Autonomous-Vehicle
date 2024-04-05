import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import quad
from Collision_avoidance_algorithm import curvature_length

#---- L
def avgDist(v_ni, accel, tau = 0.7):
    v_ne = v_ni + accel * tau
    L = 0.5 * (v_ni + v_ne) * tau
    return L

# ---- end angle
def endAng(xnf, ynf, theta_i, x_e):
    a0 = np.tan(theta_i)
    a1 = ((3*ynf - 2*xnf*np.tan(theta_i))/(xnf**2)) * x_e
    a2 = ((xnf*np.tan(theta_i) - 2*ynf)/(xnf**3))*(x_e**2)
    theta_e = np.arctan(a0 + a1 + a2)
    return theta_e

#--- get end position e
def pos_e(x):
    global g_x_nf, g_y_nf, g_theta_i, g_linear_dist
    return (quad(curvature_length, 0, x, args = (g_x_nf, g_y_nf, g_theta_i))[0] - g_linear_dist)

#--- return end position and end angle
def endPosAng(x_nf, y_nf, theta_i, v_ni, accel):
    global g_x_nf, g_y_nf, g_theta_i, g_linear_dist

    g_theta_i = theta_i
    g_x_nf = x_nf
    g_y_nf = y_nf
    g_linear_dist = avgDist(v_ni, accel)
    
    x_e = round(fsolve(pos_e, 0.01)[0], 2)
    theta_e = endAng(g_x_nf, g_y_nf, g_theta_i, x_e)
    # print(f"x_e: {x_e :.4f}, ang_e: {theta_e :.4f}")
    return [x_e, theta_e]