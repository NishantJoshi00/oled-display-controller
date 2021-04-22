from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from disp_error import error, notify
from initiate import disp
font = ImageFont.truetype("Montserrat-Regular.ttf", 50)
import time
import math
from redis_for_oled import rc
def execute():
	global blink
	try:
		data = datetime.now().time().isoformat().split(":")[-1]
		secs = float(data)
		image = Image.new('1', (disp.width, disp.height))
		draw = ImageDraw.Draw(image)
		size = disp.width - font.getsize(data)[0]
		size = size // 2
		notify(disp, draw, rc.get('oled:notification').decode())
		sinsize = 10
		for i in range(disp.width):
			draw.point((i, ((disp.height - 7) / 2 + 7 + sinsize * math.sin(secs * i/60))), fill=255)
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
