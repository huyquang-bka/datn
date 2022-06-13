import numpy as np

detect_zone = []

with open('LP/detect_zone.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x, y = line.split(' ')
        detect_zone.append((int(x), int(y)))

detect_zone = np.array(detect_zone, dtype=np.int32)
detect_zone = detect_zone.reshape((-1, 1, 2))
