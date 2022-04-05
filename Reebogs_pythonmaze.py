def turn_right():
    turn_left()
    turn_left()
    turn_left()


   
while at_goal() != True:
    if right_is_clear():
        turn_right()
    while  wall_on_right() and front_is_clear():
         move()
    if not front_is_clear() and wall_on_right():
        turn_left()
    if front_is_clear():
        move()
   
    
       
       
  
   
    


