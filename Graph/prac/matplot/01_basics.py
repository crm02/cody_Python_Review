import matplotlib.pyplot as plt

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()

#When you provide a single list of numbers to the plot function, matplotlib assumes its the y-values and generates 
# x values to go with it

# The plot function is very versitile and will take any number of arguments 

# To graph x and y you can do

#plt.plot([1,2,3,4],[1,4,9,16])
#plt.show()

# Formatting the style of your plot
 # for every x,y pair, there is a third optional argument which is the format string that indicates the color
  # and line type of the plot. The letters and symbols from the format string are from MATLAB, you concatenate a color 
   # string with a line style string, for example, 'ro' is 'red' + '
plt.plot([1,2,3,4],[1,4,9,16], 'ro')
plt.axis((0,6,0,20)) # sets x axis min to max (0-6) and y axis min to max (0,20)
#plt.show()
    # b:blue, g:green, r:red, c:cyan, m:magenta, y:yellow, k:black, w:white
    # o : circle, *:star, .:point, x:xmarker, s:square, D:diamond
    # - : solid line, -- :dashed line, -. : dash-dot line, ':' : dotted line
    # https://www.w3schools.com/python/matplotlib_markers.asp


# In MatplotLib you will typically use numpy arrays (to keep the data?)
# you can make a numpy arrau with np.arrange(value1, value2, ..valueN) where .arrange() creates an array with even spaced
 # values within a specified interval

# arrange( start (optional), stop(requited)(exclusive), step,(optional), dtype(optional))
  # the start parameter will tell numpy what number the array starts with, so what the first value will be, Defaults to 0
   # Stop will tell numpy when to stop adding numbers into the array and will be the last number added
    # step tells numpy what next number in the sequence to add from start to end
     # dtype tells numpy what datatype the output array will have, default case numpy will infer

import numpy as np
arr1 = np.arange(5) # creates and array of [0,1,2,3,4]
print(arr1) 

arr2 = np.arange(2,10,2) # creates an array of [2,4,6,8]
print(arr2)

arr3 = np.arange(5,0,-1) # creates an array of [5,4,3,2,1]
print(arr2) 


t = np.arange(0. , 5. , 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()