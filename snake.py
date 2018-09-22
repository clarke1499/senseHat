#!/usr/bin/env python
from sense_hat import SenseHat
import random
import time

sense = SenseHat()
sense.clear()
white = (255, 255, 255)
blank = (0, 0, 0)
red = (255, 0, 0)
get_red = [248, 0, 0]
length = 2
direction = -1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def opposite(directionOpp):
  if directionOpp == UP:
    return DOWN
  elif directionOpp == DOWN:
    return UP
  elif directionOpp == LEFT:
    return RIGHT
  elif directionOpp == RIGHT:
    return LEFT

def xDelta(coord):
  if direction == RIGHT:
    if coord == 7:
      return 0
    return coord + 1
  elif direction == LEFT:
    if coord == 0:
      return 7
    return coord - 1
  return coord

def yDelta(coord):
  if direction == UP:
    if coord == 0:
      return 7
    return coord - 1
  elif direction == DOWN:
    if coord == 7:
      return 0
    return coord + 1
  return coord

def move():
  pixel_list = sense.get_pixels()
  pixel_number = 0
  for pixel in pixel_list:
    if pixel == get_red:
      pixel_y_x = divmod(pixel_number, 8)
      #if pixel_y_x[0] == 7:
      #  sense.set_pixel(pixel_y_x[1], pixel_y_x[0], white)
      #  sense.set_pixel(pixel_y_x[1], 0, red)
      #else:
      sense.set_pixel(pixel_y_x[1], pixel_y_x[0], white)
      print direction
      sense.set_pixel(xDelta(pixel_y_x[1]), yDelta(pixel_y_x[0]), red)
    else:
      pixel_number += 1

def move_up():
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

def move_right():
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

def move_left():
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

def change_direction(event):
  if event.action == 'pressed':
    print event
    if event.direction == 'up':
      direction = UP
    elif event.direction == 'down':
      direction = DOWN
    elif event.direction == 'left':
      direction = LEFT
    elif event.direction == 'right':
      direction = RIGHT

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

sense.stick.direction_any = change_direction

while True:
  time.sleep(0.25)
  move()
#  if direction == 0:
#    move_up()
#  elif direction == 1:
#    move_right()
#  elif direction == 2:
#    move_down()
#  elif direction == 3:
#    move_left()
