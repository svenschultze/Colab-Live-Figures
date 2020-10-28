# Colab-Live-Figures
Simple library to display live-updating images in Google Colaboratory

## Installation
```bash
!pip install -q git+https://github.com/svenschultze/Colab-Live-Figures
```

## Usage
```python
import live
```
### Create figure manually
To create new figure:
```python
fig = live.Figure(width=40) # 40% width
```

To update the figure:
```python
fig.imshow(img)
```

Matplotlib integration:
```python
fig.figshow(pyplot_figure)
```

### Create figure automatically
```python
live.imshow(img)
```

Matplotlib integration:
```python
live.figshow(pyplot_figure)
```

## Examples
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/svenschultze/Colab-Live-Figures/blob/main/demo/demo.ipynb)

```python
import live
import time
import numpy as np

for i in range(5):
    img = np.random.randint(0, 255, (15, 15, 3))
    live.imshow(img)
    time.sleep(.5)
```

<img width="30%" src="https://github.com/svenschultze/Colab-Live-Figures/blob/main/demo/demo.gif?raw=true"/>

```python
import live
import time
import numpy as np
import matplotlib.pyplot as plt

for i in range(10):
    x, y = np.random.randint(0, 100, (2, 100))

    fig = plt.Figure(dpi=200)
    ax = fig.gca()
    ax.scatter(x, y)

    live.figshow(fig)
    time.sleep(.5)
```

<img width="40%" src="https://github.com/svenschultze/Colab-Live-Figures/blob/main/demo/matplotlib.gif?raw=true"/>

```python
import live
import time
from skimage import io
import cv2
img = io.imread("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/757px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg")

for i in range(1, 21, 2):
    blurred = cv2.GaussianBlur(img, (i, i), 0)
    live.imshow(blurred)
    time.sleep(.5)
```

<img width="40%" src="https://github.com/svenschultze/Colab-Live-Figures/blob/main/demo/blur.gif?raw=true"/>
