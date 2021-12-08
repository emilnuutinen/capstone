from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

app = QtGui.QApplication([])

win = pg.GraphicsLayoutWidget(show=True, title="Blood Pressure Monitor")
win.resize(1000, 600)
win.setWindowTitle('Blood Pressure Monitor')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)


p1 = win.addPlot(title="ECG")
curve1 = p1.plot(pen='y')
data1 = data = np.random.normal(size=(10, 1000))
ptr1 = 0

win.nextRow()

p2 = win.addPlot(title="PPG 1 Infrared")
curve2 = p2.plot(pen='y')
data2 = data = np.random.normal(size=(10, 1000))
ptr2 = 0

p3 = win.addPlot(title="PPG 2 Infrared")
curve3 = p3.plot(pen='y')
data3 = data = np.random.normal(size=(10, 1000))
ptr3 = 0

win.nextRow()

p4 = win.addPlot(title="PPG 1 Red")
curve4 = p4.plot(pen='y')
data4 = data = np.random.normal(size=(10, 1000))
ptr4 = 0

p5 = win.addPlot(title="PPG 2 Red")
curve5 = p5.plot(pen='y')
data5 = data = np.random.normal(size=(10, 1000))
ptr5 = 0

win.nextRow()

p6 = win.addPlot(title="PPG 1 Green")
curve6 = p6.plot(pen='y')
data6 = data = np.random.normal(size=(10, 1000))
ptr6 = 0

p7 = win.addPlot(title="PPG 2 Green")
curve7 = p7.plot(pen='y')
data7 = data = np.random.normal(size=(10, 1000))
ptr7 = 0


def p1_update():
    global curve1, data1, ptr1, p1
    curve1.setData(data1[ptr1 % 10])
    if ptr1 == 0:
        # stop auto-scaling after the first data set is plotted
        p1.enableAutoRange('xy', False)
    ptr1 += 1


def p2_update():
    global curve2, data2, ptr2, p2
    curve2.setData(data2[ptr2 % 10])
    if ptr2 == 0:
        # stop auto-scaling after the first data set is plotted
        p2.enableAutoRange('xy', False)
    ptr2 += 1


def p3_update():
    global curve3, data3, ptr3, p3
    curve3.setData(data3[ptr3 % 10])
    if ptr3 == 0:
        # stop auto-scaling after the first data set is plotted
        p3.enableAutoRange('xy', False)
    ptr3 += 1


def p4_update():
    global curve4, data4, ptr4, p4
    curve4.setData(data4[ptr4 % 10])
    if ptr4 == 0:
        # stop auto-scaling after the first data set is plotted
        p4.enableAutoRange('xy', False)
    ptr4 += 1


def p5_update():
    global curve5, data5, ptr5, p5
    curve5.setData(data5[ptr5 % 10])
    if ptr5 == 0:
        # stop auto-scaling after the first data set is plotted
        p5.enableAutoRange('xy', False)
    ptr5 += 1


def p6_update():
    global curve6, data6, ptr6, p6
    curve6.setData(data6[ptr6 % 10])
    if ptr6 == 0:
        # stop auto-scaling after the first data set is plotted
        p6.enableAutoRange('xy', False)
    ptr6 += 1


def p7_update():
    global curve7, data7, ptr7, p7
    curve7.setData(data7[ptr7 % 10])
    if ptr7 == 0:
        # stop auto-scaling after the first data set is plotted
        p7.enableAutoRange('xy', False)
    ptr7 += 1


timer = QtCore.QTimer()
timer.timeout.connect(p1_update)
timer.timeout.connect(p2_update)
timer.timeout.connect(p3_update)
timer.timeout.connect(p4_update)
timer.timeout.connect(p5_update)
timer.timeout.connect(p6_update)
timer.timeout.connect(p7_update)

timer.start(30)


# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
