import pygame
import random

# Initialize pygame
pygame.init()

# Set up basic pygame window
window = pygame.display.set_mode((600, 400))  # window width and height
pygame.display.set_caption("Game")

# A variable to track whether the game is running
game_loop = True

# A list to store circle data
circles = []

# Defining custom colors
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]  # list of possible colors

# Main loop
while game_loop:
    # Event handling (i.e., user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False  # if "x" is clicked, close window

    # If last circle has shrunken and disappeared, create a new circle
    if len(circles) == 0 or circles[-1]['radius'] <= 5:
        # Randomize circle parameters and append to circles list
        circles.append({
            'x': random.randrange(window.get_width()),
            'y': random.randrange(window.get_height()),
            'radius': 60,
            'color': random.choice(COLORS),
        })

    # Update circles
    for i, circle in enumerate(circles):
        circle['radius'] -= 1  # reduce circle radius by timer_tick
        if circle['radius'] <= 0:
            del circles[i]  # remove circle if it shrank to nothing

    # Draw circles
    window.fill((0, 0, 0))  # fill screen with black
    for circle in circles:
        pygame.draw.circle(window, circle['color'], (circle['x'], circle['y']), circle['radius'])
    pygame.display.flip()  # update pygame window

pygame.quit()  # end game
