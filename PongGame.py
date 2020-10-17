import pygame, sys, random

def ball_movement():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # making the ball bounce
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(hitSound)
        ball_speed_y *= -1

    # Player Score
    if ball.left <= 0 :
        pygame.mixer.Sound.play(scoreSound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    # Opponent Score
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(scoreSound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    # If the ball collides wth the Player and opponent
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(hitSound)
        ball_speed_x *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(hitSound)
        ball_speed_x *= -1
    
def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    currentTime = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if currentTime - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 -10, screen_height/2 +20))
    if 700 < currentTime - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 -10, screen_height/2 +20))
    if 1400 < currentTime - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 -10, screen_height/2 +20))

    if currentTime - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7*random.choice((1, -1))
        ball_speed_x = 7*random.choice((1, -1))
        score_time = None
        

# General setup
pygame.mixer.pre_init(44100, -16, 2, 512)
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

# colors
bg = pygame.Color('grey12')
light_grey = (200, 200 ,200)

# Speed Variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 40)

# Score Timer
score_time = True

# Sound Files
hitSound = pygame.mixer.Sound("pong.ogg")
scoreSound = pygame.mixer.Sound("score.ogg")

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
        if opponent_score >= 10 or player_score >= 10:
            pygame.quit()
            sys.exit()     

    # Game Logic
    ball_movement()
    player_movement()
    opponent_ai()

    # Drawing the stuff we defined
    screen.fill(bg)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render("{}".format(player_score), False, light_grey)
    screen.blit(player_text, (660, 360))
    opponent_text = game_font.render("{}".format(opponent_score), False, light_grey)
    screen.blit(opponent_text, (600, 360))


    # Updating the window with a frame rate
    pygame.display.flip()
    clock.tick(60)