import sys, tty, termios
import subprocess
from pyo import *
from eink_menu import makeText


if __name__ == "__main__":

    done = makeText("GPT Pedal", "m - Menu (GUI)", "s - Start (keys)", "x - Exit")
    print(done)

    def read_ch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    while True:
        ch = read_ch()
        if ch == 'x':
            break
        if ch == "s":
            pedal = subprocess.Popen(['python', 'main.py'])
            pedal.wait()
            done = makeText("GPT Pedal", "m - Menu (GUI)", "s - Start (keys)", "x - Exit")
            print(done)
        if ch == "m":
            pedal = subprocess.Popen(['python', 'menu.py'])
            pedal.wait()
            done = makeText("GPT Pedal", "m - Menu (GUI)", "s - Start (keys)", "x - Exit")
            print(done)
    
        print("key is: " + ch)