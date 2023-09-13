# ############################################################################
# FUNCTION, CF_DECAY_200(datef): Computes the activity (fissions/sec) of our 
# (200uCi) Cf-252 source on a given date 
# (C)
# Andreas Enqvist 
# 10 Nov 2016
# modifed by
# Brice Turner
# March 2023
#
# INPUTS: datef = date string in DD-MMM-YYYY format (e.g. 16-Dec-2019)
# OUTPUTS: The spontaneous fission activity in both fissions/sec and
# neutrons/sec on the specified date.
# Example: cf_decay_200('16-Nov-2018')
# ############################################################################

import datetime
import math

def cf_decay_200(datef):
    A0 = 200 # initial source activity (uCi)
    date0 = '15-April-2014' # date of initial source activity 
    t_half = 2.645 # half life (yrs)
    br = 0.0309 # spontaneous fission branching ratio
    nubar = 3.757 # neutrons per fission from PANDA
    
    t_half_s = t_half * 31556926 # half life (sec)
    lambda_ = math.log(2) / t_half_s # decay constant (sec)
    N0 = A0 * 1e-6 * 3.7e10 # initial activity in Bq
    t0 = datetime.datetime.strptime(date0, '%d-%B-%Y') # serial date in days
    tf = datetime.datetime.strptime(datef, '%d-%B-%Y') # serial date in days
    dt = (tf - t0).total_seconds() # sec

    Nf = br * N0 * math.exp(-lambda_ * dt) # final spontaneous fission activity (Bq)
    
    print('\nThe reference source activity is {:.0f} uCi, recorded on {}.'.format(A0, date0))
    print('The source activity on {} is {:.2f} uCi.'.format(datef, Nf / br / N0 * A0))
    print('The spontaneous fission activity on {} is {:.2f} fissions per second.'.format(datef, Nf))
    print('The neutron emission rate on {} is {:.2f} neutrons per second.\n'.format(datef, nubar * Nf))

    
cf_decay_200('01-January-2023')