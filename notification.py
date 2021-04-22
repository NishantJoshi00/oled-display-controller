from redis_for_oled import rc

import sys
if len(sys.argv) == 1:
	rc.set('oled:notification', '')
else:
	rc.set('oled:notification'. str(sys.argv[1])

