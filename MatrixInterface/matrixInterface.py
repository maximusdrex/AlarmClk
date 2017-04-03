import spidev
import time
from time import strftime
spi = spidev.SpiDev()
spi.open(0, 0)
spi.lsbfirst = False
spi.xfer([0x0C, 0x01])
spi.xfer([0x0B, 0xFF])

def clearScreen():
  spi.xfer([0x0F, 0x00])
  spi.xfer([0x0F, 0x00])
  spi.xfer([0x0F, 0x00])
  spi.xfer([0x0F, 0x00])
  for i in range(4):
    for j in range(9):
      spi.xfer([j , 0x00])

clearScreen()

while(True):
  for i in range(24):
    spi.xfer([0x03, 0])
    spi.xfer([0x03, 0])
    spi.xfer([0x03, 0])
    spi.xfer([0x03, i])
    for j in range(60):
        spi.xfer([0x02, 0])
        spi.xfer([0x02, 0])
        spi.xfer([0x02, 0])
        spi.xfer([0x02, j])
        print(i)
        time.sleep(1)
        for k in range(60):
            spi.xfer([0x01, 0])
            spi.xfer([0x01, 0])
            spi.xfer([0x01, 0])
            spi.xfer([0x01, k])
            print("hr: " + str(i) + "; min: " + str(j) + "; sec: " + str(k))
            time.sleep(1)

