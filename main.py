from PIL import ImageGrab
import matplotlib.pyplot as plt
import numpy as np
import time
from pyautogui import press




time.sleep(6)
press('space')
while True:
    object = False
    # grab a the detect point of the screen and checks if obstacles are present
    img = img = ImageGrab.grab(bbox=((630,150,750,250)))
    img_array = np.array(img)
    if [172,172,172,255] in img_array[80,:].tolist() or [172,172,172,255] in img_array[85,:].tolist() or  [172,172,172,255] in img_array[70,:].tolist():
        press("space")

