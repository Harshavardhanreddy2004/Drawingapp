# OpenCV Drawing App

A simple interactive drawing application built with Python and OpenCV.  
Draw shapes like circles, rectangles, lines, or freehand sketches on a white canvas with adjustable colors and thickness.

---

## Features

- Draw **Circles**, **Rectangles**, **Lines**, and **Freehand** drawings
- Change drawing **mode** with keyboard shortcuts
- Cycle through colors: **Blue**, **Green**, **Red**
- Adjust the **thickness** of shapes and lines
- Save your drawing as an image file
- Simple mouse controls for drawing

---

## How to Use

1. Run the script:
   ```bash
   python drawing_app.py
Left-click and drag on the window to draw shapes depending on the selected mode.

Keyboard Controls:

Press m to switch between modes: Circle → Rectangle → Line → Freehand

Press c to cycle through colors: Blue → Green → Red

Press + to increase the thickness of lines/shapes

Press - to decrease the thickness (minimum thickness is 1)

Press s to save the current drawing as myimage.png

Press q to quit the app

Dependencies
Python 3.x

OpenCV (opencv-python)

NumPy
