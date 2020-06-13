def label ():
    global label
    label = input("What does the button say\n")

def batteries ():
    global battery
    battery = input("How Many Batteries are there?\n")
    
def indicator ():
    global indicator
    global parts
    indicator = input("Lit up Labels?\n")
    s = indicator
    parts = s.split (" ")

def color ():
    global color
    color = input("What color is the button?\n")

def c(): #check batteries
    if int(battery)>2 and indicator == "frk":
            print ("Press and Release")
    else:
        print ("Press and Hold.\n If Blue:4\n if Yellow:5\n if Other:1")

def h(): #hold and refer
    print ("Press and Hold.\n If Blue:4\n if Yellow:5\n if Other:1")
    
def p(): #Press and Release
    print("Press & Release")
    
def button_solve():
    global color
    color = input("What color is the button?\n")
    global label
    label = input("What does the button say\n")
    
    if int(battery) > 1 and label == "det":
        p()
    elif int(battery) <= 1 and label =="det":
        h()
    elif color == "r" and label == "abo":
        c()
    elif color == "r" and label =="hold":
        p()
    elif color == "r" and label =="press":
        c()
    elif color == "b" and label =="abo":
        h()
    elif color == "b" and label =="hold":
        c()
    elif color == "b" and label =="Press":
        c()
    elif color == "w" and "car" in parts and label == "abo":
        h()
    elif color == "w" and "car" in parts and label == "hold":
        h()
    elif color == "w" and "car" in parts and label == "press":
        h()
    elif color == "y" and label == "abo":
        c()
    elif color == "y" and label == "hold" or label == "press":
        c()
    elif color == "b" or color == "w" and "car" not in parts and label == "abo" or label == "hold" or label == "press":
        c()


batteries()
indicator()

while True:
    button_solve()
    again = input("Would you like to restart\n")
    if again == "n":
        exit()
        
#authored by DerrickGnC
#Watch me live twitch.tv/derrickGnC
