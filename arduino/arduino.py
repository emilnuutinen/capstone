import serial
import datetime
import re
import platform
from pathlib import Path

# serial port of Arduino
port = "COM5" if platform.system() == "Windows" else "/dev/cu.SLAB_USBtoUART"
baud = 115200  # Arduino runs at 115200 baud

# connect to Arduino
ser = serial.Serial(port, baud)
print("Connected toArduino port:" + port)

# take datetime now in ISO 8061 format and make that the filename
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

# path for the data file
data_folder = Path("data/raw/")
file_path = data_folder / file_name

samples = 100  # how many samples to collect
line = 0

while line < samples:

    get_data = str(ser.readline())

    # remove extra characters from the data
    data = re.sub('[brn\'\\\]', '', get_data)
    print(data)

    # ignore information printed in the first lines from the Arduino
    if any(character.isalpha() for character in data):
        pass
    else:
        file = open(file_path, "a")
        # ecg_time, ecg, ppg1_time, ppg1_ir, ppg1_red, ppg1_green, ppg2_time, ppg2_ir, ppg2_red, ppg2_green
        file.write(data + "\n")
        line += 1

print("Finished")
file.close()
