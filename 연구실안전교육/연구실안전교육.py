from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

import time
import pyautogui as pg
# pg.FAILSAFE=False
# pg.mouseInfo()
# quit()
# x,y=pg.locateCenterOnScreen("Next.png")
while True:
    CurrentPos=pg.position()
    pg.doubleClick(x=1452, y=-418)
    pg.click(x=CurrentPos.x, y=CurrentPos.y)
    print("Clicked!")
    print("Sleeping for a minute...\n")
    time.sleep(60)
    