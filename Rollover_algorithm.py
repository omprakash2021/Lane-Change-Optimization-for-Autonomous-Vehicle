#a_sf = maximum side acceleration
#a_sr = rollover side acceleration threshold value(1.4)
#(a_sf < a_sr) => to avoid rollover of the vehicle

import numpy as np

a_sr = 1.4

def rollover_position(u_ni, y_nf):
    global a_sr
    #rollver lower boundary = x_nr
    x_nr = (6*y_nf*u_ni)/(np.sqrt(6*y_nf*a_sr))
    #to avoid rollover, x_nf should be in range (x_nr, infinity)
    return x_nr
    