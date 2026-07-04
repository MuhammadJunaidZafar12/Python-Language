import matplotlib.pyplot as plt

# Plotting graph in python

# very basic plot - we want something better
# x = [1, 3, 5, 10] # This is what we are plotting
# plt.plot(x)
# plt.show() # This will show the plot we are plotting

# Plotting x and y against each other
# y = [7, 12, 21, 22]
# plt.plot(x, y)
# plt.show()

# Let us plot graph a bit complex

# Line 1 - points
x = [3, 9, 14]
y = [2, 7, 30]

plt.plot(x,y, c = "red", linewidth = 2, label= "Line 1")

# Line 2 - points
x2 = [1, 15, 18]
y2 = [0, 3, 12]

#Plotting x2 and y2 graph
plt.plot(x2, y2, color = "blue", linewidth = 0.5, label = "Line 2", linestyle = "dashed",
         marker = 'o', markerfacecolor = "red", markersize = 10)
# we can also change the marker style (circle to box)
# marker = 's'
# plt.show()

# Label the Axis and give the plot a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Compares Two Lines")

# Limit the axis
# plt.ylim(0, 10)
# plt.xlim(0, 30)

# Show the legend on the plot
plt.legend()

# Get python to show the plot
plt.show()




