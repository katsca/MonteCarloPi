import numpy as np
import sys
from matplotlib import pyplot as plt
import argparse


#Parse command line arguments

#Check for pause time to be a positive float
def positive_float(value):
    try:
        f = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid float")
    if f <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be positive")
    return f

#Check for number of points to be plotted to be a positive int
def positive_int(value):
    try:
        i = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid int")
    if i <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be positive")
    return i

#Set the arguments
parser = argparse.ArgumentParser(description="Monte Carlo visualisation of finding Pi")
parser.add_argument("--pause", type=positive_float, default=0.001,
                    help="Pause time between points in seconds (default: 0.001)")
parser.add_argument("--num_points", type=positive_int, default=10000,
                    help="Number of points to add (default: 10000)")

args = parser.parse_args()

#Number of points going to generate
pause_time = args.pause
n = args.num_points

#Close the window when exited for loop
def on_close(event):
    global window_closed
    window_closed = True
    print("Window closed!")
    sys.exit(0)  # immediately exit program

#Check if window closed
window_closed = False

#Compare to the actual value of Pi to find error
PI = np.pi

#Circle features
radius = 1 # radius of the circle
centre = (0,0) #Define centre

#List of randomly generated x points
ls_x  = []
#List of randomly generated y points
ls_y = []
#Number of points in the circle
n_circle = 0
#Number of points in the square
n_square = 0




#Define the axis and figure
fig, ax = plt.subplots(figsize=(6,6))
fig.canvas.mpl_connect('close_event', on_close)  # attach close event
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-radius, radius)
ax.set_ylim(-radius, radius)

#Define the number of points to plot on circle outer
theta = np.linspace(0,2*PI, 500)
circle_x = np.cos(theta) * radius + centre[0]
circle_y = np.sin(theta) * radius + centre[1]

#Plot the circle
circle_line = ax.plot(circle_x, circle_y, 'k-', label="Circle")


points_in_circle = ax.scatter([], [], color='red', label="Points in Circle")
points_out_circle = ax.scatter([], [], color="blue", label="Points out of Circle")

text_display = ax.text(-radius, radius+0.05, "Current PI: .. \nError ..\nNumber of points: ..", fontsize=12, color="green")
ax.legend( loc="upper right")
plt.ion()
plt.show()


for _ in range(n):
    #Need to generate the random points
    #Choose a probability distribution - in this case we use uniform
    x = np.random.uniform(-radius, radius)
    y = np.random.uniform(-radius,radius)
    #Append to the list
    ls_x.append(x)
    ls_y.append(y)
    

#Next need to find the number of points in the circle and the number of points out of the circle
for x, y in zip(ls_x, ls_y):
    if window_closed:
        break  # stop loop if window was closed
    
    distance_sq = (x - centre[0])**2 + (y-centre[1])**2 # find distance squared from origin
    
    if distance_sq <= radius**2: #Point is in the circle
        
        #Returns as [[x1, y1], [x2, y2] ..] so use transpose .T to switch into two arrays for x and y - if no points yet just set to empty list
        old_x_in, old_y_in = points_in_circle.get_offsets().T if points_in_circle.get_offsets().size else ([], [])
        
        #Create two arrays for x and y that contain the old and new points
        x = np.append(old_x_in, x)
        y = np.append(old_y_in, y)
        
        #Update the scatter axis for the points in circle
        points_in_circle.set_offsets(np.c_[x, y])# stacks the x and y arrays into column wise 2D array
        
         #Update the number of points within the circle
        n_circle += 1
        
    else:
        #Returns as [[x1, y1], [x2, y2] ..] so use transpose .T to switch into two arrays for x and y - if no points yet just set to empty list
        old_x_out, old_y_out = points_out_circle.get_offsets().T if points_out_circle.get_offsets().size else ([], [])
        
        
        #Create two arrays for x and y that contain the old and new points
        x = np.append(old_x_out, x)
        y = np.append(old_y_out, y) 
        
        #Update the scatter axis for the points out circle
        points_out_circle.set_offsets(np.c_[x, y]) # stacks the x and y arrays into column wise 2D array
    
    #Update the number of points within the square
    n_square += 1
    
    pi_approx = n_circle / n_square * 4
    pi_error = abs(pi_approx - PI) / PI * 100
    text_display.set_text(f"Current Pi: {pi_approx:.2f}\nError: {pi_error:.2f}%\nNumber of points: {n_square}")
    
    #Update the plot
    plt.draw()
    plt.pause(pause_time) # short delay for visual updates
        

plt.ioff()
plt.show() 
