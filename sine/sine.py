import sys
import math
import matplotlib.pyplot as plot

def array_for(points: int = 4, amplitude: float = 1.0):
    '''Takes a number of points as int and a wave amplitude as float,
       instantiates matplotlib plot of one period of a sine wave with given amplitude.
       The instance is represented by an array containing the specified number of points.
       Void function: prints the array and displays the plot of the sine wave.'''
    array = [[point*2/(points-1) for point in range(points)],                                   #generate array using list comprehension
             [amplitude*math.sin(point*2*math.pi/(points-1)) for point in range(points)]]
    fig, waveform_plot = plot.subplots()                                                        #instantiate empty plot
    waveform_plot.plot(array[0], array[1])                                                      #populate plot from array
    for point in range(points):                                                                 #print every array entry using for loop
        print((round(array[0][point], 6), round(array[1][point], 6)))                           #print statement for indexed array entry
    plot.show()                                                                                 #display waveform plot

def array_while(num_of_points: int = 4, amplitude: float = 1.0):
    '''Takes a number of points as int and a wave amplitude as float,
       instantiates matplotlib plot of one period of a sine wave.
       The instance is represented by an array containing the specified number of points.
       Void function: prints the array and displays the plot of the sine wave.'''
    point_num = 0                                                                               #instantiate iteration index
    array = [[],[]]                                                                             #instantiate empty 2D array
    while point_num < num_of_points:                                                            #generate array using while loop 
        array[0].append(point_num*2/(num_of_points-1))                                          #generate indexed x value
        array[1].append(amplitude*math.sin(point_num*math.pi*2/(num_of_points-1)))              #generate indexed sin(x) value
        point_num += 1                                                                          #increment iteration index
    fig, waveform_plot = plot.subplots()                                                        #instantiate empty plot
    waveform_plot.plot(array[0], array[1])                                                      #populate plot from array
    point_num = 0                                                                               #reset iteration index to 0
    while point_num < num_of_points:                                                            #print every array entry using while loop
        print((round(array[0][point_num], 6), round(array[1][point_num], 6)))                   #print statement for indexed array entry
        point_num += 1                                                                          #increment iteration index
    plot.show()                                                                                 #display waveform plot

if __name__ == '__main__':                                                                      #allow lv4 to run as a shell command
    if 4>= len(sys.argv) >= 2 and (sys.argv[1] == 'array_for' or sys.argv[1] == 'array_while'): #filter incorrect commandline arguments
        if len(sys.argv) == 4:                                                                  #handle case when all four arguments are provided 
            args = [int(sys.argv[2]), float(sys.argv[3])]                                       #populate array of arguments for later function call
        elif len(sys.argv) == 3:                                                                #handle case when only three arguments are provided 
            args = [int(sys.argv[2]), 1.0]                                                      #populate array of arguments for later function call
        elif len(sys.argv) == 2:                                                                #handle case when only two arguments are given
            args = [4, 1.0]                                                                     #populate array of arguments for later function call
        if sys.argv[1] == 'array_for':                                                          #handle case when array_for is passed as argument
            array_for(args[0], args[1])                                                         #call array_for with specified arguments
        else:                                                                                   #handle case when array_while is passed as argument
            array_while(args[0], args[1])                                                       #call array_for with specified arguments
    else:                                                                                       #handle case when incorrect arguments are passed
        print('usage: lv4[array_for[points][amplitude]][array_while[points][amplitude]]')       #display help menu for array_for and array_while
        
