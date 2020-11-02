import pkgutil
from IPython.display import display, HTML
import cv2
import base64
import io
import skimage.io
import matplotlib.pyplot as plt
import numpy as np
import re
from collections import Counter

import live
import live.gif
import live.renderer

class Figure():
    figure_index = 0

    def __init__(self, name=None, width=30, memory_enabled=True):
        if name is None:
            name = f"Figure{Figure.figure_index}"

        self.width = 30
        self.name = re.sub(r'[^a-zA-Z0-9_]', '', name)
        Figure.figure_index += 1

        live.renderer.listen(self.name, width)

        self.memory_enabled = memory_enabled
        if memory_enabled:
            self.memory = []

    def imshow(self, img):
        if len(img.shape) not in {2, 3}:
            raise ValueError(f"Expected image to have 2 or 3 dimensions, but got {len(img.shape)}")
        elif len(img.shape) == 3 and img.shape[-1] not in {1, 3}:
            raise ValueError(f"Expected image to have 1 or 3 channels, but got {img.shape[-1]}")

        if img.dtype == np.floating:
            img = (img * 255).astype(np.uint8)

        if self.memory_enabled:
            self.memory.append(img)

        if len(img.shape) == 3:
            img = np.flip(img, axis=2)

        byte_array = cv2.imencode('.jpg', img)[1]
        base64_url = base64.b64encode(byte_array).decode("utf-8")

        live.renderer.broadcast(self.name, 'data:image/jpg;base64,' + base64_url)

    def vidshow(self, vid, fps=10):
        if len(vid.shape) != 4:
            raise ValueError(f"Expected video to have 4 dimensions, but got {len(vid.shape)}")
        if vid.shape[-1] != 3:
            raise ValueError(f"Expected video to have 3 channels, but got {vid.shape[-1]}")

        base64_url = live.gif.video_to_gif(vid, fps)
        live.renderer.broadcast(self.name, 'data:image/gif;base64,' + base64_url)

    def repeat(self, shape=None, fps=10):
        if not self.memory:
            raise ValueError(f"No figures in memory.")

        rgb_imgs = [cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) if len(img.shape) == 2 else img for img in self.memory]

        if shape is None:
            memory_shapes = [(img.shape[1], img.shape[0]) for img in rgb_imgs]
            shape = Counter(memory_shapes).most_common(1)[0][0]

        vid = np.array([cv2.resize(img, shape, interpolation=cv2.INTER_NEAREST) for img in rgb_imgs])
        self.vidshow(vid, fps)

    def figshow(self, fig=None):
        if fig is not None:
            fig = plt.gcf()

        buf = io.BytesIO()
        fig.savefig(buf, format='jpg')
        plt.close()
        buf.seek(0)
        img = skimage.io.imread(buf)
        self.imshow(img)
