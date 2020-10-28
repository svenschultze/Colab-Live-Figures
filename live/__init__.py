import pkgutil
from IPython.display import display, Javascript
import inspect

from live.figure import Figure


broadcast_template = pkgutil.get_data(__name__, "templates/broadcast.js").decode("utf-8")

figures = {}

def figure(name=None, width=30):
    context = get_current_context()
    if context not in figures.keys():
        figures[context] = Figure(name, width)

    return figures[context]

def imshow(img, width=30):
    fig = figure(width=width)
    fig.imshow(img)

def get_current_context():
    for frame in inspect.stack():
        if "ipython-input" in frame.filename:
            return frame.filename
    
    return None

def broadcast(channel, message):
    js = broadcast_template.replace(
        "{CHANNEL}", channel
    ).replace(
        "{MESSAGE}", message
    )

    display(Javascript(js))