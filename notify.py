from initiate import disp
from disp_error import error
import sys

if len(sys.argv) < 2:
	exit()
else:
	if sys.argv[1] == 'clear':
		disp.clear()
		disp.display()
	elif sys.argv[1] == 'put':
		disp.clear()
		error(disp, sys.argv[2])

