# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((128,0,0))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (25,25,112), (250,250), 150)
    pygame.draw.circle(screen, (135,206,250), (250,250), 100)
    pygame.draw.circle(screen, (92 ,58,147), (250,250), 60)
    pygame.draw.circle(screen, (0,0,0), (250,250), 8)
   
    pygame.draw.circle(screen, (250,240,230), (300,290), 25)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()