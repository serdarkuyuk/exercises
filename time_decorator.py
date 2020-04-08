def timeit(func):
	import time
	def wrapper(*args, **kwargs):
		time_first = time.time()
		output = func(*args, **kwargs)
		time_end = time.time()
		print(time_end-time_first)
		return output

	return wrapper	