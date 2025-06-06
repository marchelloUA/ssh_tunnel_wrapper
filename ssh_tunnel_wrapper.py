import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer
from sshtunnel import SSHTunnelForwarder
import sys
from datetime import datetime
from babel.dates import format_date
import configparser
import os
import ipaddress
import paramiko
import re

def settings_check_alert(InformativeText):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(InformativeText)
    msg.setWindowTitle("Error")
    msg.exec_()
    formatted_date = format_date_now()
    print(f"ssh tunnel wrapper | application version: {formatted_date}")
    exit(1)

def format_date_now():
    suffix = None
    now = datetime.now()
    formatted_date = format_date(now, "d 'of' MMMM, y", locale='en')
    day = int(now.strftime("%d"))
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    formatted_date = formatted_date.replace(str(day), f"{day}{suffix}")
    return formatted_date

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        formatted_date = format_date_now()
        self.setWindowTitle(f"ssh tunnel wrapper | application version: {formatted_date}")
        self.setGeometry(160, 160, 1050, 650)

    def set_tunnel(self, tunnel):
        self.tunnel = tunnel

    def load_url(self):
        QTimer.singleShot(6000, lambda: self.browser.setUrl(QUrl(f'http://127.0.0.1:{local_port}/')))

app = QApplication(sys.argv)
if app is None:
    app = QApplication([])

if not os.path.isfile('settings.ini'):
    settings_check_alert(InformativeText = "The file 'settings.ini' does not exist!")

config = configparser.ConfigParser()
config.read('settings.ini')

ssh_host = config.get('DEFAULT', 'ssh_host')
local_port = config.get('DEFAULT', 'local_port')
remote_host = config.get('DEFAULT', 'remote_host')
remote_port = config.get('DEFAULT', 'remote_port')

with SSHTunnelForwarder(
    ssh_host,
    remote_bind_address=(remote_host, remote_port),
    local_bind_address=('127.0.0.1', local_port)
) as tunnel:
    window = MainWindow()
    try:
        window.set_tunnel(tunnel)
    except Exception as e1:
        print(f"Error during setting ssh tunnel: {e1}")
    finally:
        print(f"No error during setting ssh tunnel")
    try:
        window.load_url()
    except Exception as e2:
        print(f"Error during loading url: {e2}")
    finally:
        print(f"No error during loading url")
    try:
        window.show()
    except Exception as e3:
        print(f"Error during showing window: {e3}")
    finally:
        print(f"No error during showing window")

    # Introduce a delay before starting the event loop
    time.sleep(5)  # Adjust the delay as needed

    try:
        sys.exit(app.exec_())
    except Exception as e4:
        print(f"Error during exiting: {e4}")
    finally:
        print(f"No error during exiting")
