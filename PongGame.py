import pygame, sys

def ball_movement():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # making the ball bounce
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # If the ball collides wth the Player and opponent
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    
def player_movement():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player_speed += 7
        if event.key == pygame.K_UP:
            player_speed -= 7

pygame.init()
clock = pygame.time.Clock()

# setting up the window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg = pygame.Color('grey12')
light_grey = (200, 200 ,200)

# Speed Variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True:
    # taking input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7        


    ball_movement()
    player.y += player_speedx
    player_movement()

    # Drawing the stuff we defined
    screen.fill(bg)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Updating the window with a frame rate
    pygame.display.flip()
    clock.tick(60)