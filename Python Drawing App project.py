#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


drawing = False
mode = "circle"
start_x, start_y = -1, -1
color = (255, 0, 0) 
thickness = 2


# In[3]:


def draw(event, x, y, flags, param):
    global drawing, start_x, start_y, img, mode, color, thickness
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and mode == "Freehand":
            cv2.line(img, (start_x, start_y), (x, y), color, thickness)
            start_x, start_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == "circle":
            radius = int(((x - start_x) ** 2 + (y - start_y) ** 2) ** 0.5)
            cv2.circle(img, (start_x, start_y), radius, color, thickness)
        elif mode == "rectangle":
            cv2.rectangle(img, (start_x, start_y), (x, y), color, thickness)
        elif mode == "line":
            cv2.line(img, (start_x, start_y), (x, y), color, thickness)
            
        


# In[4]:


print("Manual of the App:")
print("1. Left click to start drawing")
print("2. Press 'm' to change mode: Circle, Rectangle, Line, Freehand")
print("3. Press 'c' to change the color: Red, Green, Blue")
print("4. Press '+' or '-' for increasing or decreasing the thickness")
print("5. Press 's' to save")
print("6. Press 'q' to quit")
img = np.ones((600, 800, 3), dtype=np.uint8) * 255
cv2.namedWindow("my drawing app")
cv2.setMouseCallback("my drawing app", draw)
while True:
    cv2.imshow("my drawing app", img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  
        break
    elif key == ord('m'):  
        modes = ["circle", "rectangle", "line", "Freehand"]
        mode = modes[(modes.index(mode) + 1) % len(modes)]
        print(f"Mode Changed to: {mode}")
    elif key == ord('c'): 
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  
        current_index = colors.index(color) if color in colors else 0
        color = colors[(current_index + 1) % len(colors)]
        print(f"Color changed to: {'Blue' if color == (255, 0, 0) else 'Green' if color == (0, 255, 0) else 'Red'}")
    elif key == ord('+'):  
        thickness += 1
        print(f"Thickness increased to: {thickness}")
    elif key == ord('-'): 
        if thickness > 1:
            thickness -= 1
            print(f"Thickness decreased to: {thickness}")
    elif key == ord('s'):  
        cv2.imwrite("myimage.png", img)
        print("Drawing saved as 'myimage.png'.")

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




