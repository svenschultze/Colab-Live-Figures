from google.colab.output._js_builder import Js

listen = Js(f"""
    function(channel, width) {{
        elem = document.createElement("img")
        elem.style.imageRendering = "pixelated"
        elem.style.width = width + "%"
        elem.style.float = "left"
        output = google.colab.output.getActiveOutputArea()
        output.appendChild(elem)
        new BroadcastChannel('test').onmessage = (msg) => {{
            elem.src = msg.data
        }}
    }}
""")

broadcast = Js(f"""
    function(channel, msg) {{
        new BroadcastChannel(channel).postMessage(msg)
    }}
""")