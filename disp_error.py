from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
font = ImageFont.truetype("Montserrat-Regular.ttf", 12)

def error(disp, text):
	disp.clear()
	size = disp.width - font.getsize(text.lower())[0]
	size = size // 2
	image = Image.new('1', (disp.width, disp.height))
	draw = ImageDraw.Draw(image)
	draw.text((size, 0), text.lower(), font=font, fill=255)
	disp.image(image)
	disp.display()

def notify(disp, draw, text):
	size = disp.width - font.getsize(text.lower())[0]
	size = size // 2
	draw.text((size, 0), text.lower(), font=font, fill=255)

