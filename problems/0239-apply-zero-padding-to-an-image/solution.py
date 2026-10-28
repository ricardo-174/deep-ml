import numpy as np

def zero_pad_image(img, pad_width):
    if isinstance(pad_width, bool) or not isinstance(pad_width, (int,np.integer)) or pad_width<0:
        return -1 
    try:
        arr =np.asarray(img)
    except:
        return -1
    if arr.dtype == object or arr.ndim != 2:
        return -1
    if arr.shape[0] == 0 or arr.shape[1] == 0:
        return -1
    return np.pad(arr,pad_width,mode = 'constant',constant_values =0).tolist()