import matplotlib.pyplot as plt
# line 1 points
x1 = [0,0.25,0.5,1,1.5,2]
y1 = [0,2.03,2.28,2.53,2.78,3.03]
# plotting the line 1 points
plt.plot(x1, y1, label = "Intensity 5 w/m^2")

# line 2 points
x2 = [0,0.25,0.5,1,1.5,2]
y2 = [0,6.10,6.85,7.60,8.35,9.10]
# plotting the line 2 points
plt.plot(x2, y2, label = "Intensity 15 w/m^2")

# line 2 points
x3 = [0,0.25,0.5,1,1.5,2]
y3 = [0,8.13,9.13,10.13,11.13,12.13]
# plotting the line 2 points
plt.plot(x3, y3, label = "Intensity 20 w/m^2")

# naming the x axis
plt.xlabel('Voltage')
# naming the y axis
plt.ylabel('Current')
# giving a title to my graph
plt.title('Constant frequency and different intensities')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
