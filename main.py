import time
import mlx90614, oled
from machine import I2C, Pin

i2c = I2C(scl=Pin(14), sda=Pin(12))

i2c_device = i2c.scan()

if 90 in i2c_device:
    sensor = mlx90614.MLX90614(i2c)

if 60 in i2c_device:
    oled_width = 128
    oled_height = 32
    oled = oled.SSD1306_I2C(oled_width, oled_height, i2c)

if 41 in i2c_device:
    import VL53L0X
    tof = VL53L0X.VL53L0X(i2c)

while True:
    i2c_device = i2c.scan()
    if 41 in i2c_device:
        tof.start()
        tof.read()
        dist_str = "dist: " + "%.1f"%(tof.read()/10) + " cm"
        tof.stop()
    else:
        dist_str = ""

    if 90 in i2c_device:
        printstr = "temp : %.1f"%(sensor.read_object_temp())
    else:
        printstr = "No sensor!!!"
        
    if 60 in i2c_device:
        oled.fill(0)
        oled.text(dist_str, 10, 0)
        oled.text(printstr, 10, 16)
        oled.show()
    time.sleep_ms(500)

