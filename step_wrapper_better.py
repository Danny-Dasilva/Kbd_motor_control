from step.API import GrblComm

import keyboard

class Step:

    def __init__(self, binsPerlevel, levels):
        #Initialize variables
        self.comm = GrblComm("/dev/ttyUSB0", 250000,  True)
        self.existingBinPositions = {}
        self.binsPerlevel = binsPerlevel
        self.levelNames = {0:"X",1:"Y",2:"Z",3:"E0",4:"E1"}
        self.levels = levels
    def set_angle(self, binName):
        if binName not in self.existingBinPositions:
            currenlevel = len(self.existingBinPositions)//self.binsPerlevel
            binPosition = len(self.existingBinPositions)-(10*currenlevel)
            if not currenlevel > self.levels-1:
                self.existingBinPositions[binName] = [self.levelNames.get(currenlevel),binPosition/self.binsPerlevel]
            else:
                print("Not enough bins")

        self.comm.rapidMovement(str(self.existingBinPositions.get(binName)[0]) + str(self.existingBinPositions.get(binName)[1]) + " F4")
        print(str(self.existingBinPositions.get(binName)))
        # ADD IN sleep ??
    def angle_gen(self, length):
        angle = 360 / length
        return(angle)


values = {1 : "q", 2 : "w", 3 : "e", 4: "r", 5: "t"}



step = Step(10,1)
for i in "zxcvbnmlkj":
        step.set_angle(i)
while True:
    for key, value in values.items():
        if keyboard.is_pressed(value):
            print(value, "is pressed")
            step.set_angle(value)

    if keyboard.read_key() == "p":
        print("You pressed p")
        step.comm.closeSer()
        break
# step.comm.closeSer()