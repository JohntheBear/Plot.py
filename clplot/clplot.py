#! /usr/bin/env python

# Part of CLP
# A universal command line plotting script
#
# John Novak
# June 4, 2012 - July 19, 2012

# Run with: python clplot.py
# or just: ./clplot.py (after making it executable, obviously)

# written for Python 2.6. Requires Scipy, Numpy, and Matplotlib

import numpy as np
import globe
from structure import unstruct_plot
from helpers import read_flags, remove_empties
from plot import plot
from data_handler import read_data, detect_blocks, readdat


def main():
    dic = globe.dic
    read_flags()

    for filename in dic['files']:
        if dic['Verbose'] > 0:
            print "plotting", filename
        sys_err = dic['sys_err_default']
        if len(filename.split('#')) == 2:
            sys_err = float(filename.split('#')[1].strip())
            filename = filename.split('#')[0].strip()
        output = None
        if dic['outputs']:
            output = dic['outputs'].pop(0)
        dic['numbered'] = 0

        # Now read data file
        data = read_data(filename)

        # Make decisions about what is in the file
        if len(data) > 0:
            struct = detect_blocks(data)

            # KN: This can be done far more efficiently using a filter()
            # function. Either specify a one liner using a lambda function or
            # write a function that returns True or False
            struct, data = remove_empties(struct, data)

            # Plot the stuff
            for i in range(len(struct)):
                dic['currentstruct'] = i
                dic['Numbering'] = len(struct) > 1
                x = readdat(struct, i, data)
                unstruct_plot(np.array(x))

    if dic['remnants']:
        plot(dic['remnants'], dic['remnanterrors'], Force=True)


if __name__ == '__main__':
    """A Python program that takes a file or list of filesand creates plots of
    the data."""
    dic = globe.dic
    main()
