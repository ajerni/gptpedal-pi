from pyo import *
from pyo import pa_get_output_devices, pa_get_input_devices

from aifunctions import generateEffect, convert_audio_to_text

from fxchain import fxChain
import ast
from presets import presets

import subprocess
import time

import dweepy

s = Server()


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

    global s
    
    output_devices = pa_get_output_devices() # i.e. (['vc4-hdmi-1: MAI PCM i2s-hifi-0 (hw:2,0)', 'Scarlett 2i2 USB: Audio (hw:3,0)', 'pulse', 'default'], [1, 2, 3, 4])
    print(output_devices)
    soundcard = extract_scarlett_index(output_devices)
    print(soundcard)
    s.setOutputDevice(soundcard) #pa_list_devices() / pa_get_output_devices()/ 0 or 1 or 2 = Scarlett 2i2 USB
    #s.setOutputDevice(2) 
    s.boot()
    s.start()
    
    startFxChain(sel_dict, s)


def startFxChain(sel_dict, server):
    input = Input()
    output = fxChain(
        input,
        sel_dict,
    )

    stereo = output.mix(2).out()

    server.gui(locals())

def get_usb_pnp_device(devices): # extracts "hw:x,y" for 'USB PnP Sound Device'
    for device in devices[0]:
        if 'USB PnP Sound Device' in device:
            return device.split('(')[-1].split(')')[0].strip()
    return None

def extract_scarlett_index(t):
    for i, element in enumerate(t[0]):
        if "Scarlett" in element:
            return t[1][i]
    return None

if __name__ == "__main__":

    while True:

        # https://dweet.io/dweet/for/aeraspipedal?text=verb
        for dweet in dweepy.listen_for_dweets_from("aeraspipedal"):
            print(dweet)
            if dweet["content"]["text"]=="verb":
                p = presets.DOPPELVERB
                getPresetEffect(p)
            if dweet["content"]["text"]=="shiny":
                p = presets.SHINY
                getPresetEffect(p)
            if dweet["content"]["text"]=="gpt":
                input_devices = pa_get_input_devices()
                usb_mic = get_usb_pnp_device(input_devices)
                record = f'arecord -D {usb_mic} -d 4 -f S16_LE -r 44100 my_audio.wav'
                p = subprocess.Popen(record, shell=True)
                time.sleep(5)
                p.kill()
                print("done recording")
                audio_input = open("my_audio.wav", "rb")
                q = convert_audio_to_text(audio_input)
                print(q)
                getGPTeffect(q)
