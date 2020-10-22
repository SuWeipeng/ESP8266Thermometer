import time
import mlx90614, oled
from machine import I2C, Pin

i2c = I2C(scl=Pin(14), sda=Pin(12))

i2c_device = i2c.scan()

if 64 in i2c_device:
    import si7051
    si7051 = si7051.Si705x(i2c=i2c)
    
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
    
    if 90 in i2c_device:
        t1 = sensor.read_object_temp()
        line_2 = "temp : %.1f"%(t1)
    else:
        line_2 = "No sensor!!!"
        
    if 64 in i2c_device:
        t2 = si7051.temperature
        line_3 = "tmep : " + "%.1f"%(t2)
        line_1 = "delta: " + "%.1f"%(t2-t1)
    else:
        line_3 = ""
        line_1 = ""
        
    if 41 in i2c_device:
        tof.start()
        tof.read()
        line_1 = "dist: " + "%.1f"%(tof.read()/10) + " cm"
        tof.stop()
    elif 64 not in i2c_device:
        line_1 = ""
        
    if 60 in i2c_device:
        oled.fill(0)
        oled.text(line_1, 10, 0)
        oled.text(line_2, 10, 15)
        oled.text(line_3, 10, 25)
        oled.show()
    time.sleep_ms(500)

