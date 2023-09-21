import tkinter as tk


def reverb():
    print("Reverb function invoked")


def chorus():
    print("Chorus function invoked")


def gpt():
    print("GPT function invoked")


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