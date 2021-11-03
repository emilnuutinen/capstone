import serial

# serial port of Arduino ("COM5" in Windows)
arduino_port = "/dev/cu.SLAB_USBtoUART"
baud = 115200  # arduino uno runs at 115200 baud
fileName = "sensor_data.csv"  # name of the CSV file generated

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)

samples = 100  # how many samples to collect
line = 0
while line <= samples:
    getData = str(ser.readline())
    data = getData  # ecg_timestamp,ecg,ppg1_timestamp,ppg1_ir,ppg1_red,ppg1_green,ppg2_timestamp,ppg2_ir,ppg2_red,ppg2_green
    print(data)
    if line > 8:  # Ignore Arduino info in the beginning
        file = open(fileName, "a")
        file.write(data[2:-5] + "\r\n")  # Ignore extra characters
    line = line+1

print("Finished")
file.close()
