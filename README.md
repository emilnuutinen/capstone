# Continuous non-invasive blood pressure monitoring

### Components used

- [Adafruit HUZZAH32 – ESP32 Feather Board](https://www.adafruit.com/product/3405)
- [MAX30105 Particle and Pulse Ox Sensor(PPG)](https://www.sparkfun.com/products/16474)
- [Gravity: Analog Heart Rate Monitor Sensor (ECG)](https://www.dfrobot.com/product-1510.html)

### Hardware configuration
The hardware configuration is described with a diagram in the following location:

[Pinout Diagram](https://github.com/emilnuutinen/capstone/blob/master/arduino/ptt-esp32/pinout-diagram.jpg)

### 3D-model
The 3D-printed clip is used to connect the MAX30105 Particle and Pulse Ox Sensor(PPG) sensor:

[3D-model](https://github.com/emilnuutinen/capstone/tree/master/3D-model)  

### Data

Files include data from different collection sessions.

### Notebooks

The required libraries:
- matplotlib 
- numpy
- pandas
- scipy
- sklearn
- biosppy.signals
- neurokit2
- xgboost

Each file the requirments are always presented first.

### Usage

Install dependencies with Conda:

```
conda install pyqtgraph pyserial numpy 
```

You can also install everything with pip:

```
pip install pyqtgraph pyserial numpy 
```

After installation you can run the data collecting script with:

```
python src/data/collect_data.py
```

You can also start the real time monitor GUI with:

```
python src/gui/main.py
```
