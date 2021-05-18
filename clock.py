from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from disp_error import error, notify
from initiate import disp
font = ImageFont.truetype("Montserrat-Regular.ttf", 45)
import time
from redis_for_oled import rc
from status import status_bar
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
		try:	
			notify(disp, draw, rc.get('oled:notification').decode())
		except:
			notify(disp, draw, "")
			rc.set('oled:notification', '')
		padding = (size, 7)
		draw.text(padding, data, font=font, fill=255)
		status_bar(image, draw, disp)
		disp.image(image)
		disp.display()
	except Exception as e:
		error(disp, "Terminated")
		print(e)
		return -1
	return 0

if __name__ == "__main__":
	while True:
		execute()
