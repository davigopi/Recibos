from time import sleep
import pyautogui
from PIL.Image import Image


class ImageManip:
  def __init__(self, img: Image) -> None:
    self.img: Image = img

  @property
  def images(self):
    return self.img

  @images.setter
  def images(self, img):
    self.img = img

  @property
  def clickImg(self):
    similariyImg = 1
    waitImg = 0.9
    while True:
      try:
        # Instalar 'pip install opencv-python'
        x, y = pyautogui.locateCenterOnScreen(
            self.img,
            confidence=similariyImg
        )
        pyautogui.click(x, y)
      except Exception:
        similariyImg -= 0.01
        if similariyImg <= waitImg:
          sleep(1)
          waitImg -= 0.1
          if waitImg <= 0.6:
            similariyImg = 1
            waitImg = 0.9
