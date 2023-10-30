import math


def project_point(x, y, z, d=5, zoom=1, width=800, height=600):
    """
    Project a 3D point to 2D using perspective projection.
    
    Parameters:
    - x, y, z: 3D coordinates
    - d: distance between the viewer and the projection plane
    - zoom: zoom factor
    
    Returns:
    - x_proj, y_proj: 2D coordinates
    """
    x_proj, y_proj = (d * x / (z + d), d * y / (z + d))
    x_proj *= zoom
    y_proj *= zoom
     # Adjust for centering
    x_proj += width / 2
    y_proj += height / 2
    return (x_proj, y_proj)

def rotate_x(vertices, angle):
    """Rotate the points around the X axis."""
    """Rotate the points around the X axis."""
    angle_rad = math.radians(angle)
    matrix = [
        [1, 0, 0],
        [0, math.cos(angle_rad), -math.sin(angle_rad)],
        [0, math.sin(angle_rad), math.cos(angle_rad)]
    ]
    return [[sum(a*b for a,b in zip(vertex, row)) for row in zip(*matrix)] for vertex in vertices]


def rotate_y(vertices, angle):
    """Rotate the points around the Y axis."""
    angle_rad = math.radians(angle)
    matrix = [
        [math.cos(angle_rad), 0, math.sin(angle_rad)],
        [0, 1, 0],
        [-math.sin(angle_rad), 0, math.cos(angle_rad)]
    ]
    return [[sum(a*b for a,b in zip(vertex, row)) for row in zip(*matrix)] for vertex in vertices]


def rotate(vertices, angle_x, angle_y):
    """Rotate the points around both the X and Y axes."""
    vertices = rotate_x(vertices, angle_x)
    vertices = rotate_y(vertices, angle_y)
    return vertices
