import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

font = pygame.font.SysFont('Garamond', 100)

blue = pygame.Color(0,0,255)
red = pygame.Color(255,0,0)

text = font.render('Ejike', True, red)

screen.fill(blue)
screen.blit(text, (0, 0))
pygame.display.flip()

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        print(event)
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
