#!/usr/bin/python
# convert_mm_in.py
# go between millimeters and inches
# Brice Turner, 2023

import argparse

def convert_to_inches(mm):
    return mm / 25.4

def convert_to_mm(inch):
    return inch * 25.4

parser = argparse.ArgumentParser(description="Converts measurements in inches to millimeters, and vice versa.")
parser.add_argument("value", type=float, help="The numeric value you want to convert.")
parser.add_argument("unit", type=str, choices=['in', 'mm'], help="The unit of the input value.")

args = parser.parse_args()

if args.unit == 'mm':
    print(f"{args.value} mm = {convert_to_inches(args.value)} in")
else:
    print(f"{args.value} in = {convert_to_mm(args.value)} mm")

# useage: $ python convert_mm_in.py <value> <units: mm or in>
