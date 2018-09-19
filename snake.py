#!/usr/bin/env python
from sense_hat import SenseHat
import random

sense = SenseHat()
sense.clear()
white = (255, 255, 255)
blank = (0, 0, 0)
red = (255, 0, 0)


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def xDelta(coord, direction):
  if direction == RIGHT:
    return coord + 1
  elif direction == LEFT:
    return coord - 1
  return coord
  
def yDelta(coord, direction):
  if direction == UP:
    return coord - 1
  elif direction == DOWN:
    return coord + 1
  return coord

corner = random.randint(0, 3)
if corner == 0:
  sense.set_pixel(0, 0, white)
  direction = random.randint(1, 2)
  sense.set_pixel(xDelta(0, direction), yDelta(0, direction), red)
elif corner == 1:
  sense.set_pixel(0, 7, white)
  direction = random.randint(0, 1)
  sense.set_pixel(xDelta(0, direction), yDelta(7, direction), red)
elif corner == 2:
  sense.set_pixel(7, 0, white)
  direction = random.randint(2, 3)
  sense.set_pixel(xDelta(7, direction), yDelta(0, direction), red)
elif corner == 3:
  sense.set_pixel(7, 7, white)
  direction = random.randint(0, 1)
  if direction == 1:
    direction = 3
  sense.set_pixel(xDelta(7, direction), yDelta(7, direction), red)

def move_down(event):
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

def move_up(event):
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
    
def move_right(event):
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

def move_left(event):
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

sense.stick.direction_any = change_direction

while True:
  
