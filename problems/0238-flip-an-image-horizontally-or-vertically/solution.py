import numpy as np

def flip_image(image, direction):
    if direction not in ('horizontal','vertical'):
        return -1
    try:
        arr = np.asarray(image)
    except Exception:
        return -1
    if arr.dtype == object or arr.ndim not in (2,3):
        return -1
    if arr.shape[0] ==0 or arr.shape[1] == 0 or (arr.ndim == 3 and arr.shape[2] ==0):
        return -1
    if direction == 'horizontal':
        return arr[:,::-1].tolist()
    return arr[::-1].tolist()
