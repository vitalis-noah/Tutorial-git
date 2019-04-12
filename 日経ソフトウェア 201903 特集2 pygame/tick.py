#tick test
import pygame #Pygameのライブラリをインポート

WIDTH = 640
HEIGHT = 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init() #Pygameの初期化
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #描画オブジェクトを作成
myfont = pygame.font.Font(None,32)
myclock = pygame.time.Clock()
loopcnt = 0
endflag = 0

#メインループ処理
while endflag == 0:
  for event in pygame.event.get():
      if event.type == pygame.QUIT: endflag = 1 #ウィンドウを閉じたとき

  screen.fill(BLACK)
  loopcnt += 1
  imagetext = myfont.render(str(loopcnt), True ,WHITE) #ループ回数の表示
  screen.blit(imagetext, (100, 50))
  myclock.tick(60) #ループの周期を1/60秒とする
  pygame.display.flip() #画面を描画

pygame.quit()
