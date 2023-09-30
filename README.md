# gptpedal-pi

## Insallation links for pyo:
- http://ajaxsoundstudio.com/pyodoc/compiling.html (sudo apt-get install libjack-jackd2-dev libportmidi-dev portaudio19-dev liblo-dev libsndfile-dev)
- https://www.wxpython.org/pages/downloads/ (https://extras.wxpython.org/wxPython4/extras/manylinux-test/)

## How to start:
- python -m venv env
- source env/bin/activate
- pip install -r requirements.txt

- python main.py für dweet Steuerung
- python menu.py für Menü-Steuerung

## Start on reboot script here:
- sudo nano /home/pi/.config/autostart/gptpedal.desktop

- this runs startme.sh