import serial
import time

class GrblComm:

    def __init__(self, port, baud, debug):
        #Initialize variables
        self.port = port
        self.baud = baud
        self.buffSize = 100
        self.debug = debug

        #Connect to device running Grbl firmware
        if(self.debug):
            print("Connecting to Marlin")

        self.ser = serial.Serial(self.port, self.baud, timeout=0.1)
        self.recieveAllData()

        if(self.debug):
            print("Marlin device connected")

    def recieveAllData(self):
        time.sleep(1)
        while True:
            data = self.ser.read_until()
            if data == b'':
                break
            else:
                print(data)
    #Return the current baudrate
    def getBaud(self):
        if(self.debug):
            print("Baudrate is " + self.baud)
        return self.baud

    #Return the current USB port
    def getPort(self):
        if(self.debug):
            print("Baudrate is " + self.port)
        return self.port

    #Move device rapidly using G00 axis all move at max speed to position specified
    def rapidMovement(self,posStr):
        self.sendGCode('G0 ' + posStr)
        self.sendGCode("M400")

    #Move device in a line using G01 axis move at the proper speed so all stop movign at the same time
    def linearMovement(self,posStr):
        self.sendGCode('G1 ' + posStr)
        resp = self.ser.read(self.buffSize)
        if(self.debug):
            print(resp)

    #Inform Grbl G-Code commands will be sent in inches
    def useInches(self):
        self.sendGCode('G20')
        resp = self.ser.read(self.buffSize)
        if(self.debug):
            print(resp)

    #Inform Grbl G-Code commands will be sent in mm
    def useMM(self):
        self.sendGCode('G21')
        resp = self.ser.read(self.buffSize)
        if(self.debug):
            print(resp)

    #Move device to the set home position (Does not home device)
    def returnHome(self):
        self.sendGCode('G28')
        resp = self.ser.read(self.buffSize)
        if(self.debug):
            print(resp)

    #Send a G-Code command
    def sendGCode(self,cmd):
        if(self.debug):
            print(cmd)
        self.ser.write(str.encode(cmd + '\r\n'))
    # Send a G-Code command and read data
    def sendGCodeResp(self, cmd):
        if (self.debug):
            print(cmd)
        self.ser.write(str.encode(cmd + '\r\n'))
        self.recieveAllData()


    #Disconnect from device running Grbl firmware
    def closeSer(self):
        if(self.debug):
            print("Disconnceting from Marlin")
        self.ser.close()


comm = GrblComm("COM10", 250000,  True)
time.sleep(1)
comm.rapidMovement("X4 F4")
time.sleep(7)
comm.closeSer()
