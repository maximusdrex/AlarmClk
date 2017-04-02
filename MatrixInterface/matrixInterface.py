import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)
spi.lsbfirst = False
spi.xfer([0x0C, 0x01])
spi.xfer([0x0B, 0xFF])

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

