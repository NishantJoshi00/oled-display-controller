from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from disp_error import error, notify
from initiate import disp
import time
def bootimage(stime):
	image = Image.new('1', (disp.width, disp.height))
	image2 = Image.open('assets/s_cat.jpg')
	image.paste(image2, ((128 - 80) // 2, 0))
	disp.image(image)
	disp.display()
	time.sleep(stime)
