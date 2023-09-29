# gptpedal-pi

## How to start:

- source env/bin/activate

- python main.py für dweet Steuerung
- python menu.py für Menü-Steuerung

## Start service at:
- /etc/systemd/system/gptpedal-raspi.service
- Start: sudo systemctl enable gptpedal-raspi.service
- Status: sudo systemctl status gptpedal-raspi.service
- Stop: sudo systemctl status gptpedal-raspi.service + sudo systemctl disable gptpedal-raspi.service
