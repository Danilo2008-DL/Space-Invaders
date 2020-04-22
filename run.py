import pygame
pygame.init()
x = 400
y = 300
pos_x = 200
pos_y = 800
velocidade = 35
velocidade_outros = 15
fundo = pygame.image.load("images/Mapa.1.gif")
nave = pygame.image.load("images/battleship.png")
enemy = pygame.image.load("images/enemy.png")


janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    janela.fill((0,0,0))

    if (pos_y <= -200):
        pos_y = 600

    pos_y -= velocidade_outros

    janela.blit(fundo,(0,0))
    janela.blit(nave, (x + 0,y))
    janela.blit(enemy, (pos_x + 160,pos_y))
    pygame.draw.circle(janela,(0,0,0),(x,y),0)
    pygame.display.update()

pygame.quit()


