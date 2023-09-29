import tkinter as tk
from main import *

def reverb():
    p = presets.STEEREOVERB
    pedal = subprocess.Popen(['python', '-c', f"from main import getPresetEffect; getPresetEffect({p})"])
    pedal.wait()

   

def chorus():
    p = presets.CHORUS
    pedal = subprocess.Popen(['python', '-c', f"from main import getPresetEffect; getPresetEffect({p})"])
    pedal.wait()


def gpt():
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
    pedal = subprocess.Popen(['python', '-c', f"from main import getGPTeffect; getGPTeffect('{q}')"])
    pedal.wait()

def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Andi's GPT Pedal")

root.geometry("400x200")

reverb_button = tk.Button(root, text="Reverb", command=reverb, width=20)
reverb_button.pack(pady=10)

chorus_button = tk.Button(root, text="Chorus", command=chorus, width=20)
chorus_button.pack(pady=10)

gpt_button = tk.Button(root, text="GPT", command=gpt, width=20)
gpt_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app, width=20)
exit_button.pack(pady=10)

root.mainloop()
 