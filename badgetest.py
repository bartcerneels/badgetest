# HW test for the Fri3dcamp badge

import uasyncio

import os

from neopixels import *

async def cycle_neopixels():
    cycle = 0
    while True:
        cycle = (cycle + 1)
        # print("cycle {}".format(cycle))
        for i in range(0, len(neopixels)):
            pixel = (cycle+i)%len(neopixels)
            # print("pixel {}".format(pixel))
            if (i == 0):
                # print("i == 0")
                neopixels[pixel] = (255,255,255)
            neopixels[pixel] = (10,10,10)
        neopixels.write()

        await uasyncio.sleep_ms(800)

uasyncio.run(cycle_neopixels())
