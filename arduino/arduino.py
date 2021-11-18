import serial
import datetime
from pathlib import Path

# serial port of Arduino ("COM5" in Windows)
arduino_port = "/dev/cu.SLAB_USBtoUART"
baud = 115200  # arduino uno runs at 115200 baud

# take datetime now in ISO 8061 format and make that the filename
now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d-%H-%M-%S") + "PPG_ONLY_CLIP.csv"

# Path for the data file
data_folder = Path("data/raw/")
file_path = data_folder / file_name

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)

samples = 2000  # how many samples to collect
line = 0
while line <= samples:
    get_data = str(ser.readline())
    data = get_data  # ecg_timestamp,ecg,ppg1_timestamp,ppg1_ir,ppg1_red,ppg1_green,ppg2_timestamp,ppg2_ir,ppg2_red,ppg2_green
    print(data)
    if line > 10:  # Ignore Arduino info in the beginning
        file = open(file_path, "a")
        file.write(data[2:-5] + "\r\n")  # Ignore extra characters
    line = line+1

print("Finished")
file.close()
