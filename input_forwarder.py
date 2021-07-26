import socket
import zlib
from time import sleep

#QEMU Communication Constants
QEMU_RC_HOST = "127.0.0.1"
QEMU_RC_PORT = 6942
QEMU_SENDING = 0xDEADBEEB

#QEMU GPIO Constants
QEMU_GPIO_SET = 0x100
QEMU_GPIO_CLEAR = 0x200
#QEMU ADC Constants
QEMU_ADC_SEND_DATA = 0x21000100
#QEMU TIMER Constants
QEMU_TIMER_CAPTURE = 0x11000100

qemuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

qemuSocket.connect((QEMU_RC_HOST, QEMU_RC_PORT))

#This should print some data if connection is established
print(qemuSocket.recv(10))

#You can change ADC number from this however there is only 1 ADC so it will be 0:
QEMU_ADC = ord('0')
#You can change ADC Channel number from this:
QEMU_ADC_CHANNEL = 2
#You can change ADC DATA from this:
QEMU_ADC_DATA = 0x100

#This message is for generating an ADC data for specific ADC Channel
qemuDataADCBuffer = bytearray()
qemuDataADCBuffer += (QEMU_SENDING).to_bytes(4,byteorder='big')
qemuDataADCBuffer += (QEMU_ADC_SEND_DATA).to_bytes(4,byteorder='big')
qemuDataADCBuffer += (QEMU_ADC).to_bytes(4,byteorder='big')
qemuDataADCBuffer += (QEMU_ADC_CHANNEL).to_bytes(4,byteorder='big')
qemuDataADCBuffer += (QEMU_ADC_DATA).to_bytes(4,byteorder='big')
qemuDataADCBuffer += (0).to_bytes(4,byteorder='big')
qemuDataADCBuffer += (0).to_bytes(4,byteorder='big')
qemuDataADCBuffer += (0).to_bytes(4,byteorder='big')

crcADCData = zlib.crc32(qemuDataADCBuffer)
crcADCDataBuffer = (crcADCData).to_bytes(4,byteorder='big')
qemuDataADCBuffer += crcADCDataBuffer

print(qemuDataADCBuffer)

##
qemuSocket.send(qemuDataADCBuffer)
##

#You can change TIMER number from this:
QEMU_TIMER = ord('3')
#You can change TIMER CAPTURE register CR0 or CR1:
QEMU_TIMER_CAPTURE_PIN = 1
#You can send Rising and Falling Edge to Capture Register:
QEMU_TIMER_CAPTURE_SEND_RISING_EDGE = 1
QEMU_TIMER_CAPTURE_SEND_FALLING_EDGE = 0

#This message is for generating rising edge message for Timer
qemuDataTimerBuffer001 = bytearray()
qemuDataTimerBuffer001 += (QEMU_SENDING).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += (QEMU_TIMER_CAPTURE).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += (QEMU_TIMER).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += (QEMU_TIMER_CAPTURE_PIN).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += (QEMU_TIMER_CAPTURE_SEND_RISING_EDGE).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += (0).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += (0).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += (0).to_bytes(4,byteorder='big')

crcTimerData001 = zlib.crc32(qemuDataTimerBuffer001)
crcTimerDataBuffer001 = (crcTimerData001).to_bytes(4,byteorder='big')
qemuDataTimerBuffer001 += crcTimerDataBuffer001

print(qemuDataTimerBuffer001)

#This message is for generating falling edge message for Timer
qemuDataTimerBuffer002 = bytearray()
qemuDataTimerBuffer002 += (QEMU_SENDING).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += (QEMU_TIMER_CAPTURE).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += (QEMU_TIMER).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += (QEMU_TIMER_CAPTURE_PIN).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += (QEMU_TIMER_CAPTURE_SEND_FALLING_EDGE).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += (0).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += (0).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += (0).to_bytes(4,byteorder='big')

crcTimerData002 = zlib.crc32(qemuDataTimerBuffer002)
crcTimerDataBuffer002 = (crcTimerData002).to_bytes(4,byteorder='big')
qemuDataTimerBuffer002 += crcTimerDataBuffer002

print(qemuDataTimerBuffer002)

#Send RPM message to QEMU for 1 minute
motorRPM = 30
for index in range(1*motorRPM):
    qemuSocket.send(qemuDataTimerBuffer001)
    sleep((60.0/motorRPM)/2)
    qemuSocket.send(qemuDataTimerBuffer002)
    sleep((60.0/motorRPM)/2)

#Send message to QEMU
qemuSocket.send(qemuDataBuffer)
qemuSocket.close()