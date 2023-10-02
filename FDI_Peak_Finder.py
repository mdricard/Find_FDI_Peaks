import numpy as np
import matplotlib.pyplot as plt


peak_force = np.zeros(5)
peak_force_location = []
force = np.zeros(6000)
fdi = np.zeros(6000)
fn = 'd:/fdi_burst.csv'
data = np.genfromtxt(fn, delimiter=',', skip_header=1)
force = data[:, 0]
fdi = abs(data[:, 1])


def threshold_crossing(curve, threshold):
    """
    search array for all instances crossing the threshold
    Warning -- this function begins searching for the first rising point.
    :param threshold: value to search for in input array curve[]
    :param curve:
    :return: point_locations[] is a list of matching pairs (rising, falling) about
    threshold in the array curve[]. An even number of matching pairs is returned.

    """
    point_locations = []
    i = 0
    while i < (len(curve)-2):
        while curve[i] < 10 and i < (len(curve)-2):
            i += 1
        if curve[i] >= 10:
            point_locations.append(i)                   # found rising point
        while curve[i] > 10 and i < (len(curve)-2):
            i += 1
        if curve[i] <= 10:
            point_locations.append(i)                   # found falling point
    if len(point_locations) % 2 != 0:
        point_locations = point_locations[:-1]          # slice off the odd point at the end
    return point_locations


def get_peak(curve, first_pt, last_pt):
    """
    get_peak searches array curve[] between first_pt and last_pt to find the first peak.
    If there are more than 1 peak value only the first is returned.
    :param curve: array to search for peak
    :param first_pt: index of first point in curve[] to start searching
    :param last_pt: index of last point in curve[] to search
    :return: max_pt is the index of the first peak in the interval curve[first_pt] to curve[last_pt]
    """
    max_value = curve[first_pt]
    for i in range(first_pt  + 1, last_pt):
        if curve[i] > max_value:
            max_value = curve[i]
            max_pt = i
    return max_pt


force_pts = threshold_crossing(force, 10.0)
j = 0
for i in range(0, len(force_pts), 2):
    peak_force_location.append(get_peak(force, force_pts[i], force_pts[i+1]))
    peak_force[j] = force[peak_force_location[j]]
    j += 1

plt.plot(force)
for i in range(len(peak_force)):
    plt.scatter(peak_force_location[i], peak_force[i])
plt.show()



