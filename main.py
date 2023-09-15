from pyo import *
from aifunctions import generateEffect, convert_audio_to_text

from fxchain import fxChain
import ast
from presets import presets

import sys, tty, termios

from eink_menu import makeText

import subprocess
import time


def getGPTeffect(q):
    sel_dict_string = generateEffect(q)
    sel_dict = ast.literal_eval(sel_dict_string)
    print(sel_dict)
    startServer(sel_dict)


def getPresetEffect(p):
    sel_dict = p
    print(sel_dict)
    startServer(sel_dict)

def startServer(sel_dict):
    s = Server()
    devices = pa_get_output_devices()
    device_names = devices[0]
    device_indices = devices[1]
    output_device_index = None
    for i, name in enumerate(device_names):
        if "Scarlett 2i2 USB" in name:
            output_device_index = device_indices[i]
            break
    if output_device_index is not None:
        s.setOutputDevice(output_device_index)
    else:
        print("Scarlett 2i2 USB device not found.")
        return
    s.boot()
    s.start()
    startFxChain(sel_dict, s)


# def startServer(sel_dict):
#     s = Server()
#     s.setOutputDevice(2) #pa_list_devices()
#     s.boot()
#     s.start()
#     startFxChain(sel_dict, s)


def startFxChain(sel_dict, server):
    input = Input()
    output = fxChain(
        input,
        sel_dict,
    )

    stereo = output.mix(2).out()

    server.gui(locals())

def read_ch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == "__main__":

    done = makeText("1 - Steroverb", "2 - Chorus", "g - GPT", "x - Exit")
    print(done)
  
    filedescriptors = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    x = 0
    while 1:    
        x=sys.stdin.read(1)[0]
        print("You pressed", x)
        if x == "1":
            p = presets.STEEREOVERB
            getPresetEffect(p)
        if x == "2":
            p = presets.CHORUS
            getPresetEffect(p)
        if x == "g":
            # USB PnP Sound Device TODO: always use the same mic
            print("recording")
            record = 'arecord -d 4 my_audio.wav'
            p = subprocess.Popen(record, shell=True)
            time.sleep(5)
            p.kill()
            print("done recording")
            audio_input = open("my_audio.wav", "rb")
            q = convert_audio_to_text(audio_input)
            print(q)
            getGPTeffect(q)
        if x == "x":
            print("make exit command")
            raise KeyboardInterrupt
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)

  