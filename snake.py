#!/usr/bin/env python3
from sense_hat import SenseHat
import random
from enum import Enum, auto

sense = SenseHat()
sense.clear()
white = (255, 255, 255)
blank = (0, 0, 0)

class Direction(Enum):
  UP = auto()
  DOWN = auto()
  RIGHT = auto()
  LEFT = auto()

sense.set_pixel(random.randint(0, 7), random.randint(0, 7), white)

def pushed_down(event):
  if event.action == 'pressed':
    pixel_list = sense.get_pixels()
    pixel_number = 0
    for pixel in pixel_list:
      if pixel != [0, 0, 0]:
        pixel_y_x = divmod(pixel_number, 8)
        if pixel_y_x[0] == 7:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(pixel_y_x[1], 0, white)
        else:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0] + 1, white)
      else:
        pixel_number += 1

def pushed_up(event):
  if event.action == 'pressed':
    pixel_list = sense.get_pixels()
    pixel_number = 0
    for pixel in pixel_list:
      if pixel != [0, 0, 0]:
        pixel_y_x = divmod(pixel_number, 8)
        if pixel_y_x[0] == 0:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(pixel_y_x[1], 7, white)
        else:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0] - 1, white)
      else:
        pixel_number += 1
    
def pushed_right(event):
  if event.action == 'pressed':
    pixel_list = sense.get_pixels()
    pixel_number = 0
    for pixel in pixel_list:
      if pixel != [0, 0, 0]:
        pixel_y_x = divmod(pixel_number, 8)
        if pixel_y_x[1] == 7:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(0, pixel_y_x[0], white)
        else:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(pixel_y_x[1] + 1, pixel_y_x[0], white)
      else:
        pixel_number += 1

def pushed_left(event):
  if event.action == 'pressed':
    pixel_list = sense.get_pixels()
    pixel_number = 0
    for pixel in pixel_list:
      if pixel != [0, 0, 0]:
        pixel_y_x = divmod(pixel_number, 8)
        if pixel_y_x[1] == 0:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(7, pixel_y_x[0], white)
        else:
          sense.set_pixel(pixel_y_x[1], pixel_y_x[0], blank)
          sense.set_pixel(pixel_y_x[1] - 1, pixel_y_x[0], white)
      else:
        pixel_number += 1

#sense.stick.direction_down = pushed_down

while True:
  event = sense.stick.wait_for_event()
  if event.direction == 'down':
    direction = Direction.DOWN
  elif event.direction == 'right':
    direction = Direction.RIGHT
  elif event.direction == 'left':
    direction = Direction.LEFT
  elif event.direction == 'up':
    direction = Direction.UP
