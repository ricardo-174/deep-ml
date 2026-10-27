import numpy as np

def rgb_to_grayscale(image):
    if not image or not image[0] or not isinstance(image[0][0], (list, tuple)):
        return -1
    l = len(image[0])
    if any(len(row) != l for row in image):
        return -1
    out = []
    for row in image:
        g_row = []
        for px in row:
            if len(px) != 3 or not all(0 <= c <= 255 for c in px):
                return -1
            g_row.append(round(0.299 * px[0]+0.587 * px[1]+0.114 * px[2]))
        out.append(g_row)
    return out