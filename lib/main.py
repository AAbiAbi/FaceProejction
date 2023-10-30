import tkinter as tk
from tkinter import Canvas, Button
from math import sin, cos, radians

# Read the data files
with open("face-vertices.data", "r") as f:
    vertices = [list(map(float, line.strip().split(","))) for line in f]

with open("face-index.txt", "r") as f:
    triangles = [[int(index) - 1 for index in filter(None, line.strip().split(","))] for line in f]

zoom_factor = 1
current_mode = "points"

def project_point(x, y, z, d=5, width=800, height=600, zoom=1):
    x_proj, y_proj = (d * x / (z + d), d * y / (z + d))
    x_proj *= zoom
    y_proj *= zoom
    x_proj += width / 2
    y_proj += height / 2
    return (x_proj, y_proj)

def display(mode="points"):
    global current_mode
    current_mode = mode
    canvas.delete("all")
    projected_points = [project_point(*vertex, zoom=zoom_factor) for vertex in vertices]

    if mode == "points":
        for x, y in projected_points:
            canvas.create_oval(x-2, y-2, x+2, y+2, fill="white")
    elif mode == "wireframe":
        for triangle in triangles:
            for i in range(len(triangle)):
                if triangle[i] < len(projected_points):
                    x1, y1 = projected_points[triangle[i]]
                    x2, y2 = projected_points[triangle[(i + 1) % len(triangle)]]
                    canvas.create_line(x1, y1, x2, y2, fill="white")

def zoom_in():
    global zoom_factor
    zoom_factor += 0.1
    display(current_mode)

def zoom_out():
    global zoom_factor
    zoom_factor -= 0.1
    display(current_mode)

root = tk.Tk()
root.title("3D Face Projection")

canvas = Canvas(root, width=800, height=600, bg="black")
canvas.pack(pady=20)

button_frame = tk.Frame(root, bg="red")  # Temporarily set a red background to see the frame.

button_frame.pack(pady=20)

btn_display_points = Button(button_frame, text="Display Points", command=lambda: display("points"))


btn_display_wireframe = Button(button_frame, text="Display Wireframe", command=lambda: display("wireframe"))


btn_zoom_in = Button(button_frame, text="Zoom In", command=zoom_in)


btn_zoom_out = Button(button_frame, text="Zoom Out", command=zoom_out)

btn_display_points.grid(row=0, column=0, padx=5, pady=5)
btn_display_wireframe.grid(row=0, column=1, padx=5, pady=5)
btn_zoom_in.grid(row=0, column=2, padx=5, pady=5)
btn_zoom_out.grid(row=0, column=3, padx=5, pady=5)


root.mainloop()