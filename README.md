# ssh_tunnel_wrapper
wrapper for opening web app using ssh tunnel

Wrapper is a tool that users can run on their PC or laptop. It creates an SSH tunnel and opens the web app behind ssh in its window automatically.


To compile for Linux (Ubuntu), run:

sudo apt-get install libpython3.12-dev

pip install pyinstaller

pyinstaller --enable-shared --onefile ssh_tunnel_wrapper.py


Windows:

pyinstaller --hidden-import=babel --hidden-import=babel.numbers ssh_tunnel_wrapper.py


settings.ini format:

[DEFAULT]

ssh_host = ssh_host

ssh_user = ssh_user

local_port = local_port

remote_host = remote_host # internal IP address behind ssh

remote_port = remote_port # port of web app

ssh_private_key_path = /home/user1/.ssh/id_rsa

Requirements:

- Python dependencies: pip install PyQt5 PyQtWebEngine sshtunnel paramiko babel
- SSH private key must be in RSA format.
- settings.ini must be located in the same directory as the script or executable.
