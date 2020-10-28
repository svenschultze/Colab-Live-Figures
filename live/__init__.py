import pkgutil
from IPython.display import display, Javascript

from live.figure import Figure


broadcast_template = pkgutil.get_data(__name__, "templates/broadcast.js").decode("utf-8")

def broadcast(channel, message):
    js = broadcast_template.replace(
        "{CHANNEL}", channel
    ).replace(
        "{MESSAGE}", message
    )

    display(Javascript(js))

