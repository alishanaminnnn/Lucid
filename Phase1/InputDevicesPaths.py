import evdev

# evdev.list_devices(); #it gives us the path of every input devices;
# evdev.InputDevice takes a path of input devices it give us the info of the input device of the specfic device


for path in evdev.list_devices():#goes through every path of input devices
    device=evdev.InputDevice(path)#path and name are stored in device
    print(f"Path:{path}, Name: {device.name}\n")#prints all the devices names and their paths


# the keyboard path is : /dev/input/event3/dev/input/event3/dev/input/event3