import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import ttk
from geometry import project_point, rotate_x, rotate_y, rotate

# Read the face vertices and indices
with open("face-vertices.data", "r") as f:
    vertices = [list(map(float, line.strip().split(","))) for line in f]

with open("face-index.txt", "r") as f:
    indices = [list(map(int, line.strip().split(","))) for line in f if line.strip()]

def plot_object(vertices):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for index_pair in indices:
        p1 = vertices[index_pair[0]]
        p2 = vertices[index_pair[1]]
        xs = [p1[0], p2[0]]
        ys = [p1[1], p2[1]]
        zs = [p1[2], p2[2]]
        ax.plot(xs, ys, zs, color="b")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    plt.show(block=False)

def update_plot(event):
    angle_x = x_slider.get()
    angle_y = y_slider.get()
    rotated_vertices = rotate(vertices, angle_x, angle_y)
    plt.clf()
    plot_object(rotated_vertices)

root = tk.Tk()
root.title("Rotation Controller")

x_slider = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, label="Rotate X-axis")
x_slider.pack(fill=tk.X, padx=10, pady=10)
x_slider.bind("<Motion>", update_plot)

y_slider = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, label="Rotate Y-axis")
y_slider.pack(fill=tk.X, padx=10, pady=10)
y_slider.bind("<Motion>", update_plot)

exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

plot_object(vertices)  # Initial plot
root.mainloop()
