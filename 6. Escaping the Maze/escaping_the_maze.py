# This code is implemented for the mage game of the Reeborgs world site.
# go to the website, choose the maze problem and copy the code below and run it

# Level = Beginner

def turn_right():
    turn_left()
    turn_left()
    turn_left()
t = 0    
while not at_goal():
    if right_is_clear(): 
        turn_right()
        t+=1
        print(t)
        if t >= 4:
            if front_is_clear():
                t = 0
                move()
        if front_is_clear():
            move()
            
    elif front_is_clear():
        move()
        t =0
    else:
        turn_left()
        t = 0