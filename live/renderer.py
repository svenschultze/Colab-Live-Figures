from google.colab.output._js_builder import Js

listen = Js("""
    function(channel, width) {
        let elem = document.createElement("img")
        elem.style.imageRendering = "pixelated"
        elem.style.width = width + "%"
        elem.style.float = "left"
        elem.style.margin = "5px"
        let output = google.colab.output.getActiveOutputArea()
        output.appendChild(elem)
        new BroadcastChannel(channel).onmessage = (msg) => {
            elem.src = msg.data
        }
    }
""")

broadcast = Js("""
    function(channel, msg) {
        new BroadcastChannel(channel).postMessage(msg)
    }
""")