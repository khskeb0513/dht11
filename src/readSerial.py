from serial import Serial
import threading
from dotenv import load_dotenv
from os import environ
from datetime import datetime

load_dotenv()

port = environ.get('PORT')
baud = environ.get('BAUD')
con = Serial(port=port, baudrate=baud)
latest_line = ',,,,,,,'
parsed = {}
started_at = datetime.fromtimestamp(0)


def parse_line(line: str):
    global parsed
    items = line.split(',')
    mills = int(items[1])
    available = bool(int(items[3] or '0'))
    if not available:
        return
    humidity = float(items[5])
    temp = float(items[7])
    updated_at = datetime.fromtimestamp(started_at.timestamp() + (mills / 1000))
    parsed = {
        'mills': mills,
        'started_at': started_at,
        'updated_at': updated_at,
        'available': available,
        'humidity': humidity,
        'temp': temp
    }


def read():
    global latest_line
    global started_at
    while True:
        line = []
        for char in con.readline():
            if started_at.timestamp() < 1:
                started_at = datetime.now()
            line.append(char)
        latest_line = ''.join([chr(i) for i in line]).strip()
        if latest_line.startswith('mills,') and latest_line.endswith(';'):
            parse_line(latest_line[0:-1])


threading.Thread(target=read).start()
