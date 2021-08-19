import pygame,sys,random,os
from random import randrange, choice, sample

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 18)
white = (255, 255, 255)
coklat = (51, 45, 53)
blue = (0, 0, 128)

LAYAR = pygame.display.set_mode((1000,670))
pygame.display.set_caption("COUNT ME by Nuril Esti K") 
clock = pygame.time.Clock()
FPS = 120 
#-------------------------- konfigurasi BACKGROUND ------------------------------------
bg1 = pygame.image.load('images/bg_1.png').convert()
bg2 = pygame.image.load('images/bg_2.png').convert()
bg3 = pygame.image.load('images/bg_3.png').convert()
bg4 = pygame.image.load('images/bg_4.png').convert()
bg5 = pygame.image.load('images/bg_5.png').convert()
bg6 = pygame.image.load('images/bg_66.png').convert_alpha()
bg7 = pygame.image.load('images/bg_7.png').convert_alpha()

bgnow = bg1
# -------------------------------------------------------------------------------------
#--------------------------------- splach screen --------------------------------------
speeeed_boy = 12
batasXmin = -80
batasXmax = 1100
sboyX = 0
sboyY = 120
sboy_speedX = 0
sboy_speedY = 0
sboy_baris = 1
sboyA = pygame.image.load('images/boyA.png').convert_alpha()
sboyB = pygame.image.load('images/boyB.png').convert_alpha()
sboy_NOW = sboyA
sboy_rect = sboy_NOW.get_rect(center = (sboyX,sboyY))
# -------------
def ONO() :
    print("ONOOOOOOOOO")
# -------------------------------------------------------------------------------------
#-------------------------- konfigurasi karakter utama --------------------------------
boySpeedX = 0
boySpeedY = 0
boyX = 100
boyY = 100
flagDirBoy = 0
boy1 = pygame.image.load('images/boy_1.png').convert_alpha()
boy2 = pygame.image.load('images/boy_2.png').convert_alpha()
boy1L = pygame.image.load('images/boy_3.png').convert_alpha()
boy2L = pygame.image.load('images/boy_4.png').convert_alpha()
boy_frames = [boy1, boy2, boy1, boy2]
boy_framesL = [boy1L, boy2L, boy1L, boy2L]
boy_index = 0
boy_surface = boy_frames[boy_index]
boy_rect1 = boy1.get_rect(center = (boyX,boyY))
boy_rect2 = boy_surface.get_rect(center = (boyX,boyY))
# baling-baling muter
BALING_MUTER = pygame.USEREVENT
pygame.time.set_timer(BALING_MUTER,150)
# ------------API
boy_api = pygame.image.load('images/boy_api.png').convert_alpha()
boy_api_rect = boy_api.get_rect(center = (-100,-100))
#------------
def BOY_animation(boy_index,j):
    if j == 1 :
        new_boy = boy_frames[boy_index]
    else :
        new_boy = boy_framesL[boy_index]
    new_boy_rect = new_boy.get_rect(center = (boy_rect2.centerx,boy_rect2.centery))
    return new_boy,new_boy_rect
# -------------------------------------------------------------------------------------
# ----------------------------------- SCORE NOW --------------------------------------

def tampilkan_HIGHscore(x) :
    aaaa = "High Score is "+str(x)
    scoretxt = font2.render( aaaa , True, coklat, None)
    scoreRect = scoretxt.get_rect()
    scoreRect.midleft = (438, 450)
    LAYAR.blit(scoretxt,scoreRect)
    

def tampilkan_score(x) :
    scoretxt = font.render( str(x) , True, coklat, None)
    scoreRect = scoretxt.get_rect()
    scoreRect.midleft = (935, 44)
    LAYAR.blit(scoretxt,scoreRect)
def tampilkan_scoreAkhir(x) :
    aaaa = "Your Score is "+str(x)
    scoretxt = font.render( aaaa , True, coklat, None)
    scoreRect = scoretxt.get_rect()
    scoreRect.midleft = (380, 390)
    LAYAR.blit(scoretxt,scoreRect)

# -------------------------------------------------------------------------------------
# ----------------------------------- HIGH SCORE --------------------------------------

# -------------------------------------------------------------------------------------
# ----------------------------------- SOAL --------------------------------------------
templateSOAL = [ ["SOAL ke-1 adalah 1 + 10 = ","11","12","13","14"], 
        ["SOAL ke-2 adalah 2 + 2 = ","4","5","6","7"], 
        ["SOAL ke-3 adalah 5 - 2 = ","3","4","5","6"], 
        ["SOAL ke-4 adalah 2 * 5 = ","10","11","12","13"], 
        ["SOAL ke-5 adalah 3 + 4 = ","7","8","9","10"]
    ]

SOALused = []
# ----------------
def mengacak_SOAL():
    print("acak soal")
    acak_yaaa = sample(templateSOAL,len(templateSOAL))
    #for i in acak_yaaa :
    #    print(i)
    return acak_yaaa
# ----------------
def tampilkan_JAWABAN(itu) :
    jwb1 = font.render( itu[1] , True, coklat, None)
    jwb1Rect = jwb1.get_rect()
    jwb1Rect.midleft = (800, 110)
    LAYAR.blit(jwb1,jwb1Rect)

    jwb2 = font.render( itu[2] , True, coklat, None)
    jwb2Rect = jwb2.get_rect()
    jwb2Rect.midleft = (800, 240)
    LAYAR.blit(jwb2,jwb2Rect)

    jwb3 = font.render( itu[3] , True, coklat, None)
    jwb3Rect = jwb3.get_rect()
    jwb3Rect.midleft = (800, 370)
    LAYAR.blit(jwb3,jwb3Rect)

    jwb4 = font.render( itu[4] , True, coklat, None)
    jwb4Rect = jwb4.get_rect()
    jwb4Rect.midleft = (800, 500)
    LAYAR.blit(jwb4,jwb4Rect)
# ----------------
def tampilkan_SOAL(ini,i):
    print("diterima ",i)
    #print(ini)
    #for x in ini :
    #    print(x)
    text = font.render( ini[i][0] , True, coklat, None)
    textRect = text.get_rect()
    textRect.midleft = (170, 40)
    LAYAR.blit(text,textRect)
    tampilkan_JAWABAN(ini[i])
# -------------------------------------------------------------------------------------
