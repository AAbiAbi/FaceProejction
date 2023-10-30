from PIL import Image, ImageDraw
from geometry import project_point

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

    return img
