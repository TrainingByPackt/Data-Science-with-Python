# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 04:58:38 2019

@author: aengland
"""

# Loops to demonstrate scaling


# min-max normalization
list_of_numbers = [3,5,4,7,4,3]
# calculate the minimum of the list
minimum_of_list = min(list_of_numbers)
# calculate the maximum of the list
maximum_of_list = max(list_of_numbers)
# calculate the denominator
denominator = maximum_of_list - minimum_of_list
# calculate the numerator
numerator = list_of_numbers[0] - minimum_of_list
# calculate the min-max normed value
min_max_normed_value = numerator/denominator
print(min_max_normed_value)

# min-max normalization loop
list_of_numbers = [3,5,4,7,4,3]
# calculate the minimum of the list
minimum_of_list = min(list_of_numbers)
# calculate the maximum of the list
maximum_of_list = max(list_of_numbers)
# calculate the denominator
denominator = maximum_of_list - minimum_of_list
# instantiate an empty list for which to append
min_maxed_list_of_numbers = []
for i in range(len(list_of_numbers)): 
    # calculate the numerator
    numerator = list_of_numbers[i] - minimum_of_list
    # calculate the min-max normed value
    min_max_normed_value = numerator/denominator
    # append the min max normed value to the empty list
    min_maxed_list_of_numbers.append(min_max_normed_value)
print(min_maxed_list_of_numbers)

# z-score
list_of_numbers = [3,5,4,7,4,3]
# get mean
import numpy as np
mean_of_list = np.mean(list_of_numbers)
# get denominator (i.e., sd)
denominator = np.std(list_of_numbers)
# get numerator
numerator = list_of_numbers[0] - mean_of_list
# calculate z score
z_score = numerator/denominator
print(z_score)

# z-score loop
list_of_numbers = [3,5,4,7,4,3]
# get mean
import numpy as np
mean_of_list = np.mean(list_of_numbers)
# get denominator (i.e., sd)
denominator = np.std(list_of_numbers)
# instantiate empty list for which to append z-scores
z_score_list = []
for i in range(len(list_of_numbers)):
    # get numerator
    numerator = list_of_numbers[i] - mean_of_list
    # calculate z score
    z_score = numerator/denominator
    # append z score to z_score_list
    z_score_list.append(z_score)
print(z_score_list)







