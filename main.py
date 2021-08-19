from sources.bg import *
# ini branch finishing
# yang merupakan lanjutan dari progress game di hari minggu 15 agustus


# ----- state game e -------
SPLASHSCREEN = 0
MENU = 1
GAMESTART = 2
ABOUT = 3
GAMEOVER = 4
YOUWIN = 5
STATE = SPLASHSCREEN
choosedMenu = 1
ACAK_SOAL = -1
SOAL_KE_1 = 0
SOAL_KE_2 = 1
SOAL_KE_3 = 2
SOAL_KE_4 = 3
SOAL_KE_5 = 4
SOAL_KE_6 = 5
SOAL_KE_7 = 7
SOAL_KE_8 = 8
SOAL_KE_9 = 9
SOAL_KE_10 = 10
MAX_MENANG = 10
# ---------------- SOUND
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
#sound_menu = score_sound 
sound_menu = pygame.mixer.Sound('sound/sfx_hit.wav')

# ---------------- hIGH SCORE
HIGH_SHIGH_SCORECORE = 0
h = open('sources/data.txt', "r")
content = h.readlines()

bacafile = 0
c = 0

for line in content:
    c = len(line)
    for i in line:
        if i.isdigit() == True:     
            if c==3 :
                bacafile += int(i)*100
                c-=1
            elif c==2 :
                bacafile += int(i)*10
                c-=1
            else :
                bacafile += int(i)
HIGH_SCORE = bacafile
print("HIGH_SCORE",HIGH_SCORE)

def update_HIGHSCORE(score_skrg,highscore_skrg) :
    if score_skrg > highscore_skrg :
        f = open('sources/data.txt', "w")
        f.write(str(score_skrg))
        f.close()
        highscore_skrg = score_skrg
        return score_skrg
    else :
        return highscore_skrg

flagSOAL = ACAK_SOAL
acakposisiJawaban = 0
# ---------------------------------------------
#-------------------------- konfigurasi jawaban --------------------------------
aSpeedX = 0
aSpeedY = 0
aX = 100
aY = 100
flagDirBoy = 0
a1 = pygame.image.load('images/pic01.png').convert_alpha()
a2 = pygame.image.load('images/pic02.png').convert_alpha()
a3 = pygame.image.load('images/pic03.png').convert_alpha()
a4 = pygame.image.load('images/pic04.png').convert_alpha()
a5 = pygame.image.load('images/pic05.png').convert_alpha()
a6 = pygame.image.load('images/pic06.png').convert_alpha()
a7 = pygame.image.load('images/pic07.png').convert_alpha()
a8 = pygame.image.load('images/pic08.png').convert_alpha()
a9 = pygame.image.load('images/pic09.png').convert_alpha()
a10 = pygame.image.load('images/pic10.png').convert_alpha()
a11 = pygame.image.load('images/pic11.png').convert_alpha()
a12 = pygame.image.load('images/pic12.png').convert_alpha()
a13 = pygame.image.load('images/pic13.png').convert_alpha()
a14 = pygame.image.load('images/pic14.png').convert_alpha()
a15 = pygame.image.load('images/pic15.png').convert_alpha()
a16 = pygame.image.load('images/pic16.png').convert_alpha()
a17 = pygame.image.load('images/pic17.png').convert_alpha()
a18 = pygame.image.load('images/pic18.png').convert_alpha()
a19 = pygame.image.load('images/pic19.png').convert_alpha()
a20 = pygame.image.load('images/pic20.png').convert_alpha()

a_frames = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20]
a_index = 0
a_surface = a_frames[a_index]
a_rect1 = a1.get_rect(center = (aX,aY))
a_rect2 = a_surface.get_rect(center = (aX,aY))
azkaAX = 300
azkaAY = 300
azka_indexA = 0
azka_indexB = 0
azka_indexC = 0
azka_indexD = 0
azkaA_sur = a_frames[azka_indexA]
azkaB_sur = a_frames[azka_indexB]
azkaC_sur = a_frames[azka_indexC]
azkaD_sur = a_frames[azka_indexD]
azkaA_rect2 = azkaA_sur.get_rect(center = (azkaAX,azkaAY))
azkaB_rect2 = azkaB_sur.get_rect(center = (azkaAX,azkaAY+50))
azkaC_rect2 = azkaC_sur.get_rect(center = (azkaAX,azkaAY+100))
azkaD_rect2 = azkaD_sur.get_rect(center = (azkaAX,azkaAY+150))
# ---------------------------------------------

ayamSoal = [   
            [16,14,12,10,"18 / 3 x ( 12 + 4 ) / 6 = "],
            [15, 9, 7, 14,"6 x 5 x 4 / 8 = "],
            [ 4, 3, 2, 1,"80 / 4 / 5 = "],
            [ 5, 4, 3, 2,"77 / 11 - 2 = "],
            [11, 7, 5, 9,"100 / 20 + ( 2 x 3 ) = "],
            [11, 5, 7, 8,"36 / 4 - ( 23 - 17 ) + 8 = "],
            [10, 8, 7, 5,"( 7 x 11 + ( -85 / 5 ) ) / 6 = "],
            [10, 7, 4, 9,"8 x 5 / 4 = "],
            [12, 8, 5, 9,"( 3 + 1 ) x 9 / 3 = "],
            [13, 5, 2, 8,"48 / 6 + 5 = "],
            [ 6, 5, 3, 2,"8 - 2 x 3 + 4= "],
            [ 5, 4, 3, 2,"40 - 5  x 7 = "],
            [12,11,10,9,"6 + 6 x 3 / 3 = "],
            [ 8, 7, 6, 5,"8 + 6 - 3 x 2 = "],
            [17,15,12, 8,"7 x 6 + 9 / 3 = "],
            [12,11,1,5,"7 + 5 = "],
            [8,6,4,5,"20 / 4 + 3 = "],
            [7,6,5,4,"9 * 9 / 12 + 0.25 = "],
            [9,7,3,6,"27 / 3 = "],
            [8,6,4,3,"16 x 4 / 8 = "]
        ]
# ---------------------------------------------
pertanyaanAcak = []
score_now = 0

def view_acak() :
    sssssss = sample(ayamSoal,10)
    for i in sssssss :
        print(i)
    return sssssss
def view_pertanyaan(isi_nya) :
    #print(pertanyaanAcak[flagSOAL][4])
    text = font.render( pertanyaanAcak[flagSOAL][4] , True, coklat, None)
    textRect = text.get_rect()
    textRect.midleft = (170, 40)
    LAYAR.blit(text,textRect)
def view_jawaban(SA,RA,SB,RB,SC,RC,SD,RD) :
    tempA = pertanyaanAcak[flagSOAL][0]
    tempB = pertanyaanAcak[flagSOAL][1]
    tempC = pertanyaanAcak[flagSOAL][2]
    tempD = pertanyaanAcak[flagSOAL][3]
    SA = a_frames[tempA-1]
    SB = a_frames[tempB-1]
    SC = a_frames[tempC-1]
    SD = a_frames[tempD-1]
    RA = SA.get_rect(center = (randrange(2,48)*20,randrange(10,55)*10))
    RB = SB.get_rect(center = (randrange(2,48)*20,randrange(10,55)*10))
    RC = SC.get_rect(center = (randrange(2,48)*20,randrange(10,55)*10))
    RD = SD.get_rect(center = (randrange(2,48)*20,randrange(10,55)*10))
    return SA,RA,SB,RB,SC,RC,SD,RD

while True:
    clock.tick(FPS) # ensure the event only at FPS setting
    for event in pygame.event.get(): # get list of event
        # if window close -> 'x' was clicked
        if event.type == pygame.QUIT:
            pygame.quit() #quit
            sys.exit() #exit
        # -------------------------------------
        if event.type == BALING_MUTER :
            boy_index += 1
            if boy_index > 3:
                boy_index = 0
            #print("index boy =", boy_index)
            if flagDirBoy==0 :
                boy_surface, boy_rect2 = BOY_animation(boy_index,1)
            else :
                boy_surface, boy_rect2 = BOY_animation(boy_index,2)
        # -------------------------------------
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_x :
                pygame.quit() #quit
                sys.exit() #exit
            if event.key == pygame.K_DOWN and STATE==MENU :
                sound_menu.play()
                if choosedMenu == 1 :
                    bgnow = bg3
                    choosedMenu = 2
                elif choosedMenu == 2 :
                    bgnow = bg2
                    choosedMenu = 1
                print("K_DOWN K_DOWN -- menu", choosedMenu)
            if event.key == pygame.K_UP and STATE==MENU :
                sound_menu.play()
                if choosedMenu == 1 :
                    bgnow = bg3
                    choosedMenu = 2
                elif choosedMenu == 2 :
                    bgnow = bg2
                    choosedMenu = 1
                print("K_UP K_UP -- menu", choosedMenu)
            if event.key == pygame.K_RETURN and STATE==MENU :
                print("enter enter")
                if choosedMenu == 2 :
                    bgnow = bg4
                    STATE = ABOUT
                elif choosedMenu == 1 :
                    bgnow = bg5
                    STATE = GAMESTART
                    score_now = 0
                    flagSOAL = ACAK_SOAL
            elif event.key == pygame.K_RETURN and STATE==ABOUT :
                STATE = MENU
                bgnow = bg3
                choosedMenu = 2
            elif event.key == pygame.K_RETURN and STATE==GAMESTART :
                #if flagSOAL > ACAK_SOAL :
                if flagSOAL > ACAK_SOAL and boy_rect2.colliderect(azkaA_rect2) :
                    score_now +=1
                    score_sound.play()
                    #tampilkan_scoreAkhir(score_now)
                    if score_now < MAX_MENANG :
                        flagSOAL+=1
                        acakposisiJawaban = 0
                    else :
                        STATE = YOUWIN
                        HIGH_SCORE = update_HIGHSCORE(score_now,HIGH_SCORE)
                        
                    
                print("enter enter")
                if boy_rect2.colliderect(azkaB_rect2) or boy_rect2.colliderect(azkaC_rect2) or boy_rect2.colliderect(azkaD_rect2):
                    STATE = GAMEOVER
                    HIGH_SCORE = update_HIGHSCORE(score_now,HIGH_SCORE)
            elif event.key == pygame.K_RETURN and STATE==GAMEOVER :
                STATE = MENU
                bgnow = bg2
                choosedMenu = 1
            elif event.key == pygame.K_RETURN and STATE==YOUWIN :
                STATE = MENU
                bgnow = bg2
                choosedMenu = 1
            if event.key == pygame.K_LEFT:
                boySpeedX = -3
                flagDirBoy = 1
            elif event.key == pygame.K_RIGHT:
                boySpeedX = 3
                flagDirBoy = 0
            elif event.key == pygame.K_UP:
                boySpeedY = -3
            elif event.key == pygame.K_DOWN:
                boySpeedY = 3
        # -------------------------------------
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                boySpeedX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                boySpeedY = 0
        
        # -------------------------------------

    # ----------------------- tampilan layar -----------------------
    if STATE == SPLASHSCREEN :
        #print("SPLASHSCREEN")
        if sboy_baris == 1 :
            if sboyX < batasXmax :
                sboy_speedX = speeeed_boy
                sboyX += sboy_speedX
            else :
                sboy_baris = 2
                sboy_NOW = sboyB
                sboyY += 205
        elif sboy_baris == 2 :
            #print("baris 2")
            if sboyX > batasXmin :
                sboy_speedX = 0-speeeed_boy
                sboyX += sboy_speedX
            else :
                sboy_baris = 3
                sboy_NOW = sboyA
                sboyY += 205
        elif sboy_baris == 3 :
            print("baris 3")
            if sboyX < batasXmax :
                sboy_speedX = speeeed_boy
                sboyX += sboy_speedX
            else :
                STATE = MENU
                choosedMenu = 1
        sboy_rect.centerx = sboyX
        sboy_rect.centery = sboyY
        bgnow = bg1
        if STATE == MENU :
            bgnow = bg2  
        LAYAR.blit(bgnow,(0,0))
        LAYAR.blit(sboy_NOW,sboy_rect)
        #splashscreen_sound.play()
    elif STATE == MENU :
        print("menu")
        LAYAR.blit(bgnow,(0,0))
        update_HIGHSCORE(score_now,HIGH_SCORE)
        tampilkan_HIGHscore(HIGH_SCORE)

    elif STATE == ABOUT :
        print("about")
        LAYAR.blit(bgnow,(0,0))
    elif STATE == GAMESTART :
        #print("game start")

        if boyX < 30 and boySpeedX < 0:
            print("mentok KIRI")
        elif boyX > 972 and boySpeedX > 0:
            print("mentok KANAN")
        else :
            boyX = boyX + boySpeedX
        if boyY < 97 and boySpeedY < 0:
            print("mentok ATAS")
        elif boyY > 640 and boySpeedY > 0:
            print("mentok BAWAH")
        else :
            boyY = boyY + boySpeedY

        bgnow = bg5
        LAYAR.blit(bgnow,(0,0))
        print("posisi boy = ", boyX, "-", boyY)
        boy_rect2.centerx = boyX
        boy_rect2.centery = boyY
        LAYAR.blit(boy_surface,boy_rect2)
        # -----------------------------------------
        tampilkan_score(score_now)
        #-----------------------------------------
        #print("flag soal",flagSOAL, " -- acakposisi", acakposisiJawaban)
        if flagSOAL==ACAK_SOAL :
            pertanyaanAcak = view_acak()
            flagSOAL += 1
            acakposisiJawaban = 0
        else :
            view_pertanyaan(pertanyaanAcak)
            if acakposisiJawaban== 0 :
                azkaA_sur,azkaA_rect2,azkaB_sur,azkaB_rect2,azkaC_sur,azkaC_rect2,azkaD_sur,azkaD_rect2 = view_jawaban(azkaA_sur,azkaA_rect2,azkaB_sur,azkaB_rect2,azkaC_sur,azkaC_rect2,azkaD_sur,azkaD_rect2)
                acakposisiJawaban = 1
            LAYAR.blit(azkaA_sur,azkaA_rect2)
            LAYAR.blit(azkaB_sur,azkaB_rect2)
            LAYAR.blit(azkaC_sur,azkaC_rect2)
            LAYAR.blit(azkaD_sur,azkaD_rect2)
            
            #print("boy",boy_rect2.center," --- A",azkaA_rect2.center)
            
            if boy_rect2.colliderect(azkaA_rect2) :
                #print("--- tabrak aaaa ---")
                abc=0
                #break
            if boy_rect2.colliderect(azkaB_rect2) :
                abc=0
                #print("--- tabrak bbbb ---")
                #break
            if boy_rect2.colliderect(azkaC_rect2) :
                abc=0
                #print("--- tabrak ccc ---")
                #break
            if boy_rect2.colliderect(azkaD_rect2) :
                abc=0
                #print("--- tabrak ddd ---")
                #break

            
        # --------------------------------------- SOAL ---
        # if flagSOAL==ACAK_SOAL :
        #     SOALused = mengacak_SOAL()
        #     flagSOAL += 1
        # else :
        #     print("kirim ",flagSOAL)
        #     tampilkan_SOAL(SOALused,flagSOAL) 
        # ------------------------------------------------
    elif STATE == GAMEOVER :
        boy_api_rect.centerx = boyX
        boy_api_rect.centery = boyY
        LAYAR.blit(boy_api, boy_api_rect)
        print(boy_rect2.center)

        bgnow = bg6
        LAYAR.blit(bgnow,(125,150))
        tampilkan_scoreAkhir(score_now)
        
    elif STATE == YOUWIN :
        
        #boy_api_rect.center = boy_rect2.center
        boy_api_rect.centerx = boyX
        boy_api_rect.centery = boyY
        LAYAR.blit(boy_api, boy_api_rect)
        print(boy_rect2.center)

        bgnow = bg7
        LAYAR.blit(bgnow,(125,150))
        tampilkan_scoreAkhir(score_now)
    else :
        print("-------- ERROR -------")
    # --------------------------------------------------------------
    pygame.display.update()

print("-------- G A M E    O V E R -------")