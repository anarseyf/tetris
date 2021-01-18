#!/usr/bin/env python3

import board
import neopixel
import time
import sys

NUM = 8
OFF = (0,0,0)
RED = (8,0,0)
WHITE = (5,5,5)

# must be 10, 12, 18, or 21
key = '12'
PIN = board.D12
print("Neopixel pin " + key)

pixels = neopixel.NeoPixel(PIN, NUM, brightness=0.9)
i = 0
while True:
  pixels.fill(OFF)
  if i < NUM - 1:
    pixels[i] = WHITE
  elif i == NUM - 1:
    pixels.fill(RED)

  i += 1
  if i >= NUM:
    i = 0

  pixels.show()
  time.sleep(0.1)

