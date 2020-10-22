# ESP8266Thermometer

mlx90614 driver
---
[https://github.com/mcauser/micropython-mlx90614](https://github.com/mcauser/micropython-mlx90614)

ssd1306 oled driver
---
[https://github.com/adafruit/micropython-adafruit-ssd1306](https://github.com/adafruit/micropython-adafruit-ssd1306)

vl53l0x driver
---
[https://github.com/uceeatz/VL53L0X](https://github.com/uceeatz/VL53L0X)

这个直接把 `*.py` 放到 ESP8266 上运行会报错，需要先转成 `*.mpy` 然后将 `*.mpy` 文件传到 ESP8266 上执行。

1、先安装 ampy 工具

```py
pip3 install adafruit-ampy
```

![](https://github.com/SuWeipeng/img/raw/master/24_ESP8266/mpy_02.jpg)

2、通过 micropython 源码工具生成 `*.mpy`

```py
./mpy-cross VL53L0X.py
```

![](https://github.com/SuWeipeng/img/raw/master/24_ESP8266/mpy_01.jpg)

3、将 `*.mpy` 传到 ESP8266

![](https://github.com/SuWeipeng/img/raw/master/24_ESP8266/mpy_03.jpg)