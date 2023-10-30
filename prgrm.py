import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
a = (5,6,7)
b = (3,6,10)
    # Write your code here
def gain_points():
  pointa = 0
  pointb = 0
  for i in range(3):
    if a[i]>b[i]:
        pointa+=1
    if a[i]<b[i]:
        pointb+=1
  return(pointa,pointb)
print(gain_points())


    


    

