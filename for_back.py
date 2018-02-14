import pygame

pygame.init()
pygame.joystick.init() 

joy = pygame.joystick.Joystick(0)
joy.init()

axis_down = 1
axis_right = 2

while True:
    pygame.event.pump()
    if -1.0 <= joy.get_axis(axis_down) <= -0.5:
        print("Move Forward ", end='')
    elif 0.5 <= joy.get_axis(axis_down) <= 1.0:
        print("Move Backward ", end='')
    elif -0.5 < joy.get_axis(axis_down) < 0.5:
        print("Stagnant f/b ", end='')

    if -1.0 <= joy.get_axis(axis_right) <= -0.5:
        print("Move Left")
    elif 0.5 <= joy.get_axis(axis_right) <= 1.0:
        print("Move Rught")
    elif -0.5 < joy.get_axis(axis_right) < 0.5:
        print("Stagnant R/L")
