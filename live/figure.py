import pkgutil
from IPython.display import display, HTML
import cv2
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np

import live

figure_template = pkgutil.get_data(__name__, "templates/figure.html").decode("utf-8")

class Figure():
    figure_index = 0

    def __init__(self, name=None, width=30):
        if name is None:
            name = f"Figure{Figure.figure_index}"

        self.width = 30
        self.name = name
        Figure.figure_index += 1

        html = figure_template.replace(
            "{WIDTH}", str(width)
        ).replace(
            "{CHANNEL}", self.name
        )
        display(HTML(html))

    def imshow(self, img):
        if len(img.shape) not in {2, 3}:
            raise ValueError(f"Expected image to have 2 or 3 dimensions, but got {len(img.shape)}")
        elif len(img.shape) == 3 and img.shape[-1] not in {1, 3}:
            raise ValueError(f"Expected image to have 1 or 3 channels, but got {img.shape[-1]}")

        byte_array = cv2.imencode('.jpg', img)[1]
        base64_url = base64.b64encode(byte_array).decode("utf-8")

        live.broadcast(channel=self.name, message=base64_url)


    def figshow(self, fig):
        canvas = FigureCanvas(fig)
        canvas.draw()

        width, height = fig.get_size_inches() * fig.get_dpi()
        image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8').reshape(int(height), int(width), 3)
        self.imshow(image)