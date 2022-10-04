# vector length, 2D or 3D 
def dist_to_origin(point):
    # calculate Euclidean distance; agnostic towards vector length
    return np.sqrt((np.asarray(point) ** 2).sum(axis=0))

# get simple timestamp 
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")
