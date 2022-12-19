import numpy as np
import matplotlib.pyplot as plt
import os
import json
import cv2

IMG_WIDTH=400
IMG_HEIGHT=230
DATA_DIR = 'data'
IMG_SAMPLES_DIR = os.path.join(DATA_DIR, 'samples')
DATA_JOURNAL = os.path.join(DATA_DIR, 'journal.json')

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

def save_json(obj, file_path: str):
    json_string = json.dumps(obj)
    with open(file_path, 'w') as file:
        file.write(json_string)

    print(f'Saved journal to {file_path}')

def save_img(data, file_path: str):
    result = cv2.imwrite(file_path, data)
    if result != True:
        raise f'Could not save {file_path}, because {file_path}'

ensure_dir(DATA_DIR)
ensure_dir(IMG_SAMPLES_DIR)


blank_img = np.ones([IMG_HEIGHT, IMG_WIDTH]) * 255
# plt.imshow(blank_img, cmap='gray', vmin=0, vmax=255)
# plt.show()

samples = []

for y in range(IMG_HEIGHT):
    for x in range(IMG_WIDTH):
        sample = {
            'src': os.path.join(IMG_SAMPLES_DIR, f'img_{x}-{y}.png'),
            'result': {
                'x': x,
                'y': y
            }
        }

        blank_img[y][x]=0

        save_img(blank_img, sample['src'])

        blank_img[y][x]=255

        samples.append(sample)

save_json(samples, DATA_JOURNAL)
