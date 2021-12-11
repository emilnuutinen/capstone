# Continuous non-invasive blood pressure monitoring

### Components used

- [Adafruit HUZZAH32 – ESP32 Feather Board](https://www.adafruit.com/product/3405)
- [MAX30105 Particle and Pulse Ox Sensor(PPG)](https://www.sparkfun.com/products/16474)
- [Gravity: Analog Heart Rate Monitor Sensor (ECG)](https://www.dfrobot.com/product-1510.html)

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


