import numpy as np

def calculate_contrast(img) -> int:
	# Your code here
	max_v, min_v = -1, 256
	for p in img.flat:
		if max_v < p:
			max_v = p
		if min_v > p:
			min_v = p
	return int(max_v - min_v)