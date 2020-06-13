def serial():
    global serial
    global last
    serial = input ('What is the serial number?\n')
    last = serial[-1]
    
def wire_solve():
    global wires
    wires = input ("Please input the wires?\n")
    s = wires
    parts = s.split(" ")

    n = len(parts)
    print (n)
    print (parts)
    blue = parts.count("b") #count the numeber of blue wires
    red = parts.count("r") #count the number of red wires
    yellow = parts.count("y") #count the number of yellow wwires
    black = parts.count("k") #count the number of black wires
    white = parts.count("w") #count the number of white wires

    if n == 3: #3 wires
        if 'r' not in parts:
            print("Cut the 2nd wire")
        elif parts[-1] == "w":
                print("Cut the last Wire")
        elif blue > 1:
            print( "Cut the last blue wire")
        else:
            print("cut the Last Wire")

    if n == 4: # 4 wires
        if red > 1 and int(last) % 2 == 1:
            print ("Cut the last Red Wire.")
        elif parts[-1] == "y" and red == 0:
            print ("Cut the 1st Wire")
        elif blue ==1:
            print("cut the 1st wire")
        elif yellow > 1:
            print("Cut the Last Wire.")
        else:
            print("Cut the 2nd Wire.")
                
    if n == 5: #five wires
        if parts[-1] == 'k'and int(last) % 2 == 1: #odd)
            print ("Cut the 4th Wire.")
        elif red == 1 and yellow > 1:
            print ("Cut the 1st Wire.")
        elif black == 0:
            print ("Cut the 2nd Wire.")
        else:
            print ("cut the 1st wire")         
            
    if n == 6: # six wires
        if yellow ==0 and int(last) % 2 == 1: #odd
            print("cut the 3rd wire")
        elif yellow == 1 and white > 1:
            print ("Cut the 4th wire")
        elif red == 0:
            print ("cut the Last Wire")
        else:
            print ("Cut the 4th Wire")
            
serial()


while True:
    wire_solve()
    if wires== "exit":
        break
#Authored by DerrickGnC and ChucklesTheBeard
#Live on Twitch Twitch.tv/DerrickGnC 06/12/2020
