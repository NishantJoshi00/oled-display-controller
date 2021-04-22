import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

RST =24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
yellow = ((0, 0),(disp.width, 6)) 
blue = ((0, 7),(disp.width, disp.height))
