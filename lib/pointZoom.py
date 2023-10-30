from PIL import Image, ImageDraw

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

def display_points(vertices, zoom=1):
    """
    Display the 2D projected points for a list of 3D vertices.

    Parameters:
    - vertices: List of 3D coordinates
    - zoom: zoom factor

    Returns:
    - List of 2D projected points
    """
    projected_points = [project_point(*vertex, zoom=zoom) for vertex in vertices]
    for x, y in projected_points:
        print(f"({x:.2f}, {y:.2f})")


def display_on_image(vertices, indices, mode='points', zoom=1, width=800, height=600, point_size=5):
    img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)

    projected_points = [project_point(*vertex, zoom=zoom, width=width, height=height) for vertex in vertices]
    
    if mode == 'points':
        for x, y in projected_points:
            draw.ellipse([(x-point_size, y-point_size), (x+point_size, y+point_size)], fill="white")
    elif mode == 'wireframe':
        for triangle in indices:
            p1 = projected_points[triangle[0]]
            p2 = projected_points[triangle[1]]
            p3 = projected_points[triangle[2]]
            draw.line([p1, p2, p3, p1], fill="white")

    img.show()

# Example Usage
with open("face-vertices.data", "r") as f:
    vertices = [list(map(float, line.strip().split(","))) for line in f]

with open("face-index.txt", "r") as f:
    indices = [list(map(int, line.strip().split(","))) for line in f if line.strip()]

# Display points
display_on_image(vertices, indices, mode='points', zoom=15)

# Display wireframe
display_on_image(vertices, indices, mode='wireframe', zoom=15)