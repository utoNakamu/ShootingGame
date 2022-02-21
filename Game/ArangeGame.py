import math
import pygame
import random
import math

# 初期化
pygame.init()
screen = pygame.display.set_mode((900, 600))

# 題名
pygame.display.set_caption('battleGame')

# Remon
RemonImg = pygame.image.load("remon.png")
RemonXaxis, RemonYaxis = 350, 420
RemonXDegree = 0

# 炎
flameImg = pygame.image.load('flame.png')
flameXAxis = random.randint(0, 750)
flameYAxis = random.randint(50, 150)
flameXDegree, flameYDegree = 1, 40
movingSpeed = random.uniform(0, 0.7)

# 撃破数
defeatNumber = 0

# 弾
bulletImg = pygame.image.load('bullet.png')
bulletXAxis, bulletYAxis = 50, 300
bulletXDegree, bulletYDegree = 0, 3
bulletState = 'ready'


def remon(xAxis, yAxis):
    screen.blit(RemonImg, (xAxis, yAxis))


def flame(xAxis, yAxis):
    screen.blit(flameImg, (xAxis, yAxis))


def fireBullet(xAxis, yAxis):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImg, (xAxis+16, yAxis+16))


def isBulletContact(flameXAxis, flameYAxis, bulletXAxis, bulletYAxis):
    distance = math.sqrt(math.pow(flameXAxis-bulletXAxis, 2) +
                         math.pow(flameYAxis-bulletYAxis, 2))
    if distance < 27:
        return True
    else:
        return False


running = True

# 画面起動
while running:
    screen.fill('black')
    # 文字スタイルの設定
    #font = pygame.font.SysFont(None, 80)
    #message = font.render('testMessage', False, 'black')
    #screen.blit(message, (500, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ボタンを押したとき
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                RemonXDegree = -0.7
            if event.key == pygame.K_RIGHT:
                RemonXDegree = 0.7
            if event.key == pygame.K_SPACE:
                if bulletState is 'ready':
                    bulletXAxis = RemonXaxis
                    fireBullet(bulletXAxis, bulletYAxis)

        # ボタンを話したとき
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                RemonXDegree = 0

    # れもんの位置情報更新
    RemonXaxis += RemonXDegree
    if RemonXaxis <= 0:
        RemonXaxis = 0
    elif RemonXaxis >= 750:
        RemonXaxis = 750

    # 炎の位置情報更新
    if flameYAxis > 300:
        break
    flameXAxis += flameXDegree
    if flameXAxis <= 0:
        flameXDegree = movingSpeed
        flameYAxis += flameYDegree
    elif flameXAxis >= 800:
        flameXDegree = -movingSpeed
        flameYAxis += flameYDegree

    # 接触情報の更新
    contact = isBulletContact(flameXAxis, flameYAxis, bulletXAxis, bulletYAxis)
    if contact:
        bulletYAxis = 300
        bulletState = 'ready'
        defeatNumber += 1
        flameXAxis = random.randint(0, 750)
        flameYAxis = random.randint(50, 150)

    # bullet情報の更新
    if bulletXAxis <= 0:
        bulletXAxis = 300
        bulletState = 'ready'

    if bulletState == 'fire':
        fireBullet(bulletXAxis, bulletYAxis)
        bulletYAxis -= bulletYDegree

    # 撃破情報の更新
    font = pygame.font.SysFont(None, 32)
    defeat = font.render(f'defeat: {str(defeatNumber)}', True, 'white')
    screen.blit(defeat, (390, 50))

    remon(RemonXaxis, RemonYaxis)
    flame(flameXAxis, flameYAxis)

    pygame.display.update()
