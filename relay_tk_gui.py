#!/usr/bin/python3
"""
A simple GUI to control a relay board with four channels.
"""

import tkinter as tk
from tkinter import messagebox
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
outPin1 = 19  # WiringPi 24
outPin2 = 26  # WiringPi 25
outPin3 = 20  # WiringPi 28
outPin4 = 21  # WiringPi 29

# GPIO.setmode(GPIO.BOARD)
# outPin1 = 35
# outPin2 = 37
# outPin3 = 38
# outPin4 = 40


GPIO.setup(outPin1, GPIO.OUT)
GPIO.output(outPin1, True)

GPIO.setup(outPin2, GPIO.OUT)
GPIO.output(outPin2, True)

GPIO.setup(outPin3, GPIO.OUT)
GPIO.output(outPin3, True)

GPIO.setup(outPin4, GPIO.OUT)
GPIO.output(outPin4, True)


def relayOn():
    GPIO.output(outPin1, False)
    print("Relay On")

def relayOff():
    GPIO.output(outPin1, True)
    print("Relay Off")

def relayToggle1():
    if GPIO.input(outPin1):
        GPIO.output(outPin1, False)
        print("Relay Off")
        toggleButton1['text'] = "Relay CH1 ON"
        toggleButton1['bg'] = 'green'
    else:
        MsgBox = messagebox.askquestion(
                                'Power OFF',
                                'Are you sure you want to Power OFF',
                                icon = 'warning')
        if MsgBox == 'yes':
            GPIO.output(outPin1, True)
            print("Relay On")
            toggleButton1['text'] = "Relay CH1 OFF"
            toggleButton1['bg'] = 'red'
        else:
            pass

def relayToggle2():
    if GPIO.input(outPin2):
        GPIO.output(outPin2, False)
        print("Relay2 Off")
        toggleButton2['text'] = "Relay CH2 ON"
        toggleButton2['bg'] = 'green'
    else:
        MsgBox = messagebox.askquestion(
                                'Power OFF',
                                'Are you sure you want to Power OFF',
                                icon = 'warning')
        if MsgBox == 'yes':
            GPIO.output(outPin2, True)
            print("Relay2 On")
            toggleButton2['text'] = "Relay CH2 OFF"
            toggleButton2['bg'] = 'red'
        else:
            pass

def relayToggle3():
    if GPIO.input(outPin3):
        GPIO.output(outPin3, False)
        print("Relay3 Off")
        toggleButton3['text'] = "Relay CH3 ON"
        toggleButton3['bg'] = 'green'
    else:
        MsgBox = messagebox.askquestion(
                                'Power OFF',
                                'Are you sure you want to Power OFF',
                                icon = 'warning')
        if MsgBox == 'yes':
            GPIO.output(outPin3, True)
            print("Relay3 On")
            toggleButton3['text'] = "Relay CH3 OFF"
            toggleButton3['bg'] = 'red'
        else:
            pass

def relayToggle4():
    if GPIO.input(outPin4):
        GPIO.output(outPin4, False)
        print("Relay4 Off")
        toggleButton4['text'] = "Relay CH4 ON"
        toggleButton4['bg'] = 'green'
    else:
        MsgBox = messagebox.askquestion(
                                'Power OFF',
                                'Are you sure you want to Power OFF',
                                icon = 'warning')
        if MsgBox == 'yes':
            GPIO.output(outPin4, True)
            print("Relay4 On")
            toggleButton4['text'] = "Relay CH4 OFF"
            toggleButton4['bg'] = 'red'
        else:
            pass


def close():
    MsgBox = messagebox.askquestion(
                        'Exit Application',
                        'Are you sure you want to exit the application',
                        icon = 'warning')
    if MsgBox == 'yes':
        GPIO.cleanup()
        print("GPIO cleared")
        root.destroy()
    else:
        messagebox.showinfo(
                        'Return',
                        'You will now return to the application screen')



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Relay Control")

    # onButton = tk.Button(root, text="Relay CH1 ON",
    #                       width=10, bg='green', command=relayOn)
    # onButton.pack()
    # 
    # offButton = tk.Button(root, text="Relay CH1 OFF",
    #                       width=10, bg='red', command=relayOff)
    # offButton.pack()

    toggleButton1 = tk.Button(root, text="Relay CH1 OFF",
                              width=30, height=4,
                              bg='red', command=relayToggle1)
    toggleButton1.pack()

    toggleButton2 = tk.Button(root, text="Relay CH2 OFF",
                              width=30, height=4,
                              bg='red', command=relayToggle2)
    toggleButton2.pack()

    toggleButton3 = tk.Button(root, text="Relay CH3 OFF",
                              width=30, height=4,
                              bg='red', command=relayToggle3)
    toggleButton3.pack()

    toggleButton4 = tk.Button(root, text="Relay CH4 OFF",
                              width=30, height=4,
                              bg='red', command=relayToggle4)
    toggleButton4.pack()

    exitButton = tk.Button(root, text='Exit',
                           command=close, height=2, width=30)
    exitButton.pack()

    # cleanup GPIO when user closes window
    root.protocol("WM_DELETE_WINDOW", close)

    root.mainloop()
    print("Window closed\nCleaning GPIO")



