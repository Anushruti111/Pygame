import pygame
import random
import math
from pygame import mixer
pygame.init()
screen= pygame.display.set_mode((800, 600))
background= pygame.image.load("background1.png")
pygame.display.set_caption("space invaders")
player=pygame.image.load("player.png")
playerX=370
playerY=480
playerxy=0
enemy = []
enemyX = []
enemyY = []
enemy_x = []
enemy_y = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemy_x.append(4)
    enemy_y.append(40)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def ply(x,y):
    screen.blit(player,(x,y))
def ene(x,y,i):
    screen.blit(enemy[i],(x,y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
running=True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):

                playerxy=-5

            if(event.key==pygame.K_RIGHT):
                playerxy=5
            if (event.key == pygame.K_SPACE):
                if bullet_state is "ready":


                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if(event.type==pygame.KEYUP):
            if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                playerxy=0

    playerX+=playerxy
    if(playerX<=0):
        playerX=0
    elif(playerX>=736):
        playerX=736
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemy_x[i]
        if enemyX[i] <= 0:
            enemy_x[i] = 4
            enemyY[i] += enemy_y[i]
        elif enemyX[i] >= 736:
            enemy_x[i] = -4
            enemyY[i] += enemy_y[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:

            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        ene(enemyX[i], enemyY[i], i)
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    ply(playerX , playerY)
    show_score(textX, testY)
    pygame.display.update()




