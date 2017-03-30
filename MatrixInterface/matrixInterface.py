import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)

while(True):
    spi.xfer([0x01, 0x02])
    time.sleep(0.1)
    spi.xfer([0x01, 0x00])
    time.sleep(0.1)
    spi.xfer([0x01, 0x00])
    time.sleep(0.1)
    spi.xfer([0x01, 0x00])
    time.sleep(0.1)
