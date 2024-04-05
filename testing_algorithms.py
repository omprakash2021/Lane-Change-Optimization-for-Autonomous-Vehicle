import numpy as np
import matplotlib.pyplot as plt 
from Optimal_trajectory_algorithm import y_n
from Optimal_trajectory_algorithm import cost_j

#==============================================================================
#------------------------------------------------------------------------------
# x = np.linspace(0, 200, 201)
# x = np.arange(0, 1350, 2.7)
# fig, axs = plt.subplots(2, 2, sharex = True)

# y_nf = 5
# theta_i = 0
# x_n = x
# x_nf = [20, 50, 100, 150]
# y = []

# for value in x_nf:
#     y.append(y_n(value, y_nf, x_n, theta_i))

# i = 0
# for ax in axs.flat:
#     ax.axhline(y = 5, ls = '-', lw = 2, color = 'r')
#     ax.axvline(x = x_nf[i], ls = '-', lw = 2, color = 'r')
#     ax.set_xlabel(f"X, x_nf = {x_nf[i]}")
#     ax.set_ylabel(f"Y")
#     ax.set_xlim([0, 200])
#     ax.set_ylim([-20, 20])
#     ax.plot(x, y[i])
#     i += 1

# plt.show()

#==============================================================================
#------------------------------------------------------------------------------

# y_nf = 7
# u_ni = 27.77 #initial velocity
# # x_nf = #given above
# # theta_i = #given above
# # y_nf = #given above
# theta_i = 30*np.pi/180
# weight = 0.75 #omega as weight
# t_amax = 6 #max time to lane change
# a_smax = 3 #maximum side distance
# tau = 0.1

# # print("u_ni:", u_ni, ",theta_i:", theta_i, ",y_nf:", y_nf, ",weight:", weight, ",t_amax:", t_amax, ",a_smax:", a_smax)
# # x_nf_of_cost = np.linspace(1, 5, 1000)
# x_nf_of_cost = np.arange(1, 101, 1)
# y_of_cost = cost_j(u_ni, x_nf_of_cost, y_nf, theta_i, weight, t_amax, a_smax, tau)
# plt.plot(x_nf_of_cost, y_of_cost)
# plt.show()

#==============================================================================
#------------------------------------------------------------------------------
# # Matplotlib interactive graph using slider for value change
# from matplotlib.widgets import Button, Slider

# def f(t, amplitude, frequency):
#     return amplitude * np.sin(2 * np.pi * frequency * t)

# t = np.linspace(0, 1, 1000)

# init_amplitude = 5
# init_frequency = 3 


# fig, ax = plt.subplots()
# line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
# ax.set_xlabel('Time [s]')

# fig.subplots_adjust(left = 0.25, bottom = 0.25)
# axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
# freq_slider = Slider(
#     ax = axfreq,
#     label = 'Frequency [Hz]',
#     valmin = 0.1,
#     valmax = 30,
#     valinit = init_frequency,
# )

# axamp = fig.add_axes([0.1, 0.25, 0.025, 0.63])
# amp_slider = Slider(
#     ax = axamp,
#     label = 'Amplitude',
#     valmin = 0,
#     valmax = 10,
#     valinit = init_amplitude,
#     orientation = "vertical"
# )

# def update(val):
#     line.set_ydata(f(t, amp_slider.val, freq_slider.val))
#     fig.canvas.draw_idle()

# freq_slider.on_changed(update)
# amp_slider.on_changed(update)

# resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', hovercolor = '0.975')

# def reset(event):
#     freq_slider.reset()
#     amp_slider.reset()
# button.on_clicked(reset)

# plt.show()

# ==============================================================================
# ------------------------------------------------------------------------------
# applying slider to Cost function(cost_j) and trajectory function (y_n)

# from matplotlib.widgets import Button, Slider
# #cost_j(u_ni, x_nf, y_nf, theta_i, weight, t_amax, a_smax, tau = 0.7)

# init_u_ni = 27
# init_x_nf = np.linspace(1, 300, 301)
# init_y_nf = 7
# init_theta_i = 0
# init_weight = 0.75
# init_t_amax = 6
# init_a_smax = 3
# init_tau = 0.7

# fig, ax = plt.subplots()
# # (u_ni, x_nf, y_nf, theta_i, weight = 0.75)

# cost_y = []
# for i in init_x_nf:
#     # cost_j(x_nf, u_ni, weight, theta_i, y_nf = 7, t_amax = 6, a_smax = 3, tau = 0.7)
#     cost = cost_j(i, init_u_ni, init_weight, init_theta_i, init_y_nf, init_t_amax, init_a_smax, init_tau)
#     cost_y.append(cost)
# line, = ax.plot(init_x_nf, cost_y)
# ax.set_title('Cost Function vs its parameter')
# ax.set_xlim([0, 310])
# ax.set_ylim([-500, 500])
# ax.set_xlabel('x_nf(m)')
# ax.set_ylabel('cost')

# fig.subplots_adjust(left = 0.2, bottom = 0.25)

# #-----------left side sliders
# ax_init_vel = fig.add_axes([0.01, 0.25, 0.025, 0.63])
# init_vel_slider = Slider(
#     ax = ax_init_vel,
#     label = 'u_i',
#     valmin = 0,
#     valmax = 50,
#     valinit = init_u_ni,
#     orientation = 'vertical'
# )

# ax_init_y_nf = fig.add_axes([0.05, 0.25, 0.025, 0.63])
# y_nf_slider = Slider(
#     ax = ax_init_y_nf,
#     label = 'y_nf',
#     valmin = 0,
#     valmax = 14,
#     valinit = init_y_nf,
#     orientation = 'vertical'
# )

# ax_init_theta_i = fig.add_axes([0.09, 0.25, 0.025, 0.63])
# theta_i_slider = Slider(
#     ax = ax_init_theta_i,
#     label = 'θ_i',
#     valmin = 0,
#     valmax = np.pi/2,
#     valinit = init_theta_i,
#     orientation = 'vertical'
# )
# #-----------bottom sliders
# ax_init_weight = fig.add_axes([0.1, 0.01, 0.63, 0.025])
# weight_slider = Slider(
#     ax = ax_init_weight,
#     label = 'weight',
#     valmin = 0,
#     valmax = 1,
#     valinit = init_weight,
#     # orientation = 'vertical'
# )

# ax_init_t_amax = fig.add_axes([0.1, 0.05, 0.63, 0.025])
# t_amax_slider = Slider(
#     ax = ax_init_t_amax,
#     label = 'max time',
#     valmin = 0,
#     valmax = 10,
#     valinit = init_t_amax,
#     # orientation = 'vertical'
# )

# ax_init_a_smax = fig.add_axes([0.1, 0.09, 0.63, 0.025])
# a_smax_slider = Slider(
#     ax = ax_init_a_smax,
#     label = 'a_smax',
#     valmin = 0,
#     valmax = 5,
#     valinit = init_a_smax,
#     # orientation = 'vertical'
# )

# ax_init_tau = fig.add_axes([0.1, 0.13, 0.63, 0.025])
# tau_slider = Slider(
#     ax = ax_init_tau,
#     label = 'tau',
#     valmin = 0,
#     valmax = 1.5,
#     valinit = init_tau,
#     # orientation = 'vertical'
# )

# #controlling the range of axes
# ax_xlim = fig.add_axes([0.2, 0.95, 0.63, 0.025])
# xlim_slider = Slider(
#     ax = ax_xlim,
#     label = 'X_lim',
#     valmin = 0, 
#     valmax = 2000,
#     valinit = 300
# )

# ax_ylim = fig.add_axes([0.92, 0.25, 0.025, 0.63])
# ylim_slider = Slider(
#     ax = ax_ylim,
#     label = 'Y_lim',
#     valmin = 0,
#     valmax = 2000,
#     valinit = 300,
#     orientation = 'vertical'
# )

# def update(val):
#     # line.set_ydata(cost_j(init_u_ni, init_x_nf, init_y_nf, init_theta_i, init_weight, init_t_amax, init_a_smax, init_tau))
#     # line.set_ydata(cost_j(init_vel_slider.val, init_x_nf, y_nf_slider.val, theta_i_slider.val, weight_slider.val, t_amax_slider.val, a_smax_slider.val, tau_slider.val))
#     cost_y = []
#     for i in init_x_nf:
#         cost = cost_j(i, init_vel_slider.val, weight_slider.val, theta_i_slider.val, y_nf_slider.val, t_amax_slider.val, a_smax_slider.val, tau_slider.val)
#         cost_y.append(cost)
#     line.set_ydata(cost_y)
#     ax.set_xlim([-xlim_slider.val, xlim_slider.val])
#     ax.set_ylim([-ylim_slider.val, ylim_slider.val])
#     fig.canvas.draw_idle()

# init_vel_slider.on_changed(update)
# y_nf_slider.on_changed(update)
# theta_i_slider.on_changed(update)
# weight_slider.on_changed(update)
# t_amax_slider.on_changed(update)
# a_smax_slider.on_changed(update)
# tau_slider.on_changed(update)
# xlim_slider.on_changed(update)
# ylim_slider.on_changed(update)

# reset_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
# button1 = Button(reset_ax, 'Reset', hovercolor=0.975)

# def reset(event):
#     init_vel_slider.reset()
#     y_nf_slider.reset()
#     theta_i_slider.reset()
#     weight_slider.reset()
#     t_amax_slider.reset()
#     a_smax_slider.reset()
#     tau_slider.reset()
#     xlim_slider.reset()
#     ylim.slider.reset()

# button1.on_clicked(reset)
# plt.show()

#==============================================================================
#------------------------------------------------------------------------------
# ==============================================================================
# ------------------------------------------------------------------------------
# applying slider to lateral trajectory function

# from matplotlib.widgets import Button, Slider

# init_x_nf = 20
# init_y_nf = 7
# init_theta_i = 0
# x_n = np.linspace(0, 300, 301)
# fig, ax = plt.subplots()

# line, = ax.plot(x_n, y_n(init_x_nf, init_y_nf, x_n, init_theta_i*np.pi/180))
# point, = ax.plot([0, init_x_nf], [0, init_y_nf], 'o')

# ax.set_title('Trajcectory vs x_nf')
# ax.set_xlim([0, 310])
# ax.set_ylim([-500, 500])
# ax.set_xlabel('x_n')
# ax.set_ylabel('y_n')

# ax.axhline(y = init_y_nf, ls = ':', lw = 2, color = 'r')
# ax.axhline(y = 0, ls = '-.', lw = 1, color = 'g')
# ax.axvline(x = init_x_nf, ls = ':', lw = 2, color = 'r')

# fig.subplots_adjust(left = 0.2, bottom = 0.25)

# #-----------left side sliders
# ax_x_nf = fig.add_axes([0.01, 0.25, 0.025, 0.63])
# x_nf_slider = Slider(
#     ax = ax_x_nf,
#     label = 'x_nf',
#     valmin = 1,
#     valmax = 200,
#     valinit = init_x_nf,
#     orientation = 'vertical'
# )

# ax_init_y_nf = fig.add_axes([0.05, 0.25, 0.025, 0.63])
# y_nf_slider = Slider(
#     ax = ax_init_y_nf,
#     label = 'y_nf',
#     valmin = 0,
#     valmax = 14,
#     valinit = init_y_nf,
#     orientation = 'vertical'
# )

# ax_init_theta_i = fig.add_axes([0.09, 0.25, 0.025, 0.63])
# theta_i_slider = Slider(
#     ax = ax_init_theta_i,
#     label = 'θ_i',
#     valmin = 0,
#     valmax = 90,
#     valinit = init_theta_i,
#     orientation = 'vertical'
# )

# # #controlling the range of axes
# ax_xlim = fig.add_axes([0.2, 0.95, 0.63, 0.025])
# xlim_slider = Slider(
#     ax = ax_xlim,
#     label = 'X_lim',
#     valmin = 0, 
#     valmax = 2000,
#     valinit = 310
# )

# ax_ylim = fig.add_axes([0.92, 0.25, 0.025, 0.63])
# ylim_slider = Slider(
#     ax = ax_ylim,
#     label = 'Y_lim',
#     valmin = 0,
#     valmax = 2000,
#     valinit = 500,
#     orientation = 'vertical'
# )

# def update(val):
#     global x_n
#     # ax.cla()
#     line.set_ydata(y_n(x_nf_slider.val, y_nf_slider.val, x_n, theta_i_slider.val * np.pi/180))
    
#     ax.axhline(y = y_nf_slider.val, ls = ':', lw = 0.5, color = 'r')
#     ax.axhline(y = 0, ls = '-.', lw = 2, color = 'g')
#     ax.axvline(x = x_nf_slider.val, ls = ':', lw = 1, color = 'r')
#     point, = ax.plot([0, x_nf_slider.val], [0, y_nf_slider.val], 'o')

#     ax.set_xlim([-xlim_slider.val, xlim_slider.val])
#     ax.set_ylim([-ylim_slider.val, ylim_slider.val])
#     fig.canvas.draw_idle()
    
# x_nf_slider.on_changed(update)
# y_nf_slider.on_changed(update)
# theta_i_slider.on_changed(update)
# xlim_slider.on_changed(update)
# ylim_slider.on_changed(update)

# reset_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
# button1 = Button(reset_ax, 'Reset', hovercolor=0.975)

# def reset(event):
#     x_nf_slider.reset()
#     y_nf_slider.reset()
#     theta_i_slider.reset()
#     xlim_slider.reset()
#     ylim_slider.reset()

# button1.on_clicked(reset)
# plt.show()

#==============================================================================
#------------------------------------------------------------------------------
#Testing Range of collision avoidance and rollover avoidance
# import numpy as np 
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Button, Slider
# from Collision_avoidance_algorithm import get_Collision_Avoidance_Range
# # get_Collision_Avoidance_Range(x_ni, x_nf, y_nf, theta_i, x_pvi, v_pvi, x_lvi, v_lvi, u_ni)

# from Rollover_algorithm import rollover_position
# # rollover_position(u_ni, y_nf)

# x_ni = 10
# x_nf = 100
# y_nf = 3.5
# theta_i = 0
# v_pvi = 15
# v_lvi = 15
# u_ni = 22
# x_pvi = 70
# x_lvi = 30

# collision_low_lim, collision_up_lim = get_Collision_Avoidance_Range(x_ni, x_nf, y_nf, theta_i, x_pvi, v_pvi, x_lvi, v_lvi, u_ni)
# rollover_low_lim = rollover_position(u_ni, y_nf)

# fig, ax = plt.subplots()

# ax.set_xlabel('X')
# ax.set_ylabel('Y')

# ax.set_xlim(-3, 300)
# ax.set_ylim(-3, 3)

# collision_range_x = np.linspace(collision_low_lim, collision_up_lim, 100)
# collision_range_y = np.zeros(100) + 1
# line1, = ax.plot(collision_range_x, collision_range_y, 'k')

# left_line1_x = np.zeros(100) + collision_low_lim
# left_line1_y = np.linspace(0, 1, 100)
# left_line1, = ax.plot(left_line1_x, left_line1_y, 'k')

# right_line1_x = np.zeros(100) + collision_up_lim
# right_line1_y = np.linspace(0, 1, 100)
# right_line1, = ax.plot(right_line1_x, right_line1_y, 'k')

# rollover_range_x = np.linspace(rollover_low_lim, 1000, 1000)
# rollover_range_y = np.zeros(1000)
# line2, = ax.plot(rollover_range_x, rollover_range_y, 'g')


# fig.subplots_adjust(left = 0.2, bottom = 0.25)

# #-----------left side sliders
# ax_init_vel = fig.add_axes([0.01, 0.25, 0.025, 0.63])
# init_vel_slider = Slider(
#     ax = ax_init_vel,
#     label = 'u_ni',
#     valmin = 1,
#     valmax = 50,
#     valinit = u_ni,
#     orientation = 'vertical'
# )

# ax_init_y_nf = fig.add_axes([0.05, 0.25, 0.025, 0.63])
# y_nf_slider = Slider(
#     ax = ax_init_y_nf,
#     label = 'y_nf',
#     valmin = 0,
#     valmax = 14,
#     valinit = y_nf,
#     orientation = 'vertical'
# )

# ax_init_theta_i = fig.add_axes([0.09, 0.25, 0.025, 0.63])
# theta_i_slider = Slider(
#     ax = ax_init_theta_i,
#     label = 'θ_i',
#     valmin = 0,
#     valmax = 90,
#     valinit = theta_i,
#     orientation = 'vertical'
# )
# #-----------bottom sliders
# ax_init_x_nf = fig.add_axes([0.1, 0.01, 0.63, 0.025])
# x_nf_slider = Slider(
#     ax = ax_init_x_nf,
#     label = 'x_nf',
#     valmin = 1,
#     valmax = 200,
#     valinit = x_nf,
#     # orientation = 'vertical'
# )

# #controlling the range of axes
# # ax_xlim = fig.add_axes([0.2, 0.95, 0.63, 0.025])
# # xlim_slider = Slider(
# #     ax = ax_xlim,
# #     label = 'X_lim',
# #     valmin = 0, 
# #     valmax = 20,
# #     valinit = 300
# # )

# # ax_ylim = fig.add_axes([0.92, 0.25, 0.025, 0.63])
# # ylim_slider = Slider(
# #     ax = ax_ylim,
# #     label = 'Y_lim',
# #     valmin = 0,
# #     valmax = 20,
# #     valinit = 3,
# #     orientation = 'vertical'
# # )

# def update(val):
#     global x_ni, x_pvi, v_pvi, x_lvi, v_lvi

#     collision_low_lim, collision_up_lim = get_Collision_Avoidance_Range(x_ni, x_nf_slider.val, y_nf_slider.val, theta_i_slider.val, x_pvi, v_pvi, x_lvi, v_lvi, init_vel_slider.val)
#     rollover_low_lim = rollover_position(init_vel_slider.val, y_nf_slider.val)

#     collision_range_x = np.linspace(collision_low_lim, collision_up_lim, 100)
#     collision_range_y = np.zeros(100) + 1
#     line1, = ax.plot(collision_range_x, collision_range_y, 'k')

#     left_line1_x = np.zeros(100) + collision_low_lim
#     left_line1_y = np.linspace(0, 1, 100)
#     left_line1, = ax.plot(left_line1_x, left_line1_y, 'k')

#     right_line1_x = np.zeros(100) + collision_up_lim
#     right_line1_y = np.linspace(0, 1, 100)
#     right_line1, = ax.plot(right_line1_x, right_line1_y, 'k')

#     rollover_range_x = np.linspace(rollover_low_lim, 1000, 1000)
#     rollover_range_y = np.zeros(1000)
#     line2, = ax.plot(rollover_range_x, rollover_range_y, 'g')

#     # ax.set_xlim([-xlim_slider.val, xlim_slider.val])
#     # ax.set_ylim([-ylim_slider.val, ylim_slider.val])
#     fig.canvas.draw_idle()

# init_vel_slider.on_changed(update)
# y_nf_slider.on_changed(update)
# theta_i_slider.on_changed(update)
# x_nf_slider.on_changed(update)
# # xlim_slider.on_changed(update)
# # ylim_slider.on_changed(update)

# reset_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
# button1 = Button(reset_ax, 'Reset', hovercolor=0.975)

# def reset(event):
#     init_vel_slider.reset()
#     y_nf_slider.reset()
#     theta_i_slider.reset()
#     x_nf_slider.reset()
#     # xlim_slider.reset()
#     # ylim.slider.reset()

# button1.on_clicked(reset)
# plt.show()

#==============================================================================
#------------------------------------------------------------------------------
# Collision avoidance and rollover avoidance slider

import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider
from Collision_avoidance_algorithm import get_Collision_Avoidance_Range
from Rollover_algorithm import rollover_position

collision_low, collision_up = get_Collision_Avoidance_Range(10, 169.02344799, 7, 0, 70, 20, 30, 20, 27)
rollover_low = rollover_position(27, 7)  

fig, ax = plt.subplots()
ax.set_xlabel('xn')
ax.set_ylabel('yn')
ax.set_xlim(-10, 1300)
ax.set_ylim(-10, 50)
ax.set_title("Collision Avaidance and Rollover Range")

collision_range, = ax.plot([collision_low, collision_up], [10, 10], 'o:g', label="collision")
rollover_range, = ax.plot([rollover_low, 1000], [30, 30], 'o-.k', label="rollover")

ax.legend()

def update_range(val):
    # ax.clear()
    collision_xy = get_Collision_Avoidance_Range(10, 169.02344799, 7, 0, 70, 20, 30, 20, init_vel.val)
    collision_range.set_data([collision_xy[0], collision_xy[1]], [10, 10])
    rollover_range.set_data([rollover_position(init_vel.val, 7), 1000], [30, 30])
    # plt.draw()
    fig.canvas.draw_idle()

plt.grid()
ax_slider = plt.axes([0.13, 0, 0.5, 0.02])

init_vel = Slider(ax_slider, "u_ni", valmin = 22, valmax = 28, valinit = 25, valstep = 0.5)
init_vel.on_changed(update_range)
plt.show()