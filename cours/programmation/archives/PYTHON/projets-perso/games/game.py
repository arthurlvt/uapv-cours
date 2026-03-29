import pygame
import random
from bird import Bird
from pipe import Pipe

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the game clock
clock = pygame.time.Clock()

# Load the background image
background = pygame.image.load("background.png")

# Load the font
font = pygame.font.Font("04B_19.ttf", 36)

# Define the score
score = 0

# Create the bird and pipes
bird = Bird(50, 200)
pipes = [Pipe(SCREEN_WIDTH + i * 150) for i in range(3)]

# Create the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Move the bird and pipes
    bird.update()
    for pipe in pipes:
        pipe.update()

        # Check for collision with pipes
        if bird.rect.colliderect(pipe.rect_top) or bird.rect.colliderect(pipe.rect_bottom):
            running = False

        # Increment the score if the bird passes a pipe
        if pipe.rect_top.right < bird.rect.left and not pipe.top_passed:
            pipe.top_passed = True
            score += 1
        if pipe.rect_bottom.right < bird.rect.left and not pipe.bottom_passed:
            pipe.bottom_passed = True
            score += 1

        # Remove the pipes that have gone off screen
        if pipe.rect_top.right < 0:
            pipes.remove(pipe)
            pipes.append(Pipe(pipes[-1].rect_top.right + 150))

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the bird
    bird.draw(screen)

    # Draw the pipes
    for pipe in pipes:
        pipe.draw(screen)

    # Draw the score
    score_text = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 50))

    # Update the display
    pygame.display.update()

    # Set the game clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
