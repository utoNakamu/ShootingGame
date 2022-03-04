import math
import pygame
import random

# 初期化
pygame.init()
screen = pygame.display.set_mode((900, 600))

# 題名
pygame.display.set_caption('battleGame')

# Remon
RemonImg = pygame.image.load("remon.png")
RemonXaxis, RemonYaxis = 350, 420
RemonXDegree = 0

# クロスケ
kurosukeImg = pygame.image.load('kurosuke.png')
kurosukeXAxis = random.randint(0, 750)
kurosukeYAxis = random.randint(50, 150)
kurosukeXDegree, kurosukeYDegree = 1, 40
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


def kurosuke(xAxis, yAxis):
    screen.blit(kurosukeImg, (xAxis, yAxis))


def fireBullet(xAxis, yAxis):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImg, (xAxis+16, yAxis+16))


def isBulletContact(kurosukeXAxis, kurosukeYAxis, bulletXAxis, bulletYAxis):
    distance = math.sqrt(math.pow(kurosukeXAxis-bulletXAxis, 2) +
                         math.pow(kurosukeYAxis-bulletYAxis, 2))
    if distance < 27:
        return True
    else:
        return False


running = True

# 画面起動
while running:
    screen.fill('black')

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
    if kurosukeYAxis > 300:
        break
    kurosukeXAxis += kurosukeXDegree
    if kurosukeXAxis <= 0:
        kurosukeXDegree = movingSpeed
        kurosukeYAxis += kurosukeYDegree
    elif kurosukeXAxis >= 800:
        kurosukeXDegree = -movingSpeed
        kurosukeYAxis += kurosukeYDegree

    # 接触情報の更新
    contact = isBulletContact(
        kurosukeXAxis, kurosukeYAxis, bulletXAxis, bulletYAxis)
    if contact:
        bulletYAxis = 300
        bulletState = 'ready'
        defeatNumber += 1
        kurosukeXAxis = random.randint(0, 750)
        kurosukeYAxis = random.randint(50, 150)

    # bullet情報の更新
    if bulletYAxis <= 0:
        bulletYAxis = 300
        bulletState = 'ready'

    if bulletState == 'fire':
        fireBullet(bulletXAxis, bulletYAxis)
        bulletYAxis -= bulletYDegree

    # 撃破情報の更新
    font = pygame.font.SysFont(None, 32)
    defeat = font.render(f'defeat: {str(defeatNumber)}', True, 'white')
    screen.blit(defeat, (390, 50))

    remon(RemonXaxis, RemonYaxis)
    kurosuke(kurosukeXAxis, kurosukeYAxis)

    pygame.display.update()
