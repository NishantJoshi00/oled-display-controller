from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
font = ImageFont.truetype("Montserrat-Regular.ttf", 12)
from redis_for_oled import rc
def status_bar(image, draw, disp):
	"""
	Images provided here should be of size 10 x 10
	"""
	left_offset = 0
	if rc.get("net:status").decode() == "1":
		image2 = Image.open("small_con.png")
		image.paste(image2, (left_offset, disp.height - 10))
	left_offset += 10
