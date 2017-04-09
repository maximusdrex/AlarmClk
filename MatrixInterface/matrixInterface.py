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
    sendByteList([0x0F, 0x00]*4)
    for j in range(9):
        sendByteList([j , 0x00]*4)

#clear before running
clearScreen()


def binaryClock():
    while(True):
      sendToMatrix(1, 0x03, int(strftime('%H')))
      sendToMatrix(1, 0x02, int(strftime('%M')))
      sendToMatrix(1, 0x01, int(strftime('%S')))
      print(strftime('%H:%M:%S'))
      time.sleep(1)

binaryClock()