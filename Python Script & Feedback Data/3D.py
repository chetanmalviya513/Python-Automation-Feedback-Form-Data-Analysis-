import numpy as np

# Prepare data for 3D bar graph
categories = faculty_name
values = fac_tot_rat

fig = plt.figure(figsize=(18, 29))
ax = fig.add_subplot(111, projection='3d')

# Position of bars on x-axis
xpos = np.arange(len(categories))
ypos = np.zeros(len(categories))  # y positions are all zero for a 2D bar graph
zpos = np.zeros(len(categories))

# The width and depth of the bars
dx = np.ones(len(categories)) * 0.8  # Width of the bars
dy = np.ones(len(categories))  # Depth of the bars
dz = values

# Plot bars
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='blue', edgecolor='black')

# Labeling the x-axis
ax.set_xticks(xpos)
ax.set_xticklabels(categories)

# Labeling axes
#ax.set_xlabel('Category')
#ax.set_ylabel('Y')
ax.set_zlabel('Percentage')

# Rotate x-axis labels
plt.xticks(rotation=90)

# Rotate x-axis labels
for label in ax.get_xticklabels():
    label.set_rotation(90)



#Title set
#ax.set_title("12. How would you rate the overall programme ", fontsize= 15)

# Remove y-ticks
ax.set_yticks([])
#ax.set_zticks([])



#ax.set_zlim([4, 5])

# Set the viewing angle to 89 degrees
ax.view_init(elev=2., azim=89)

# Add value labels on top of bars
#for i in range(len(categories)):
#    ax.text(xpos[i], ypos[i], dz[i], f'{dz[i]}%', ha='right', va='bottom', fontsize=11)

# Show the graph
plt.show()