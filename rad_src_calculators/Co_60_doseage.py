#!/usr/bin/python
# mirion dosimetry data

# **************************************************************************
# FUNCTION, co60dosage(datef): Computes the activity (fissions/sec) of our 
# C0-60 source on a given date 
# Andreas Enqvist
# 15  December 2020
# modifed by
# Brice Turner
# March 2023
# INPUTS: datef = date string in DD-MMM-YYYY format (e.g. 16-Dec-2019)
# OUTPUTS: apporoximate radiation dose (physical dose), and irradiation 
# time to a certain dosage % (depends on source distance i nthe gamma-
# irradiator of course). USed for the standard NASA-project bacetria 
# container
# Example: co60dosage('16-Nov-2021')
# **************************************************************************

import datetime
import math

def co60dosage(datef):
    A0 = 600 # initial activity of the strong source (Ci) from Susan
    date0 = '08-Mar-1999' # date of initial source activity
    t_half = 5.2713 # half life (yrs)
    br = 0.9988 # 2-gamma-decay branching ratio
    gammaE = br * 1.1732 + 1.3325 # E in MeV
    e_charge = 1.609e-19 # J/eV

    t_half_s = t_half * 31556926 # half life (sec)
    lambda_ = math.log(2) / t_half_s # decay constant (sec)
    N0 = A0 * 3.7e10 # initial activity in Bq
    t0 = datetime.datetime.strptime(date0, '%d-%b-%Y').toordinal()
    tf = datetime.datetime.strptime(datef, '%d-%b-%Y').toordinal()
    dt = (tf - t0) * 86400 # sec

    GBq = br * N0 * math.exp(-lambda_ * dt) # final Decay activity (Bq)
    Strength = GBq / N0 * A0 # final activity in Ci
    print(f'\nThe reference source activity is {A0} Ci, recorded on {date0}.\n')
    print(f'The source activity on {datef} is {Strength} Ci.')
    print(f'The decay activity on {datef} is {GBq} decays per second.')
    print(f'The gamma-energy emission rate on {datef} is {gammaE * GBq} MeV gamma-rays co60 per second.')
    print(f'The gamma-energy emission rate on {datef} is {gammaE * GBq * 1e6 * e_charge} Joule of gamma-rays from co60 per second.\n')

    co60dose_h = 34 * 13.2 / 10 # co-60 conversion factor * exposure constant per minutes
    co60dose_m = co60dose_h / 60 # co-60 conversion factor * exposure constant per minutes
    test = co60dose_m * Strength / 34 # dose per minute
    T_1000 = 1000 / test # time to 1000 Gy

    print(f'On {datef}, dose in Gy/minute is {test}.')
    print(f'On {datef}, time to irradiate to 1000 Gy is {T_1000} minutes / {T_1000 / 60} hours.\n')


if __name__ == '__main__':
    co60dosage('16-Nov-2021')
