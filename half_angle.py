##from step.API import GrblComm

import keyboard

class Step:

    def __init__(self):
        self.angle = 4
    def set_angle(self, input_ang):
        if input_ang:
            self.angle = 4 + (input_ang/360)
        #self.comm.rapidMovement("X" + str(self.angle) + " F4")
        print(str(self.angle))


current_degree = 0
def change(input_ang):
    global current_degree
    print(input_ang, "input")
    
    if current_degree != input_ang:
        change = 0 
        diff = (current_degree - input_ang)%360
        if diff < 0:
            change = 1
        elif diff == 0:
            change = 0
        else:
            change = -1
        if abs(diff) > 180:
            change = 0 - change
        current_degree += change
        if change == 0:
            print("return angle")
        print(current_degree, "current")
    else:
        print("return angle")
        print(current_degree, "current")


def change_angle(input_ang):
    pass
    




values = {1 : "q", 2 : "w", 3 : "e", 4: "r"}



def angle_gen(length):
    angle = 360 / length
    return(angle)
step = Step()
while True:
    
    for key, value in values.items():
        if keyboard.is_pressed(value):
            
            mult = angle_gen(len(values))
            angle = key * mult
            #print(angle, "is pressed")
            #step.set_angle(angle)
            change(angle)
    if keyboard.read_key() == "p":
        print("You pressed p")
        break