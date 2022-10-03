@staticmethod
def dist_to_origin(point):
    # calculate Euclidean distance; agnostic towards vector length
    return np.sqrt((np.asarray(point) ** 2).sum(axis=0))
