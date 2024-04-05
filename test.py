import numpy as np
import matplotlib.pyplot as plt
import math
from Collision_avoidance_algorithm import total_LaneChangeTime as Total_time
from scipy.optimize import minimize

def y_n(x_nf, y_nf, x_n, theta_i):
    theta_i = math.radians(theta_i)
    a_0 = 0
    a_1 = np.tan(theta_i)
    a_2 = (3*y_nf - 2*x_nf*np.tan(theta_i))/(x_nf**2)
    a_3 = (x_nf*np.tan(theta_i) - 2*y_nf)/(x_nf**3)
    
    return a_0 + a_1*x_n + a_2*(x_n**2) + a_3*(x_n**3)

def a_sf(u_ni, x_nf, theta_i, y_nf):
    theta_i = theta_i * np.pi / 180
    K = abs((2*x_nf*np.tan(theta_i) - 6*y_nf)/(x_nf**2))
    return (u_ni**2)*K

t_amax = 6
a_smax = 3
tau = 0.7

def cost_j(x_nf, u_ni, weight, theta_i, y_nf = 7, t_amax = 6, a_smax = 3, tau = 0.7):

    t_a = Total_time(x_nf, y_nf, theta_i, u_ni)
    a = a_sf(u_ni, x_nf, theta_i, y_nf) 
    comfort = weight * ((a/a_smax)**2)
    efficiency = (1 - weight)*t_a/t_amax

    print(f"a_sf: {a :.2f}, t_a: {t_a :.2f}, cost: {comfort + efficiency}")

    return comfort + efficiency

cost_j(150, 15, 0.75, 0)






















































# ==============================================================================
# ------------------------------------------------------------------------------
## 3D plotting of Cost function

# import numpy as np 
# import matplotlib.pyplot as plt 
# from Optimal_trajectory_algorithm import cost_j

# # def cost_j(x_nf, y_nf, u_ni, theta_i, weight = 0.75, t_amax = 6, a_smax = 3, tau = 0.7):
# uni = 20
# # theta_i = 45
# weight = 0.5

# xnf = np.linspace(1, 200, 200)
# ynf = np.linspace(0, 90, 200)
# X, Y = np.meshgrid(xnf, ynf)
# Z = np.zeros((200, 200))

# for i in range(200):
#     for j in range(200):
#         Z[i][j] = (cost_j(X[i][j], 7, uni, Y[i][j], weight))

# ax = plt.subplot(projection = '3d', computed_zorder = False)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3D Surface Plot')

# ax.plot_surface(X, Y, Z, cmap = 'viridis', zorder = 0)
# # # ax.scatter(current_pos[0], current_pos[1], current_pos[2], color = "magenta", zorder = 1)
# points_x = [9.38682514]
# points_y = [0]
# points_z = [cost_j(x, 7, uni, y, weight) for x, y in zip(points_x, points_y)]
# print(points_z)
# ax.scatter(points_x, points_y, points_z, color='red', label='Points', zorder = 1)

# for i, (x, y, z) in enumerate(zip(points_x, points_y, points_z)):
#     ax.text(x, y, z, f'({x}, {y}, {z:.2f})', color='magenta', fontsize=10)

# plt.show()

# ==============================================================================
# ------------------------------------------------------------------------------
### 3D plotting graph, and points

# from mpl_toolkits import mplot3d
# import numpy as np 
# import matplotlib.pyplot as plt

# # def f1(x, y):
# #     return x * (y**2) - (x**2) - (y**2)
# # x = np.linspace(1, 3, 20)
# # y = np.linspace(2, 3, 20)

# x = np.linspace(0, 5, 20)
# y = np.linspace(0, 5, 20)

# # X, Y = np.meshgrid(x, y)
# # z = X * (Y**2) - (X**2) - (Y**2)

# z = x * (y**2) - (x**2) - (y**2)
# print(z)

# fig = plt.figure()
# ax = plt.axes(projection = '3d')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3D Surface Plot')

# # ax.plot_surface(x, y, z)
# ax.plot(x, y, z)

# points_x = [1, 1, 2.5, 3]
# points_y = [3, 2.5, 2, 2]
# points_z = [(x * (y**2) - (x**2) - (y**2)) for x, y in zip(points_x, points_y)]
# ax.scatter(points_x, points_y, points_z, color='red', label='Points')

# for i, (x, y, z) in enumerate(zip(points_x, points_y, points_z)):
#     ax.text(x, y, z, f'({x}, {y}, {z:.2f})', color='black', fontsize=10)

# ax.legend()

# plt.show()

# ==============================================================================
# ------------------------------------------------------------------------------
## 3D plotting graph and points

# import numpy as np 
# import matplotlib.pyplot as plt 

# def func(x, y):
#     return x * (y**2) - (x**2) - (y**2)

# def dfdx(x, y):
#     return -2*x + (y**2)

# def dfdy(x, y):
#     return -2*y + 2*x*y

# x = np.linspace(1, 3, 30)
# y = np.linspace(2, 3, 30)

# X, Y = np.meshgrid(x, y)
# Z = func(X, Y)

# current_pos = [1, 2, func(1, 2)]
# learning_rate = 0.01

# ax = plt.subplot(projection = '3d', computed_zorder = False)

# for _ in range(50):
#     X_derivative, Y_derivative = dfdx(current_pos[0], current_pos[1]), dfdy(current_pos[0], current_pos[1])
#     X_new, Y_new = current_pos[0] - learning_rate * X_derivative, current_pos[1] - learning_rate * Y_derivative
#     if X_new >= 1 and X_new <= 3:
#         current_pos[0] = X_new
#     if Y_new >= 2 and Y_new <= 3: 
#         current_pos[1] = Y_new
#     if (X_new >= 1 and X_new <= 3) and (Y_new >= 2 and Y_new <= 3):
#         current_pos[2] = func(X_new, Y_new)

#     # print(current_pos[2])

# #     # ax.set_xlabel('X')
# #     # ax.set_ylabel('Y')
# #     # ax.set_zlabel('Z')
# #     # ax.set_title('3D Surface Plot')

# #     ax.plot_surface(X, Y, Z, cmap = 'viridis', zorder = 0)
# #     ax.scatter(current_pos[0], current_pos[1], current_pos[2], color = "magenta", zorder = 1)
# #     plt.pause(0.001)
# #     ax.clear()

# print(f"Optimal function value: {current_pos[2]}, \n for x: {current_pos[0]}, y: {current_pos[1]}")

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3D Surface Plot')

# ax.plot_surface(X, Y, Z, cmap = 'viridis', zorder = 0)
# # ax.scatter(current_pos[0], current_pos[1], current_pos[2], color = "magenta", zorder = 1)
# points_x = [1, 1, 2.5, 3]
# points_y = [3, 2.5, 2, 2]
# points_z = [(x * (y**2) - (x**2) - (y**2)) for x, y in zip(points_x, points_y)]
# print(points_z)
# ax.scatter(points_x, points_y, points_z, color='red', label='Points')

# for i, (x, y, z) in enumerate(zip(points_x, points_y, points_z)):
#     ax.text(x, y, z, f'({x}, {y}, {z:.2f})', color='magenta', fontsize=10)

# plt.show()