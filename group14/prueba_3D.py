# from mpl_toolkits import mplot3d
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = plt.axes(projection="3d")
#
# z_line = np.linspace(0, 15, 1000)
# x_line = np.cos(z_line)
# y_line = np.sin(z_line)
# ax.plot3D(x_line, y_line, z_line, 'gray')
#
# z_points = 15 * np.random.random(100)
# x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
# y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
# ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv')
#
# plt.show()


# %matplotlib notebook
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from benchmarks import functions as fun

fig = plt.figure()
ax = fig.gca(projection='3d')

# x_points = 10 * np.random.random(100)
# y_points = 10 * np.random.random(100)
# z_points = np.sqrt(x_points ** 2 + y_points ** 2)
# ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap=cm.coolwarm, alpha=1)

# Make data.
X = np.arange(0, 40, 0.25)
Y = np.arange(0, 40, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = R

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.8,
                       linewidth=0, antialiased=False)

# theCM = cm.get_cmap()
# theCM._init()
# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=theCM)


# Customize the z axis.

# ax.set_zlim(0, 55)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_zlabel('z label')

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d.axes3d as p3
# import matplotlib.animation as animation
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# def Gen_RandLine(length, dims=2):
#     """
#     Create a line using a random walk algorithm
#
#     length is the number of points for the line.
#     dims is the number of dimensions the line has.
#     """
#     lineData = np.empty((dims, length))
#     lineData[:, 0] = np.random.rand(dims)
#     for index in range(1, length):
#         # scaling the random numbers by 0.1 so
#         # movement is small compared to position.
#         # subtraction by 0.5 is to change the range to [-0.5, 0.5]
#         # to allow a line to move backwards.
#         step = ((np.random.rand(dims) - 0.5) * 0.1)
#         lineData[:, index] = lineData[:, index - 1] + step
#
#     return lineData
#
#
# def update_lines(num, dataLines, lines):
#     for line, data in zip(lines, dataLines):
#         # NOTE: there is no .set_data() for 3 dim data...
#         line.set_data(data[0:2, :num])
#         line.set_3d_properties(data[2, :num])
#     return lines
#
# # Attaching 3D axis to the figure
# fig = plt.figure()
# ax = p3.Axes3D(fig)
#
# # Fifty lines of random 3-D lines
# data = [Gen_RandLine(25, 3) for index in range(50)]
#
# # Creating fifty line objects.
# # NOTE: Can't pass empty arrays into 3d version of plot()
# lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
#
# # Setting the axes properties
# ax.set_xlim3d([0.0, 1.0])
# ax.set_xlabel('X')
#
# ax.set_ylim3d([0.0, 1.0])
# ax.set_ylabel('Y')
#
# ax.set_zlim3d([0.0, 1.0])
# ax.set_zlabel('Z')
#
# ax.set_title('3D Test')
#
# # Creating the Animation object
# line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
#                                    interval=50, blit=False)
#
# plt.show()
