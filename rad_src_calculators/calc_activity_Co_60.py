#mirion dosimetry data

# ############################################################################
# FUNCTION, co60dosage(datef): Computes the activity (fissions/sec) of our 
# Co-60 source on a given date 
# (C)
# Andreas Enqvist
# 15 December 2020
# modifed by
# Brice Turner
# March 2023
#
# INPUTS: datef = date string in DD-MMM-YYYY format (e.g. 16-Dec-2019)
# OUTPUTS: apporoximate radiation dose (physical dose), and irradiation 
# time to a certain dosage % (depends on source distance i nthe gamma-
# irradiator of course). USed for the standard NASA-project bacetria 
# container
# Example: co60dosage('16-Nov-2021')
# ############################################################################

import numpy as np
import datetime

def co60dosage(datef):

    #A0 = 5500; # initial source activity (uCi)
    date0 = '08-Mar-1999' # date of initial source activity
    A0 = 600 # initial activity of the strong source (Ci) from Susan
    t_half = 5.2713 # half life (yrs)
    br = 0.9988 # 2-gamma-decay branching ratio

    t_half_s = t_half*31556926 # half life (sec)
    decay_constant = np.log(2)/t_half_s # decay constant (sec)
    N0 = A0*3.7E10 # initial activity in Bq
    t0 = datetime.datetime.strptime(date0, '%d-%b-%Y') # serial date in days
    tf = datetime.datetime.strptime(datef, '%d-%b-%Y') # serial date in days
    dt = (tf - t0).total_seconds() # sec
    gammaE = br*1.1732 + 1.3325 # E in MeV
    e_charge = 1.609E-19 # J/eV

    GBq = br*N0*np.exp(-decay_constant*dt) # final Decay activity (Bq)
    Strength = GBq/N0*A0 # final activity in Ci
    
    co60dose_h = 34*13.2/10 # co-60 conversion factor * exposure constant per minutes
    co60dose_m = co60dose_h/60 # co-60 conversion factor * exposure constant per minutes
    test = co60dose_m*Strength/34 # dose per minute
    T_1000 = 1000/test # time to 1000 Gy
    
    
    print('\nThe reference source activity is', format(A0, 'G'), 'Ci, recorded on', date0, '.')
    print('The source activity on', datef, 'is', format(GBq/N0*A0, 'G'), 'Ci.')
    
    print('The decay activity on', datef, 'is', format(GBq, 'G'), 'decays per second.')
    print('The gamma-energy emission rate on', datef, 'is', format(gammaE*GBq, 'G'), 'MeV gamma-rays Co-60 per second.')
    print('The gamma-energy emission rate on', datef, 'is', format(gammaE*GBq*1e6*e_charge, 'G'), 'Joules of gamma-rays from Co-60 per second.')

    print('On', datef, 'dose in Gy/min is', format(test, 'G'), '.')
    print('On', datef, 'time to irradiate to 1000 Gy is', format(T_1000, 'G'), 'minutes =', format(T_1000/60, 'G'), 'hours.\n')

co60dosage('08-Mar-2023')

