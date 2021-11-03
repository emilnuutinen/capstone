import serial

arduino_port = "/dev/cu.SLAB_USBtoUART"  # serial port of Arduino
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
    if line > 8:
        file = open(fileName, "a")
        file.write(data[2:-5] + "\r\n")  # write data with a newline
    line = line+1

print("Data collection complete!")
file.close()
