# gptpedal-pi

## How to start:

- source env/bin/activate

- python main.py für dweet Steuerung
- python menu.py für Menü-Steuerung

## Start on reboot script here:
- sudo nano /etc/init.d/my_server

Start:
- /etc/init.d/my_server start
- sudo update-rc.d my_server defaults

Stop:
- sudo update-rc.d my_server disable (enable)