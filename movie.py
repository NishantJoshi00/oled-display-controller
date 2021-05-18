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
import tarfile

def get_tar(filename):
	return tarfile.open(filename, 'r:gz')

def static_vars(**kwargs):
	def decorate(func):
		for k in kwargs:
			setattr(func, k, kwargs[k])
		return func
	return decorate

@static_vars(frame=0, movie=get_tar("rick_roll.tar.gz"))
def execute():
	try:
		if execute.frame == len(execute.movie.getnames()):
			execute.frame = 0

		image = image.open(execute.movie.extractfile(execute.movie.getnames()[execute.frame]))
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
		
