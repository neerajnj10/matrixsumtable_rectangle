# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:06:35 2015

@author: Nj_neeraj
"""

def compute_summed_area_table(image):
    # image is a 2-dimensional array containing ints or floats, with at least 1 element.
    height = len(image)
    width = len(image[0])
    new_image = [[0.0] * width for _ in range(height)] # Create an empty summed area table
    for row in range(0, height):
        for col in range(0, width):
            if (row > 0) and (col > 0):
                new_image[row][col] = image[row][col] + \
                    new_image[row][col - 1] + new_image[row - 1][col] - \
                    new_image[row - 1][col - 1]
            elif row > 0:
                new_image[row][col] = image[row][col] + new_image[row - 1][col]
            elif col > 0:
                new_image[row][col] = image[row][col] + new_image[row][col - 1]
            else:
                new_image[row][col] = image[row][col]
    # Note that two-pass code gives the same kind of results, e.g.:
    #    for row in range(0, height):
    #        for col in range(0, width):
    #            if col > 0:
    #                new_image[row][col] = image[row][col] + new_image[row][col - 1]
    #            else:
    #                new_image[row][col] = image[row][col]
    #    for row in range(0, height):
    #        for col in range(0, height):
    #            if row > 0:
    #                new_image[row][col] += new_image[row - 1][col]
    return new_image


small_image = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
small_sat = compute_summed_area_table(small_image)
print(small_sat)
