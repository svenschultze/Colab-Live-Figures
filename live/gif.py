import ffmpeg
import cv2
import uuid
import os
import base64

def save_video_to_file(file, vid):
    writer = cv2.VideoWriter(file.name,  cv2.VideoWriter_fourcc('M','J','P','G'), 10, (15, 15))
    for img in vid:
        writer.write(img)
    writer.release()

def convert(input, output):
    ffmpeg.input(input).output(output).run()

def video_to_gif(vid):
    filename = uuid.uuid4()

    with open(f"/tmp/{filename}.avi", "w") as avi:
        save_video_to_file(avi, vid)

    ffmpeg.input(f"/tmp/{filename}.avi").output(f"/tmp/{filename}.gif").run()

    with open(f"/tmp/{filename}.gif", "rb") as image_file:
        gif_b64 = base64.b64encode(image_file.read()).decode("utf-8")

    os.remove(f"/tmp/{filename}.avi")
    os.remove(f"/tmp/{filename}.gif")

    return gif_b64