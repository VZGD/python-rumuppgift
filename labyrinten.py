import time


# Entrance method
def entrance():
    print("You have entered the entrance room")
    time.sleep(1)
    print("What do you want to do?")
    time.sleep(1)
    print("There are 2 doors, a door to the living room and a room with a cold draft coming from it")
    time.sleep(1)
    answer = input(f"1) Go to the living room \n2) check out the cold draft \n3) Stay here\n")
    
    if int(answer) == 1:
        print("You approach the door and open it...")
        time.sleep(1)
        livingroom()

    elif int(answer) == 2:
        print("You go to open the door to the drafty room")
        time.sleep(1)
        drafty_room()

    elif int(answer) == 3:
        print("You have decided to stay..")
        time.sleep(1)
        entrance()

def livingroom():
    print("You have entered the living room")
    time.sleep(1)
    print("You see two doors")
    time.sleep(1)
    print("one in front, sunshine gleams through the window")
    time.sleep(1)
    print("the other is to your right and a cold draft can be felt")
    time.sleep(1)
    print("Where do you want to go?")
    time.sleep(1)
    ans = input(f"1) back to the previous room \n2) towards the sunshine \n3) check out the cold draft \n4) stay in the room\n")
    if(ans == "1"):
        entrance()
    elif(ans == "2"):
        print("you peek through the window")
        time.sleep(1)
        sunshine_room()
    elif(ans == "3"):
        print("the draft gets colder as you approach")
        time.sleep(1)
        drafty_room()
    elif(ans == "4"):
        print("You decide to stay..")
        time.sleep(1)
        livingroom()

def drafty_room():
    print("You have entered the drafty room")
    time.sleep(1)
    print("The drafty room is too cold and you are starting to freeze")
    time.sleep(1)
    print("There are 3 doors which one do you want to enter?")
    time.sleep(1)
    answere = input(f"1) Go to the entrance \n2) Go to the living room \n3) Go to the sunshine room \n4) Stay in the room\n")
    if(answere == "1"):
        print("You went to the entrance room")
        time.sleep(1)
        entrance()
    elif(answere == "2"):
        print("You went to the living room")
        time.sleep(1)
        livingroom()
    elif(answere == "3"):
        print("Go to the sunshine room")
        time.sleep(1)
        sunshine_room()
    elif(answere == "4"):
        print("You stay in the room and die")
        time.sleep(1)
        print("Game over, you died")

def sunshine_room():
    print("You have entered the sunshine room")
    time.sleep(1)
    print("It's very hot in here")
    time.sleep(1)
    print("There are 2 doors, what do you want to do?")
    time.sleep(1)
    answeer = input(f"1) You go to the living room \n2) You go to the drafty room \n3) You stay in the room\n")
    if(answeer == "1"):
        print("You went to the living room")
        livingroom()
    elif(answeer == "2"):
        print("You went to the drafty room")
        time.sleep(1)
        drafty_room()
    elif(answeer == "3"):
        print("You decided to stay in the sunshine room")
        time.sleep(1)
        sunshine_room()

    

# This runs first
print("Welcome to the maze")
entrance()