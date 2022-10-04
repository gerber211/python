# vector length, 2D or 3D 
def dist_to_origin(point):
    # calculate Euclidean distance; agnostic towards vector length
    return np.sqrt((np.asarray(point) ** 2).sum(axis=0))

# get simple timestamp 
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")

# Calculate difference between neighboring xyz points
dd = np.diff(traj_xyzs[0:3, :], axis=1)
# Euclidean distances between each
segdists = np.sqrt((dd ** 2).sum(axis=0))

# Make axes of 3D plot to have equal scales... matplotlib's methods don't work
def set_axes_equal_3d(ax):
    limits = np.asarray([ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()])
    spans = abs(limits[:, 0] - limits[:, 1])
    centers = np.mean(limits, axis=1)
    radius = 0.5 * max(spans)
    ax.set_xlim3d([centers[0]-radius, centers[0]+radius])
    ax.set_ylim3d([centers[1]-radius, centers[1]+radius])
    ax.set_zlim3d([centers[2]-radius, centers[2]+radius])

