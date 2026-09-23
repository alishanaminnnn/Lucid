import evdev
keyboard=0

for path in evdev.list_devices():#goes through every devices path
    device=evdev.InputDevice(path)
    if 'keyboard' in device.name:#if in the name of the devices if there is Keyboard
        keyboard=device.path#path of the keyboard is stored in it
print (keyboard)#prints the path

