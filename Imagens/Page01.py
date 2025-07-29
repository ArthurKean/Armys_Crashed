import pygame

#Comando essencial para funcionar o codigo
pygame.init()

# pygame.mixer.init()
# pygame.mixer.music.load("Imagens/music.wav")  
# pygame.mixer.music.play(-1)  

estado_do_jogo = "menu"  
fonte = pygame.font.SysFont(None, 100)  
fonte_pequena = pygame.font.SysFont(None, 50)  

pygame.display.set_caption("ARmys Crashed")

#Forma a janela e Marcar FPS
screen = pygame.display.set_mode((1280,720))    
Clock = pygame.time.Clock()


#Surface(Objetos da tela)
surface = pygame.Surface((200,200))
fundo = pygame.image.load("Imagens/Fundo_8.png").convert_alpha()
boneco = pygame.image.load("Imagens/Hero.png").convert_alpha()
flecha = pygame.image.load("Imagens/Obstaculos/Arrow1.png").convert_alpha()

#Convertendo o tamanho da imagem
fundo = pygame.transform.scale(fundo,(1280,720))
boneco = pygame.transform.scale(boneco,(180,180))
flecha = pygame.transform.scale(flecha,(100,100))

#Criando o retângulo
flechaRect = flecha.get_rect(bottomleft = (-100,600))
bonecoRect = boneco.get_rect(center = (601,498))

#Colisão precisa (Pega so pixels pintados)
boneco_mask = pygame.mask.from_surface(boneco)
flecha_mask = pygame.mask.from_surface(flecha)

#Gravidade
gravidadedoboneco = 0

#Loop principal do jogo
while True:


    # mouse = pygame.mouse.get_pos()
    # print(mouse)

    #Serve para conseguir fechar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         print("Espaço pressionado")


    #Adicionar elementos na tela
    #Direita = aumenta o x
    #Baixo = aumenta o y
    screen.blit(surface,(100,100))
    screen.blit(fundo,(0,0))
    screen.blit(boneco, bonecoRect) #(600,409)
    screen.blit(flecha, flechaRect)

    #Movimentos da flecha
    flechaRect.x += 5
    if flechaRect.x >= 1500:
        flechaRect.x = -300

    #Colisões

    #Posição relativa
    offset = (flechaRect.x - bonecoRect.x, flechaRect.y - bonecoRect.y)

    if boneco_mask.overlap(flecha_mask, offset):
        print("ColidiUUUU")
        flechaRect.x = -300
        

    #Colisão por retângulos(Pode não funcionar)

    # if bonecoRect.colliderect(flechaRect):
    #     print("Colidiu, AI!!")
    #     flechaRect.x = -300

    #Serve para eu visulizar os "Retângulos"
    pygame.draw.rect(screen, (255,0,0), bonecoRect, 2)
    pygame.draw.rect(screen, (0,255,0), flechaRect, 2)

    #Movimento do Jogador
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and bonecoRect.y >= 410:
        gravidadedoboneco = -15

    gravidadedoboneco += 0.5
    bonecoRect.y += gravidadedoboneco

    if bonecoRect.y > 410:
        bonecoRect.y = 410
        gravidadedoboneco = 0

    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        bonecoRect.x += 5  # Vai pra direita

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        bonecoRect.x -= 5  # Vai pra esquerda

    #Atualizando a tela a cada mudança e fps=60
    pygame.display.update()
    Clock.tick(60)
    