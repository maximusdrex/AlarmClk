import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)

while(True):
    spi.xfer([0x0F, 0x01])
    time.sleep(0.1)
    spi.xfer([0x0F, 0x01])
    time.sleep(0.1)
    spi.xfer([0x0F, 0x00])
    time.sleep(0.1)
    spi.xfer([0x0F, 0x00])