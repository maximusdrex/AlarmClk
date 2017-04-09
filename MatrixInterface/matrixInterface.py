import spidev
import time
from time import strftime
spi = spidev.SpiDev()
spi.open(0, 0)
spi.lsbfirst = False
spi.xfer([0x0C, 0x01])
spi.xfer([0x0B, 0xFF])

NUM_MATRICES = 4
NO_OP = [0, 0]

def sendBytes(adress, data):
    spi.xfer2([adress, data])

def sendByteList(datalist):
    spi.xfer2(datalist)

def sendToMatrix(matrix, adress, data):
    sendByteList(NO_OP*(NUM_MATRICES - matrix) + [adress, data] + NO_OP*(matrix-1))

def clearScreen():
    spi.xfer([0x0F, 0x00])
    spi.xfer([0x0F, 0x00])
    spi.xfer([0x0F, 0x00])
    spi.xfer([0x0F, 0x00])
    for i in range(4):
        for j in range(9):
            spi.xfer([j , 0x00])

#clear before running
clearScreen()

def binaryStopwatch():
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
                for k in range(60):
                    spi.xfer([0x01, 0])
                    spi.xfer([0x01, 0])
                    spi.xfer([0x01, 0])
                    spi.xfer([0x01, k])
                    print("hr: " + str(i) + "; min: " + str(j) + "; sec: " + str(k))
                    time.sleep(1)

def binaryClock():
    while(True):
      spi.xfer([0x03, 0])
      spi.xfer([0x03, 0])
      spi.xfer([0x03, 0])
      spi.xfer([0x03, int(strftime('%H'))])
      spi.xfer([0x02, 0])
      spi.xfer([0x02, 0])
      spi.xfer([0x02, 0])
      spi.xfer([0x02, int(strftime('%M'))])
      spi.xfer([0x01, 0])
      spi.xfer([0x01, 0])
      spi.xfer([0x01, 0])
      spi.xfer([0x01, int(strftime('%S'))])
      print(strftime('%H:%M:%S'))
      time.sleep(1)

sendToMatrix(2, 0x01, 0x0F)
sendToMatrix(4, 0x01, 0x05)