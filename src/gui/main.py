from pyqtgraph.Qt import QtGui, QtCore
import serial
import re
import platform
import numpy as np
import pyqtgraph as pg

# serial port of ESP32 ("COM5" in Windows)
port = "COM5" if platform.system() == "Windows" else "/dev/cu.SLAB_USBtoUART"
baud = 115200  # ESP32 uno runs at 115200 baud

ser = serial.Serial(port, baud)
print("Connected to ESP32 port:" + port)

app = QtGui.QApplication([])

win = pg.GraphicsLayoutWidget(show=True, title="Blood Pressure Monitor")
win.resize(1240, 860)
win.setWindowTitle('Blood Pressure Monitor')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="ECG")
# Use automatic downsampling and clipping to reduce the drawing load
p1.setDownsampling(mode='peak')
p1.setClipToView(True)
p1.setRange(xRange=[-1000, 0])
p1.setLimits(xMax=0)
curve1 = p1.plot()
data1 = np.empty(1000)
ptr1 = 0

win.nextRow()

p2 = win.addPlot(title="PPG 1 Infrared")
# Use automatic downsampling and clipping to reduce the drawing load
p2.setDownsampling(mode='peak')
p2.setClipToView(True)
p2.setRange(xRange=[-1000, 0])
p2.setLimits(xMax=0)
curve2 = p2.plot()
data2 = np.empty(1000)
ptr2 = 0


def p1_update(ecg):
    global data1, ptr1
    data1[ptr1] = ecg
    ptr1 += 1
    if ptr1 >= data1.shape[0]:
        tmp = data1
        data1 = np.empty(data1.shape[0] * 2)
        data1[:tmp.shape[0]] = tmp
    curve1.setData(data1[:ptr1])
    curve1.setPos(-ptr1, 0)


def p2_update(ppg1_ir):
    global data2, ptr2
    data2[ptr2] = ppg1_ir
    ptr2 += 1
    if ptr2 >= data2.shape[0]:
        tmp = data2
        data2 = np.empty(data2.shape[0] * 2)
        data2[:tmp.shape[0]] = tmp
    curve2.setData(data2[:ptr2])
    curve2.setPos(-ptr2, 0)


def update():
    get_data = str(ser.readline())
    data = re.sub('[brn\'\\\]', '', get_data)
    if any(character.isalpha() for character in data):
        pass
    else:
        arr = [int(x.strip()) for x in data.split(',')]
        p1_update(arr[1])
        p2_update(arr[3])


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(5)  # ESP runs at 200Hz which equals 5ms per loop


# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
