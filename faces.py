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


def eyes(draw, look):
	"""
	look in ["plain", "poker", "angry"]
	"""
	bound = disp.height - 16
	if look == "plain":
		draw.ellipse(((disp.width-bound)//2, 16, (disp.width-bound)//2 + bound//3, 16 + bound//3), fill=255)
		draw.ellipse(((disp.width-bound)//2 + 2 * bound//3, 16, (disp.width-bound)//2 + bound, 16 + bound//3), fill=255)
	elif look == 'poker':
		draw.line(((disp.width-bound)//2, 16 + bound // 6, (disp.width-bound)//2 + bound//3, 16 + bound // 6), width=3, fill=255)
		draw.line(((disp.width-bound)//2 + 2 * bound // 3, 16 + bound // 6, (disp.width-bound)//2 + bound, 16 + bound // 6), width=3, fill=255)
	elif look == 'angry':
		draw.line(((disp.width-bound)//2, 16 , (disp.width-bound)//2 + bound//3, 16 + bound // 3), width=3, fill=255)
		draw.line(((disp.width-bound)//2 + 2 * bound // 3, 16 + bound // 3, (disp.width-bound)//2 + bound, 16), width=3, fill=255)

def mouth(draw, look):
	"""
	look in ["smile", "plain", "sad"]
	"""
	bound = disp.height - 16
	box_bound = ((disp.width - bound)//2, 16 + bound // 3, (disp.width - bound) // 2 + bound, 16 + bound)
	if look == 'smile':
		draw.arc(box_bound, start=0, end=180, fill=255, width=3)
	elif look == 'plain':
		draw.line((box_bound[0], box_bound[1] + bound // 3, box_bound[2], box_bound[3] - bound // 3), fill=255, width=3)
	elif look == 'sad':
		draw.arc((box_bound[0], box_bound[1] + bound // 3, box_bound[2], box_bound[3] + bound // 3), start=180, end=360, fill=255, width=3)

def execute():
	try:
		image = Image.new('1', (disp.width, disp.height))
		draw = ImageDraw.Draw(image)
		notify(disp, draw, rc.get('oled:notification').decode())
		eyes(draw, 'angry')
		mouth(draw, 'sad')
		disp.image(image)
		disp.display()
	except e:
		print("Terminated", e)
		return -1
	return 0

if __name__ == "__main__":
	execute()

