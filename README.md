# piTemp

# Installer les dépendances
sudo apt update
sudo apt install python3-pip
pip3 install Adafruit_DHT flask matplotlib

# Créer le fichier app.py
python3 app.py

# 1. Créer un service systemd
sudo nano /etc/systemd/system/dht11-web.service

# Contenu du fichier dht11-web.service
[Unit]
Description=Serveur Flask de température DHT11
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/app.py
WorkingDirectory=/home/pi
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi
Environment=FLASK_ENV=production

[Install]
WantedBy=multi-user.target

# Recharger systemd et activer le service
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable dht11-web.service
sudo systemctl start dht11-web.service

# Vérifier que ça tourne
sudo systemctl status dht11-web.service

# Voir les logs
journalctl -u dht11-web.service -f
