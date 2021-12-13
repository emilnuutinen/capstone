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
p1.setRange(xRange=[-100, 0])
p1.setLimits(xMax=0)
curve1 = p1.plot()
data1 = np.empty(100)
ptr1 = 0

win.nextRow()


p2 = win.addPlot(title="PPG 1 Infrared")
# Use automatic downsampling and clipping to reduce the drawing load
p2.setDownsampling(mode='peak')
p2.setClipToView(True)
p2.setRange(xRange=[-100, 0])
p2.setLimits(xMax=0)
curve2 = p2.plot()
data2 = np.empty(100)
ptr2 = 0

p3 = win.addPlot(title="PPG 2 Infrared")
# Use automatic downsampling and clipping to reduce the drawing load
p3.setDownsampling(mode='peak')
p3.setClipToView(True)
p3.setRange(xRange=[-100, 0])
p3.setLimits(xMax=0)
curve3 = p3.plot()
data3 = np.empty(100)
ptr3 = 0

win.nextRow()

p4 = win.addPlot(title="PPG 1 Red")
# Use automatic downsampling and clipping to reduce the drawing load
p4.setDownsampling(mode='peak')
p4.setClipToView(True)
p4.setRange(xRange=[-100, 0])
p4.setLimits(xMax=0)
curve4 = p4.plot()
data4 = np.empty(100)
ptr4 = 0

p5 = win.addPlot(title="PPG 2 Red")
# Use automatic downsampling and clipping to reduce the drawing load
p5.setDownsampling(mode='peak')
p5.setClipToView(True)
p5.setRange(xRange=[-100, 0])
p5.setLimits(xMax=0)
curve5 = p5.plot()
data5 = np.empty(100)
ptr5 = 0

win.nextRow()

p6 = win.addPlot(title="PPG 1 Green")
# Use automatic downsampling and clipping to reduce the drawing load
p6.setDownsampling(mode='peak')
p6.setClipToView(True)
p6.setRange(xRange=[-100, 0])
p6.setLimits(xMax=0)
curve6 = p6.plot()
data6 = np.empty(100)
ptr6 = 0

p7 = win.addPlot(title="PPG 2 Green")
# Use automatic downsampling and clipping to reduce the drawing load
p7.setDownsampling(mode='peak')
p7.setClipToView(True)
p7.setRange(xRange=[-100, 0])
p7.setLimits(xMax=0)
curve7 = p7.plot()
data7 = np.empty(100)
ptr7 = 0


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


def p3_update(ppg2_ir):
    global data3, ptr3
    data3[ptr3] = ppg2_ir
    ptr3 += 1
    if ptr3 >= data3.shape[0]:
        tmp = data3
        data3 = np.empty(data3.shape[0] * 2)
        data3[:tmp.shape[0]] = tmp
    curve3.setData(data3[:ptr3])
    curve3.setPos(-ptr3, 0)


def p4_update(ppg1_red):
    global data4, ptr4
    data4[ptr4] = ppg1_red
    ptr4 += 1
    if ptr4 >= data4.shape[0]:
        tmp = data4
        data4 = np.empty(data4.shape[0] * 2)
        data4[:tmp.shape[0]] = tmp
    curve4.setData(data4[:ptr4])
    curve4.setPos(-ptr4, 0)


def p5_update(ppg2_red):
    global data5, ptr5
    data5[ptr5] = ppg2_red
    ptr5 += 1
    if ptr5 >= data5.shape[0]:
        tmp = data5
        data5 = np.empty(data5.shape[0] * 2)
        data5[:tmp.shape[0]] = tmp
    curve5.setData(data5[:ptr5])
    curve5.setPos(-ptr5, 0)


def p6_update(ppg1_green):
    global data6, ptr6
    data6[ptr6] = ppg1_green
    ptr6 += 1
    if ptr6 >= data6.shape[0]:
        tmp = data6
        data6 = np.empty(data6.shape[0] * 2)
        data6[:tmp.shape[0]] = tmp
    curve6.setData(data6[:ptr6])
    curve6.setPos(-ptr6, 0)


def p7_update(ppg2_green):
    global data7, ptr7
    data7[ptr7] = ppg2_green
    ptr7 += 1
    if ptr7 >= data7.shape[0]:
        tmp = data7
        data7 = np.empty(data7.shape[0] * 2)
        data7[:tmp.shape[0]] = tmp
    curve7.setData(data7[:ptr7])
    curve7.setPos(-ptr7, 0)


def update():
    get_data = str(ser.readline())
    data = re.sub('[brn\'\\\]', '', get_data)
    if any(character.isalpha() for character in data):
        pass
    else:
        arr = [int(x.strip()) for x in data.split(',')]
        p1_update(arr[1])
        p2_update(arr[3])
        p3_update(arr[7])
        p4_update(arr[4])
        p5_update(arr[8])
        p6_update(arr[5])
        p7_update(arr[9])


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)


# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
