import pygame


pygame.init()

screen = pygame.display.set_mode((900, 600))
# スクリーン背景
# screen.fill("#9dd1ff")
# 題名
pygame.display.set_caption('battleGame')
# Remon
RemonImg = pygame.image.load("remon.png")
RemonXaxis, RemonYaxis = 300, 300
RemonXDegree = 0


def Remon(xAxis, yAxis):
    # 画像の初期位置を設定
    screen.blit(RemonImg, (xAxis, yAxis))


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
                RemonXDegree = -1.5
            if event.key == pygame.K_RIGHT:
                RemonXDegree = 1.5
            # if event.key == pygame.K_SPACE:
            # if bulletState is 'ready':
            #     bulletXAxis = RemonXaxis
            #     fireBullet(bulletXAxis, bulletYAxis)

        # ボタンを話したとき
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                RemonXDegree = 0

    RemonXaxis += RemonXDegree
    Remon(RemonXaxis, RemonYaxis)
    pygame.display.update()