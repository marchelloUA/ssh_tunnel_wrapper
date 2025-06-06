# ssh_tunnel_wrapper

wrapper for opening web app using ssh tunnel

Wrapper is a tool that users can run on their PC or laptop. It creates an SSH tunnel and opens the web app behind ssh in its window automatically.

## Pyinstaller

### Linux

To compile for Linux (Ubuntu), run:

```shell
sudo apt-get install libpython3.12-dev
pip install pyinstaller
pyinstaller --enable-shared --onefile ssh_tunnel_wrapper.py
```

### Windows

```powershell
pyinstaller --hidden-import=babel --hidden-import=babel.numbers ssh_tunnel_wrapper.py

```

## Python venv module

```shell
cd ssh_tunnel_wrapper/
python3 -m venv .venv/
.venv/bin/activate
pip3 install -r requirements.txt
```

## Configuration

Configuration is based on your ```~/.ssh/config``` file.

```dosini
[DEFAULT]

ssh_host = ssh_host             # as defined in ssh_config
local_port = local_port         # Port listened on 127.0.0.1
remote_host = remote_host       # internal IP address or hostname
remote_port = remote_port       # port of web app

```
