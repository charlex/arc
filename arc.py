from math import pi

class ArcException(Exception):
    pass

def arc_length(theta, radius=False, circumference=False):
    # Either radius and circumference need to be passed in
    if not radius and not circumference:
        raise ArcException("No radius or circumference passed in.")

    # If both radius and circumference are passed in and don't match each
    # other, then raise an error
    if (radius and circumference) and (radius != circumference / 2):
        raise ArcException("Both radius and circumference are passed in \
and do not match each other.")

    # Calculate radius based on circumference if no radius provided
    if not radius:
        radius = circumference / 2

    # Convert to floats
    theta = float(theta) # degree of arc
    radius = float(radius) # radius of circle

    # Do the math
    return (theta / 360) * (2 * pi * radius)
