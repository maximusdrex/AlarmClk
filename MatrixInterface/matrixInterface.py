import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)
spi.lsbfirst = False
spi.xfer([0x0C, 0x01])
spi.xfer([0x0B, 0xFF])

while(True):
  for i in range(60):
    spi.xfer([0x01, 0])
    spi.xfer([0x01, 0])
    spi.xfer([0x01, 0])
    spi.xfer([0x01, i])
    print(i)
    time.sleep(1)

