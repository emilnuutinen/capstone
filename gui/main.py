from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

app = QtGui.QApplication([])

win = pg.GraphicsLayoutWidget(show=True, title="Blood Pressure Monitor")
win.resize(1920, 1080)
win.setWindowTitle('Blood Pressure Monitor')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

chunkSize = 100
maxChunks = 10
startTime = pg.ptime.time()

p1 = win.addPlot(title="ECG")
p1.setLabel('bottom', 'Time', 's')
p1.setXRange(-10, 0)
curves1 = []
data1 = np.empty((chunkSize+1, 2))
ptr1 = 0

win.nextRow()

p2 = win.addPlot(title="PPG 1 Infrared")
p2.setLabel('bottom', 'Time', 's')
p2.setXRange(-10, 0)
curves2 = []
data2 = np.empty((chunkSize+1, 2))
ptr2 = 0

p3 = win.addPlot(title="PPG 2 Infrared")
p3.setLabel('bottom', 'Time', 's')
p3.setXRange(-10, 0)
curves3 = []
data3 = np.empty((chunkSize+1, 2))
ptr3 = 0

win.nextRow()

p4 = win.addPlot(title="PPG 1 Red")
p4.setLabel('bottom', 'Time', 's')
p4.setXRange(-10, 0)
curves4 = []
data4 = np.empty((chunkSize+1, 2))
ptr4 = 0

p5 = win.addPlot(title="PPG 2 Red")
p5.setLabel('bottom', 'Time', 's')
p5.setXRange(-10, 0)
curves5 = []
data5 = np.empty((chunkSize+1, 2))
ptr5 = 0

win.nextRow()

p6 = win.addPlot(title="PPG 1 Green")
p6.setLabel('bottom', 'Time', 's')
p6.setXRange(-10, 0)
curves6 = []
data6 = np.empty((chunkSize+1, 2))
ptr6 = 0

p7 = win.addPlot(title="PPG 2 Green")
p7.setLabel('bottom', 'Time', 's')
p7.setXRange(-10, 0)
curves7 = []
data7 = np.empty((chunkSize+1, 2))
ptr7 = 0


def p1_update():
    global p1, data1, ptr1, curves1
    now = pg.ptime.time()
    for c in curves1:
        c.setPos(-(now-startTime), 0)

    i = ptr1 % chunkSize
    if i == 0:
        curve = p1.plot()
        curves1.append(curve)
        last = data1[-1]
        data1 = np.empty((chunkSize+1, 2))
        data1[0] = last
        while len(curves1) > maxChunks:
            c = curves1.pop(0)
            p1.removeItem(c)
    else:
        curve = curves1[-1]
    data1[i+1, 0] = now - startTime
    data1[i+1, 1] = np.random.normal()
    curve.setData(x=data1[:i+2, 0], y=data1[:i+2, 1])
    ptr1 += 1


def p2_update():
    global p2, data2, ptr2, curves2
    now = pg.ptime.time()
    for c in curves2:
        c.setPos(-(now-startTime), 0)

    i = ptr2 % chunkSize
    if i == 0:
        curve = p2.plot()
        curves2.append(curve)
        last = data2[-1]
        data2 = np.empty((chunkSize+1, 2))
        data2[0] = last
        while len(curves2) > maxChunks:
            c = curves2.pop(0)
            p2.removeItem(c)
    else:
        curve = curves2[-1]
    data2[i+1, 0] = now - startTime
    data2[i+1, 1] = np.random.normal()
    curve.setData(x=data2[:i+2, 0], y=data2[:i+2, 1])
    ptr2 += 1


def p3_update():
    global p3, data3, ptr3, curves3
    now = pg.ptime.time()
    for c in curves3:
        c.setPos(-(now-startTime), 0)

    i = ptr3 % chunkSize
    if i == 0:
        curve = p3.plot()
        curves3.append(curve)
        last = data3[-1]
        data3 = np.empty((chunkSize+1, 2))
        data3[0] = last
        while len(curves3) > maxChunks:
            c = curves3.pop(0)
            p3.removeItem(c)
    else:
        curve = curves3[-1]
    data3[i+1, 0] = now - startTime
    data3[i+1, 1] = np.random.normal()
    curve.setData(x=data3[:i+2, 0], y=data3[:i+2, 1])
    ptr3 += 1


def p4_update():
    global p4, data4, ptr4, curves4
    now = pg.ptime.time()
    for c in curves4:
        c.setPos(-(now-startTime), 0)

    i = ptr4 % chunkSize
    if i == 0:
        curve = p4.plot()
        curves4.append(curve)
        last = data4[-1]
        data4 = np.empty((chunkSize+1, 2))
        data4[0] = last
        while len(curves4) > maxChunks:
            c = curves4.pop(0)
            p4.removeItem(c)
    else:
        curve = curves4[-1]
    data4[i+1, 0] = now - startTime
    data4[i+1, 1] = np.random.normal()
    curve.setData(x=data4[:i+2, 0], y=data4[:i+2, 1])
    ptr4 += 1


def p5_update():
    global p5, data5, ptr5, curves5
    now = pg.ptime.time()
    for c in curves5:
        c.setPos(-(now-startTime), 0)

    i = ptr5 % chunkSize
    if i == 0:
        curve = p5.plot()
        curves5.append(curve)
        last = data5[-1]
        data5 = np.empty((chunkSize+1, 2))
        data5[0] = last
        while len(curves5) > maxChunks:
            c = curves5.pop(0)
            p5.removeItem(c)
    else:
        curve = curves5[-1]
    data5[i+1, 0] = now - startTime
    data5[i+1, 1] = np.random.normal()
    curve.setData(x=data5[:i+2, 0], y=data3[:i+2, 1])
    ptr5 += 1


def p6_update():
    global p6, data6, ptr6, curves6
    now = pg.ptime.time()
    for c in curves6:
        c.setPos(-(now-startTime), 0)

    i = ptr6 % chunkSize
    if i == 0:
        curve = p6.plot()
        curves6.append(curve)
        last = data6[-1]
        data6 = np.empty((chunkSize+1, 2))
        data6[0] = last
        while len(curves6) > maxChunks:
            c = curves6.pop(0)
            p6.removeItem(c)
    else:
        curve = curves6[-1]
    data6[i+1, 0] = now - startTime
    data6[i+1, 1] = np.random.normal()
    curve.setData(x=data6[:i+2, 0], y=data3[:i+2, 1])
    ptr6 += 1


def p7_update():
    global p7, data7, ptr7, curves7
    now = pg.ptime.time()
    for c in curves7:
        c.setPos(-(now-startTime), 0)

    i = ptr7 % chunkSize
    if i == 0:
        curve = p7.plot()
        curves7.append(curve)
        last = data7[-1]
        data7 = np.empty((chunkSize+1, 2))
        data7[0] = last
        while len(curves7) > maxChunks:
            c = curves7.pop(0)
            p7.removeItem(c)
    else:
        curve = curves7[-1]
    data7[i+1, 0] = now - startTime
    data7[i+1, 1] = np.random.normal()
    curve.setData(x=data7[:i+2, 0], y=data3[:i+2, 1])
    ptr7 += 1


def update():
    p1_update()
    p2_update()
    p3_update()
    p4_update()
    p5_update()
    p6_update()
    p7_update()


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)


# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
