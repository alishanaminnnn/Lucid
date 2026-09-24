# Import everything from the tkinter module.
# Tkinter is a built-in Python library used to create GUI
# (Graphical User Interface) applications, such as windows,
# buttons, labels, text boxes, etc.
from tkinter import *


# Create the main application window.
# Tk() creates a new window where we can place GUI elements.
# We store this window in the variable first_root.
first_root = Tk()


# Set the initial size of the window.
# The format is "width x height".
# Width = 644 pixels
# Height = 434 pixels
first_root.geometry("644x434")


# Set the maximum size the user can resize the window to.
# The first value (733) is the maximum width in pixels.
# The second value (434) is the maximum height in pixels.
# The user cannot enlarge the window beyond these dimensions.
first_root.maxsize(733, 434)


# Create a Label widget.
# A Label is used to display text or an image in the window.
# text="my name is alishan" is the text that will appear.
# The label is stored in the variable alishan.
first_lable = Label(text="my name is alishan")


# Add the Label to the window using the pack() geometry manager.
# pack() places the widget inside the window.
# By default, it places the label near the top center.
first_lable.pack()


# Start the Tkinter event loop.
# This keeps the window open and allows it to respond to
# user actions, such as resizing, minimizing and closing.
# Without mainloop(), the window may appear and close immediately.
first_root.mainloop()