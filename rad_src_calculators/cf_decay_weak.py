# **************************************************************************
# FUNCTION, CF_DECAY_WEAK(datef): Computes the activity (fissions/sec) of our
#      Cf-252 source on a given date 
# Andreas Enqvist (Shaun D. Clarke)
# 10 Nov 2010
# modifed by
# Brice Turner
# March 2023
#
# INPUTS: datef = date string in DD-MMM-YYYY format (e.g. 16-Dec-2009)
# OUTPUTS: The spontaneous fission activity in both fissions/sec and
#    neutrons/sec on the specified date.
# Example: cf_decay_weak('16-Nov-2010')
# **************************************************************************

import numpy as np
from datetime import datetime

def cf_decay_weak(datef_str):
    A0 = 50                            # initial source activity (uCi)
    date0_str = '15-May-2005'          # date of initial source activity
    t_half = 2.645                     # half life (yrs)
    br = 0.0309                        # spontaneous fission branching ratio
    nubar = 3.757                      # neutrons per fission from PANDA

    t_half_s = t_half * 31556926       # half life (sec)
    lambda_ = np.log(2) / t_half_s     # decay constant (sec)
    N0 = A0 * 1e-6 * 3.7e10            # initial activity in Bq

    date_format = "%d-%b-%Y"
    t0 = datetime.strptime(date0_str, date_format)
    tf = datetime.strptime(datef_str, date_format)
    
    dt = (tf - t0).total_seconds()     # sec

    Nf = br * N0 * np.exp(-lambda_ * dt)  # final spontaneous fission activity (Bq)
    print(f"""
The reference source activity is {A0} uCi, recorded on {date0_str}.
The source activity on {datef_str} is {Nf/br/N0*A0} uCi.
The spontaneous fission activity on {datef_str} is {Nf} fissions per second.
The neutron emission rate on {datef_str} is {nubar*Nf} neutrons per second.
    """)

cf_decay_weak('16-Nov-2010')
