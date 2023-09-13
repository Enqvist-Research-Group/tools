#surf_assay_geom.py

import numpy as np
import time

pi = np.pi
time_start = time.time()

# assumes centrally concentric alignment
# (detector centered over sample, or sample
# large enough that it is approximated as
# "infinite" vs the source-det. distance)

# source dimensions (cm?) (silver foil)
S1 = 5.2
S2 = 3.2

# Monte carlo histories:
# (computing time scales linearly
# above N=10^6... 10^7 is ~1s)
N = 10000000

#detector dimension (assume circular cross section)
Rd = 0.6 #use same units for all distances!
h = 3 #height/distance between source and detector

# (forwards) angles to send radiation with
angles = np.random.rand(N,2) 
angles[:,0] = 2*pi*angles[:,0]
angles[:,1] = pi/2*angles[:,1]
# locations from source plate to start from
start = np.random.rand(N,2) 
start[:,0] = S1*start[:,0]-S1/2
start[:,1] = S2*start[:,1]-S2/2

#line distance to get to h(detector) in z-dimension
t1 = h/np.sin(angles[:,1]) 
# location on x axis at a line distance t1
xh = start[:,0] + t1*np.cos(angles[:,1])*np.cos(angles[:,0]) 
# location on y axis at a line distance t1
yh = start[:,1] + t1*np.cos(angles[:,1])*np.sin(angles[:,0]) 
# hits detector if at that point contained
# to a circular disk or detector radius...
hits = np.sum((xh**2+yh**2) < Rd**2) 
# division by 2 to account for half radiation
# going "backwards" away from detector
fraction = hits/N/2 
solidAngle = 4*pi*fraction

print(f'Fraction: {fraction}')
print(f'Solid ange: {solidAngle}')
time_end = time.time() - time_start
print(f'Elapsed time: {time_end} seconds')

