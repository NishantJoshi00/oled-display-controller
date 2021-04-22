"""
Config Format
{
    delay: optional! [default: 10s]
	screnes: [functions_to_execute]
	frame_rate: optional! [default: 60]
}
128 x 15 are yellow pixels
the other are blue
"""

import time
import json
from redis_for_oled import rc
def load_scenes():
	state = rc.get('oled:scene')
	if state == None:
		state = 0
		rc.set('oled:scene', 0)
	else:
		state = state.decode()
		state = int(state)
	return state

def load_config(filename):
	with open("old-config.json") as f:
		data = json.load(f)
	if 'frame_rate' in data:
		frame_rate = data['frame_rate']
	else:
		frame_rate = 60

	wait = 1/frame_rate
	if 'delay' in data:
		delay = data['delay']
	else:
		delay = -1

	scenes = data['scenes']
	for i in range(len(scenes)):
		module, function = scenes[i].split(".")
		scenes[i] = __import__(module).__getattribute__(function)
	count = 0
	scene = load_scenes()
	return (count, scene, scenes, delay, wait, frame_rate)

count, scene, scenes, delay, wait, frame_rate = load_config("old-config.json")

cycles = 0
while True:
	time.sleep(wait)
	count += wait
	if count >= delay and delay != -1:
		count = 0
		if scene == len(scenes) - 1:
			cycles += 1
			if cycles == 20:
				cycles = 0
				count, scene, scenes, delay, wait, frame_rate = load_config("old-config.json")
			scene = 0
		else:
			scene += 1
	elif delay == -1 and int(count) % 10 == 0:
		count, scene, scenes, delay, wait, frame_rate = load_config("old-config.json")
		if scene > len(scenes) or scene < 0:
			scene = 0
	
	code = scenes[scene]()
	print(code)
	if code != 0:
		break
