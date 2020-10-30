from IPython.display import display, Javascript
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import inspect

from live.figure import Figure

figures = {}

def figure(name=None, width=30, memory_enabled=True):
    context = get_current_context()
    if context not in figures.keys():
        figures[context] = Figure(name, width, memory_enabled)

    return figures[context]

def imshow(img, width=30, memory_enabled=True):
    fig = figure(width=width, memory_enabled=memory_enabled)
    fig.imshow(img)

def vidshow(vid, width=30, fps=10):
    fig = figure(width=width, memory_enabled=False)
    fig.vidshow(vid, fps)

def repeat(shape=None, fps=10):
    fig = figure()
    fig.repeat(shape, fps)

def get_current_context():
    for frame in inspect.stack():
        if "ipython-input" in frame.filename:
            return frame.filename
    
    return None

def figshow(fig, width=30):
    canvas = FigureCanvas(fig)
    canvas.draw()

    fig_width, fig_height = (fig.get_size_inches() * fig.get_dpi()).astype(np.int32)
    image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8').reshape(fig_height, fig_width, 3)
    imshow(image, width)