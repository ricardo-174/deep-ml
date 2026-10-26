
def calculate_brightness(img):
	# Write your code here
	if not img or not img[0]:
		return -1
	col = len(img[0])
	if any(len(row) !=col for row in img):
		return -1
	total,count = 0,0
	for row in img:
		for p in row:
			if not(0<= p <=255):
				return -1
			total+=p
			count+=1
	return round(total/count,2)
