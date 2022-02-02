import serial
import datetime
import re
import platform
import os
from pathlib import Path
import time

# serial port of ESP32
port = "COM5" if platform.system() == "Windows" else "/dev/cu.SLAB_USBtoUART"
baud = 115200  # ESP32 runs at 115200 baud

# connect to ESP32
ser = serial.Serial(port, baud)
print("Connected to ESP32 port:" + port)

# take datetime now in ISO 8061 format and make that the filename
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

# path for the data file
data_folder = Path("data/raw/" + now.strftime("%Y-%m-%d-%H-%M-%S")+ "/")
os.mkdir(data_folder)
file_path = data_folder / file_name

t_end = time.time() + 60  # Set the loop length in seconds

# while line < samples:
while time.time() < t_end:

    get_data = str(ser.readline())

    # remove extra characters from the data
    data = re.sub('[brn\'\\\]', '', get_data)
    print(data)

    # ignore information printed in the first lines from the ESP32
    if any(character.isalpha() for character in data):
        pass
    else:
        file = open(file_path, "a")
        # ecg_time, ecg, ppg_time, ppg_green
        file.write(data + "\n")
        #line += 1

print("Finished")
file.close()
