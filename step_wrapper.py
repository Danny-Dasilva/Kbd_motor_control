from step.API import GrblComm

import keyboard

class Step:

    def __init__(self):
        #Initialize variables
        self.comm = GrblComm("/dev/ttyUSB0", 250000,  True)
        self.angle = 4
    def set_angle(self, input_ang):

        self.angle = (input_ang/360)
        self.comm.rapidMovement("X" + str(self.angle) + " F4")
        print(str(self.angle))
        # ADD IN sleep ??



values = {1 : "q", 2 : "w", 3 : "e", 4: "r", 5: "t"}


def angle_gen(length):
    angle = 360 / length
    return(angle)

step = Step()

while True:
    
    for key, value in values.items():
        if keyboard.is_pressed(value):
            
            mult = angle_gen(len(values))
            print(mult)
            angle = key * mult
            print(angle, "is pressed")
            step.set_angle(angle)
    if keyboard.read_key() == "p":
        print("You pressed p")
        step.comm.closeSer()
        break
# step.comm.closeSer()