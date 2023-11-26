import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
width = 800
height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Paddle dimensions
paddle_width = 100
paddle_height = 10

# Ball dimensions and speed
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")

clock = pygame.time.Clock()

# Create the paddle
paddle_x = (width - paddle_width) // 2
paddle_y = height - 50

# Create the ball
ball_x = width // 2
ball_y = height // 2

# Direction of the ball
ball_dx = ball_speed_x
ball_dy = -ball_speed_y

# Create bricks
brick_width = 80
brick_height = 20
brick_rows = 5
brick_cols = width // (brick_width + 10)

bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + 10) + 50
        brick_y = row * (brick_height + 10) + 50
        brick_color = random.choice([blue, red, green, yellow])
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    paddle_x = pygame.mouse.get_pos()[0] - paddle_width // 2

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Collisions with the walls
    if ball_x <= 0 or ball_x >= width - ball_radius:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    # Collisions with the paddle
    if ball_y >= paddle_y - ball_radius and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy *= -1

    # Collisions with the bricks
    for brick in bricks:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy *= -1
            break

    # Game over
    if ball_y >= height:
        running = False

    # Clear the window
    window.fill(black)

    # Draw the paddle
    pygame.draw.rect(window, white, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(window, white, (ball_x, ball_y), ball_radius)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(window, brick_color, brick)

    # Update the window
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
