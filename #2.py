import matplotlib.pyplot as plt
# line 1 points
x1 = [0,0.25,0.5,1,1.5,2]
y1 = [0,4.07,4.57,5.07,5.57,6.07]
# plotting the line 1 points
plt.plot(x1, y1, label = "Intensity 100nm")

# line 2 points
x2 = [0,0.25,0.5,1,1.5,2]
y2 = [0,1.83,2.33,2.83,3.33,3.83]
# plotting the line 2 points
plt.plot(x2, y2, label = "Intensity 122nm")

# line 2 points
x3 = [0,0.25,0.5,1,1.5,2]
y3 = [0,0.52,1.02,1.52,2.02,2.52]
# plotting the line 2 points
plt.plot(x3, y3, label = "Intensity 140nm")

# naming the x axis
plt.xlabel('Voltage')
# naming the y axis
plt.ylabel('Current')
# giving a title to my graph
plt.title('Constant intensity and different wavelength')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
