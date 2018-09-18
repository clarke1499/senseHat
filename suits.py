from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.clear(255, 255, 255)
sleep(0.5)
sense.clear(255, 0, 0)
sleep(0.5)
sense.clear(0, 255, 0)
sleep(0.5)
sense.clear(0, 0, 255)
sleep(0.5)
sense.clear()
r = (255, 0, 0)
b = (0, 0, 0)
w = (255, 255, 255)

heart = [
w, r, w, w, w, w, r, w,
r, r, r, w, w, r, r, r,
r, r, r, r, r, r, r, r,
r, r, r, r, r, r, r, r,
w, r, r, r, r, r, r, w,
w, r, r, r, r, r, r, w,
w, w, r, r, r, r, w, w,
w, w, w, r, r, w, w, w
]

club = [
w, w, w, b, b, w, w, w,
w, w, b, b, b, b, w, w,
w, w, w, b, b, w, w, w,
w, b, b, b, b, b, b, w,
b, b, b, b, b, b, b, b,
w, b, w, b, b, w, b, w, 
w, w, w, b, b, w, w, w,
w, b, b, b, b, b, b, w
]

diamond = [
w, w, w, r, r, w, w, w,
w, w, r, r, r, r, w, w,
w, r, r, r, r, r, r, w,
r, r, r, r, r, r, r, r,
r, r, r, r, r, r, r, r,
w, r, r, r, r, r, r, w,
w, w, r, r, r, r, w, w,
w, w, w, r, r, w, w, w
]

spade = [
w, w, w, b, b, w, w, w,
w, w, b, b, b, b, w, w,
w, b, b, b, b, b, b, w,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
w, b, w, b, b, w, b, w,
w, w, b, b, b, b, w, w
]

def show_heart():
  sense.set_pixels(heart)

def show_club():
  sense.set_pixels(club)

def show_diamond():
  sense.set_pixels(diamond)

def show_spade():
  sense.set_pixels(spade)

def choose_suit(event):
  if event.action == 'pressed':
    suit = random.randint(0, 100)
    if suit < 25:
      sense.clear()
      show_heart()
    elif suit < 50:
      sense.clear()
      show_club()
    elif suit < 75:
      sense.clear()
      show_diamond()
    elif suit < 100:
      sense.clear()
      show_spade()

while True:
  event = sense.stick.wait_for_event()
  choose_suit(event)
  

