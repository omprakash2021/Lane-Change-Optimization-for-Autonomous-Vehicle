import numpy as np
import matplotlib.pyplot as plt 
import math
from matplotlib.animation import FuncAnimation

from Optimal_trajectory_algorithm import y_n
from Rollover_algorithm import rollover_position
from Collision_avoidance_algorithm import get_Collision_Avoidance_Range
from Optimal_trajectory_algorithm import cost_j
from Optimal_trajectory_algorithm import getOptimalXnf1
from Optimal_trajectory_algorithm import getOptimalXnf2
from Optimal_trajectory_algorithm import getOptimalXnf3
from Trajectory_Decision_Procedure import trajectoryDecision
from Lane_Chaging_Trajectory_Generation import endPosAng
from Collision_avoidance_algorithm import total_LaneChangeTime
#==============================================================================
#------------------------------------------------------------------------------

fig, ax = plt.subplots()
# fig.subplots_adjust(left=0.1, right=0.95)
xLowerLim = 0
xUpperLim = 800
ax.set_xlim([xLowerLim, xUpperLim])
ax.set_ylim([-4, 18.5])
plt.yticks(np.arange(-3.5, 17.5, 3.5))
ax.set_xlabel('Longitudinal Position')
ax.set_ylabel('Lateral Position')
ax.set_title('Dynamic Lane Change')

#Road Track
ax.axhline(y = 14, color = 'k', lw = 2) #top
ax.axhline(y = 0, color = 'k', lw = 2) #bottom

upperMarkerX = np.arange(0, 10000, 20)
upperMarkery = np.array([10.5]*(int ((10000/20))))
ax.plot(upperMarkerX, upperMarkery, 'k_')

middleMarkerX = np.arange(0, 10000, 20)
middleMarkery = np.array([7]*(int ((10000/20))))
ax.plot(middleMarkerX, middleMarkery, 'ks')

lowerMarkerX = np.arange(0, 10000, 20)
lowerMarkery = np.array([3.5]*(int ((10000/20))))
ax.plot(lowerMarkerX, lowerMarkery, 'k_')

class Vehicle:
    def __init__(self, x, y, vel, accel, ax, style, name = None):
        self.x = x
        self.y = y
        self.vel = vel
        self.accel = accel
        self.name = name
        self.angle = 0
        #_______________
        self.END = False #for checking if we need to change e_x, e_y, e_angle
        self.e_x = 0
        self.e_angle = 0
        self.e_y = 0
        #________________
        self.pos, = ax.plot(self.x, self.y, style, ms = 10, mec = None)
        self.ax = ax
        if name == "SV":
            self.pos_line = self.ax.axvline(self.x, c = "b", lw = 0.5)
        else:
            self.pos_line = self.ax.axvline(self.x, c = "g", lw = 0.5)
    
    def move(self, vel, accel, tau = 0.7, y_pos = y_n):
        vel_i = self.vel
        x_i = self.x
        vel_f = vel_i + accel * tau
        x_f = (0.5 * (vel_i + vel_f) * tau) + x_i
        
        # y_f = y_pos(100, 10.5, x_f, 0)
        self.x, self.vel = x_f, vel_f
        # if self.name == "SV":
        #     print(f"xi: {x_i :.4f}, x_f: {x_f :.4f}, vi: {vel_i :.4f}, vf: {vel_f :.4f} \n")
        self.pos_line.set_xdata([self.x])
        
        
SV = Vehicle(3, 3.5, 15, 0.5, ax, 'b>', 'SV')
LV = Vehicle(50, 10.5, 15, 0, ax, 'g>', 'LV')
PV = Vehicle(300, 10.5, 15, 0, ax, 'g>', 'PV')

# objects = [SV]
objects = [SV, LV, PV]
meters = ax.text(4, 15.5, 
    "SV\nv = {vel: .2f}\na = {accel: .2f}\nx = {x: .2f}\ny = {y: .2f}".format(vel = SV.vel, accel = SV.accel, x = SV.x, y = SV.y), 
    fontsize = 10, bbox = dict(facecolor = '#0dbaca', alpha = 0.5))
# just for the test, delete if not in used
test = [[0],[0]]
def pathGuider(x_nf, x_ni, u_ni, sub_v, PV_x, PV_v, LV_x, LV_v):
    global a_nmax, tau, weight, theta_i, y_nf
    global test

    velRange = (u_ni - (a_nmax * tau), u_ni + (a_nmax * tau))
    weightRange = (0, 1)
    x_foRange = (0.0000001, np.inf)
    # _____________________________________________________________________________________________________________________ 
    x_fo = getOptimalXnf1(x_nf, u_ni, weight, theta_i, y_nf) # getOptimalXnf(x_nf, u_ni, weight, theta_i, y_nf)
    # print(f"1) t_a: {total_LaneChangeTime(x_fo, y_nf, theta_i, u_ni) :.3f}")
    # get_Collision_Avoidance_Range(x_ni, x_nf, y_nf, theta_i, x_pvi, v_pvi, x_lvi, v_lvi, u_ni)
    col_lb, col_ub = get_Collision_Avoidance_Range(x_ni, x_fo, y_nf, theta_i, PV_x, PV_v, LV_x, LV_v, u_ni)
    x_nr = rollover_position(u_ni, y_nf) # rollover_position(u_ni, y_nf)
    # _____________________________________________________________________________________________________________________ 
    optimalCond = trajectoryDecision(x_fo, x_nr, col_lb, col_ub)
    # if test[1][0] == 1:
    #     print(f"[1) {test[0][0]}: {test[0][1]}, x_fo: {test[0][2] :.3f}, vf: {test[0][3] :.3f}, w_f: {test[0][4] :.3f}\n 2) lb: {optimalcond[1] :.3f}, ub: {optimalcond[2] :.3f}, x_fo: {x_fo :.3f}, vf: {u_ni :.3f}, w_f: {weight :.3f}]")
    #     test = [[0], [0]]
    # print(f"2) x_fo: {x_fo:.2f}, x_nr: {x_nr:.2f}, lb: {col_lb:.2f}, ub: {col_ub:.2f}\n")
    if optimalCond[0] == "optimal":
        sub_v.END = True
        sub_v.e_x, sub_v.e_angle = endPosAng(x_fo, y_nf, theta_i, u_ni, sub_v.accel)
        sub_v.e_y = y_n(x_fo, y_nf, sub_v.e_x, sub_v.e_angle)

    elif optimalCond[0] == "more than upperBound":
        # print(f"called ub || y_nf: {y_nf :.3f}")
        result = getOptimalXnf2(velRange, weightRange, x_foRange, optimalCond, x_nf, u_ni, weight, theta_i, y_nf)
        if result[0] == "optimal":
            # print("called opt ub")
            x_fo, v_fo, w_fo = result[1]
            sub_v.accel = (v_fo - u_ni)/tau
            test = [["lb", optimalCond[2], x_fo, v_fo, w_fo],[1]]
            weight = w_fo

    elif optimalCond[0] == "less than lowerBound":
        # print(f"called lb || y_nf: {y_nf :.3f}")
        result = getOptimalXnf3(velRange, weightRange, x_foRange, optimalCond, x_nf, u_ni, weight, theta_i, y_nf)
        if result[0] == "optimal":
            # print("called opt lb")
            x_fo, v_fo, w_fo = result[1]
            sub_v.accel = (v_fo - u_ni)/tau
            test = [["lb", optimalCond[1], x_fo, v_fo, w_fo],[1]]
            weight = w_fo
    
#intention at m point(an integer)
def intentionGen(vel, accel, x1, m, tau = 0.7): 
    vi = vel
    dist = 0
    for pos in range(0, m):
        vf = vi + accel * tau
        x2 = ((vi + vf) * 0.5 * tau) + x1
        vi = vf
        x1 = x2

    return round(x1, 2)

#initial inputs
x_nf = 150
y_nf = 7
theta_i = 0
weight = 0.75
intention = intentionGen(SV.vel, SV.accel, 3, 4)
a_nmax = 3
tau = 0.7

def update(frame, *objects):
    global x_nf, y_nf, theta_i, weight, intention, a_nmax, tau
    
    # sub_v, = objects
    sub_v, lag_v, preced_v = objects
    meters.set_text('')
    meters.set_text("SV\nv = {vel: .2f}\na = {accel: .2f}\nx = {x: .2f}\ny = {y: .2f}".format(vel = sub_v.vel, accel = sub_v.accel, x = sub_v.x, y = sub_v.y))

    for obj in objects:
        if obj.name == 'SV':
            if obj.END == True:  
                print("END->True")
                obj.pos.set_data([obj.x + obj.e_x], [obj.y + obj.e_y])
                obj.angle = obj.e_angle
                obj.x, obj.y = [obj.x + obj.e_x, obj.y + obj.e_y]
                obj.pos_line.set_xdata([obj.x])
                y_nf = y_nf - obj.e_y
                # print(f"[e_x: {obj.e_x :.3f}, e_y: {obj.e_y :.3f}, ang_e: {obj.e_angle :.3f} \n x: {obj.x :.3f}, y: {obj.y :.3f}, ang: {obj.angle :.3f}\n")
                if obj.y >= 10.5:
                    pass
                    # obj.y = 10.5
                    # obj.pos.set_ydata([10.5])
                obj.e_x = 0
                obj.e_angle = 0
                obj.e_y = 0 
                weight = 0.75
                theta_i = obj.angle
                obj.END = False
            else:
                obj.move(obj.vel, obj.accel)
                obj.pos.set_xdata([obj.x])
                # obj.pos.set_data([obj.x], [obj.y])
            continue
        obj.move(obj.vel, obj.accel)
        obj.pos.set_xdata([obj.x])
        # obj.pos.set_data([obj.x], [obj.y])
    if sub_v.x >= (800/2):
        ax.set_xlim([0 + sub_v.x - (800/2), 800 + sub_v.x - (800/2)])

    if(round(sub_v.x, 2) >= intention) and (sub_v.y < 10.5):
        sub_v.pos.set_markeredgecolor('red')
        pathGuider(x_nf, sub_v.x, sub_v.vel, sub_v, preced_v.x, preced_v.vel, lag_v.x, lag_v.vel)

    return [obj.pos for obj in objects], meters,

simulate = FuncAnimation(fig, update, fargs = objects, frames = 500, interval = 100)
plt.show()