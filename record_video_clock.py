"""
Script for recording clock animation and saving to gif
"""
import numpy as np
import cv2
from mss import mss
from PIL import Image

# hardcoded for my monitor and vscode setup
bounding_box = {"top": 857, "left": 102, "width": 23, "height": 23}

with mss() as sct:
    images = []
    while True:
        sct_img = sct.grab(bounding_box)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        images.append(img)

        cv2.imshow("screen", np.array(sct_img))
        if cv2.waitKey(25) & 0xFF == ord("q"):
            images[0].save("clock.gif", save_all=True, append_images=images[1:], duration=50, loop=0)
            cv2.destroyAllWindows()
            break
