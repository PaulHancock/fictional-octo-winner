#! /usr/bin/env python
"""Determine Andromeda location in ra/dec degrees"""

from math import cos, pi
from random import uniform


NSRC = 1_000_000
# from wikipedia
RA_STR = '00:42:44.3'
DEC_STR = '41:16:09'


def make_positions():
    # convert to decimal degrees
    d, m, s = DEC_STR.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA_STR.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/cos(dec*pi/180)


    # make 1000 stars within 1 degree of Andromeda
    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + uniform(-1,1))
        decs.append(dec + uniform(-1,1))
    return ras, decs


def clip_to_radius():
    return


def save_positions(ras, decs):
    # now write these to a csv file for use by my other program
    with open('catalog.csv','w', encoding='utf8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)


def main():
    ras, decs = make_positions()
    save_positions(ras, decs)


if __name__ == "__main__":
    main()