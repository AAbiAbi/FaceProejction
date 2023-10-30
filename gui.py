from PIL import Image, ImageDraw, ImageTk

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import ttk
from geometry import project_point, rotate_x, rotate_y, rotate
# Import our own modules
from geometry import project_point, rotate_x, rotate_y, rotate
from render import display_on_image


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




# Example Usage
with open("face-vertices.data", "r") as f:
    vertices = [list(map(float, line.strip().split(","))) for line in f]

with open("face-index.txt", "r") as f:
    indices = [list(map(int, line.strip().split(","))) for line in f if line.strip()]

# # Display points
# display_on_image(vertices, indices, mode='points', zoom=15)

# # Display wireframe
# display_on_image(vertices, indices, mode='wireframe', zoom=15)
def select_mode():
    mode = mode_var.get()
    display_on_image(vertices, indices, mode=mode, zoom=15)

def show_points_mode():
    img = display_on_image(vertices, indices, mode='points', zoom=150)
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo

def show_wireframe_mode():
    img = display_on_image(vertices, indices, mode='wireframe', zoom=150)
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo


# Functions to display based on mode and zoom level
def show_points_mode():
    zoom_level = zoom_scale.get()
    img = display_on_image(vertices, indices, mode='points', zoom=zoom_level)
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo

def show_wireframe_mode():
    zoom_level = zoom_scale.get()
    img = display_on_image(vertices, indices, mode='wireframe', zoom=zoom_level)
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo

def update_display():
    """Update display based on mode and zoom level."""
    mode = mode_var.get()
    zoom = zoom_scale.get()

    angle_x = x_rotation_scale.get()
    angle_y = y_rotation_scale.get()

    rotated_vertices = rotate(vertices, angle_x, angle_y)
    
    if mode == "points":
        img = display_on_image(rotated_vertices, indices, mode='points', zoom=zoom)
    else:
        img = display_on_image(rotated_vertices, indices, mode='wireframe', zoom=zoom)

    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo

# Create the main window
root = tk.Tk()
root.title("3D Object Display Mode Selector")
root.geometry('800x650')  # Width x Height, adjust as needed

mode_var = tk.StringVar(value="points")
zoom_var = tk.IntVar(value=150)  # or whatever default zoom level you'd like



# Create main frame
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Mode selector buttons
# Radiobuttons for mode selector
points_button = ttk.Radiobutton(frame, text="Points Mode", value="points", variable=mode_var)
wireframe_button = ttk.Radiobutton(frame, text="Wireframe Mode", value="wireframe", variable=mode_var)
submit_button = ttk.Button(frame, text="Submit", command=update_display)

points_button.pack(side=tk.LEFT, padx=5, pady=5)
wireframe_button.pack(side=tk.LEFT, padx=5, pady=5)
submit_button.pack(side=tk.LEFT, padx=5, pady=5)

# Scale for zoom control
zoom_scale = tk.Scale(frame, from_=5, to=2000, orient=tk.HORIZONTAL, label="Zoom Level", sliderlength=30)
zoom_scale.pack(fill=tk.X, expand=True, padx=5, pady=5)

# Add rotation scales in the GUI
x_rotation_scale = tk.Scale(frame, from_=-180, to=180, orient=tk.HORIZONTAL, label="Rotation X-axis", sliderlength=30)
x_rotation_scale.pack(fill=tk.X, expand=True, padx=5, pady=5)

y_rotation_scale = tk.Scale(frame, from_=-180, to=180, orient=tk.HORIZONTAL, label="Rotation Y-axis", sliderlength=30)
y_rotation_scale.pack(fill=tk.X, expand=True, padx=5, pady=5)


# Image display label with fixed size
img_frame = ttk.Frame(root, padding="10")
img_frame.pack(fill=tk.BOTH, expand=True)

img_label = ttk.Label(img_frame)
img_label.pack(fill=tk.BOTH, expand=True)

root.mainloop()