import board
import neopixel
import time
import sys

NUM = 8
OFF = (0,0,0)
RED = (10,0,0)
WHITE = (10,10,10)

# must be 10, 12, 18, or 21
PINS = {
#        '10': board.D10,
        '12': board.D12,
        '18': board.D18,
        '21': board.D21
        }
key = '12'
if len(sys.argv) > 1:
  key = sys.argv[1]

PIN = PINS.get(key)
print("Neopixel pin " + key)

pixels = neopixel.NeoPixel(PIN, NUM, brightness=0.9)
i = 0
while True:
  pixels.fill(OFF)
  if i < NUM - 1:
    pixels[i] = WHITE
  
  i += 1
  if i >= NUM:
    i = 0

  pixels.show()
  time.sleep(1)

