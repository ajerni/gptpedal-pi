import sys, tty, termios
import subprocess
import threading
from eink_menu import makeText

if __name__ == "__main__":

    done = makeText("s - Start", "x - Exit", "", "")
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
            done = makeText("s - Start", "x - Exit", "", "back")
            print(done)
            # result = pedal.poll()
            # if result is not None:
            #     print('the other process has finished and retuned %s' % result)
        print("key is: " + ch)