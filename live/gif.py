import ffmpeg
import cv2
import uuid
import os
import base64
import numpy as np

def save_video_to_file(file, vid, fps):
    writer = cv2.VideoWriter(file.name,  cv2.VideoWriter_fourcc('M','J','P','G'), fps, vid.shape[1:3])
    for img in vid:
        writer.write(np.flip(img, axis=2))
    writer.release()

def convert(input, output):
    ffmpeg.input(input).output(output).run()

def video_to_gif(vid, fps=10):
    filename = uuid.uuid4()

    with open(f"/tmp/{filename}.avi", "w") as avi:
        save_video_to_file(avi, vid, fps)

    ffmpeg.input(f"/tmp/{filename}.avi").output(f"/tmp/{filename}.gif").run()

    with open(f"/tmp/{filename}.gif", "rb") as image_file:
        gif_b64 = base64.b64encode(image_file.read()).decode("utf-8")

    os.remove(f"/tmp/{filename}.avi")
    os.remove(f"/tmp/{filename}.gif")

    return gif_b64