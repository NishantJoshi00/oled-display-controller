def static_vars(**kwargs):
	def decorate(func):
		for k in kwargs:
			setattr(func, k, kwargs[k])
		return func
	return decorate


@static_vars(frame=0)
def framer(frame):
	val = framer.frame
	framer.frame = frame
	return val

