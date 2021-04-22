from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from disp_error import error, notify
from initiate import disp
font = ImageFont.truetype("Montserrat-Regular.ttf", 50)
import time
from redis_for_oled import rc
def execute():
	global blink
	try:
		time.sleep(.1)
		data = datetime.now().time().isoformat().split(".")[0]
		secs = data[-2:]
		data = data[:-3]
		if int(secs) % 2 == 0:
			data = data.replace(':', " ")


		image = Image.new('1', (disp.width, disp.height))
		draw = ImageDraw.Draw(image)
		size = disp.width - font.getsize(data)[0]
		size = size // 2
		
		notify(disp, draw, rc.get('oled:notification').decode())
		padding = (size, 7)
		draw.text(padding, data, font=font, fill=255)
		disp.image(image)
		disp.display()
	except e:
		error(disp, "Terminated")
		print(e)
		return -1
	return 0

if __name__ == "__main__":
	while True:
		execute()
