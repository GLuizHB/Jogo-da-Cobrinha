import pygame
import random

pygame.init()

# Nome do jogo no display
pygame.display.set_caption("Snake")
largura, altura = 800, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Parâmetros da cobrinha
tamanho_quadrado = 10
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, green, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, white, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, red)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla, direcao_atual):
    if tecla == pygame.K_DOWN and direcao_atual != 'CIMA':
        return 0, tamanho_quadrado, 'BAIXO'
    elif tecla == pygame.K_UP and direcao_atual != 'BAIXO':
        return 0, -tamanho_quadrado, 'CIMA'
    elif tecla == pygame.K_RIGHT and direcao_atual != 'ESQUERDA':
        return tamanho_quadrado, 0, 'DIREITA'
    elif tecla == pygame.K_LEFT and direcao_atual != 'DIREITA':
        return -tamanho_quadrado, 0, 'ESQUERDA'
    return None, None, direcao_atual

def rodar_jogo():
    fim_jogo = False
    
    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0
    direcao_atual = 'DIREITA'
    
    tamanho_cobra = 1
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    
    while not fim_jogo:
        tela.fill(black)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                nova_velocidade_x, nova_velocidade_y, nova_direcao = selecionar_velocidade(evento.key, direcao_atual)
                if nova_velocidade_x is not None and nova_velocidade_y is not None:
                    velocidade_x, velocidade_y = nova_velocidade_x, nova_velocidade_y
                    direcao_atual = nova_direcao
        
        x += velocidade_x
        y += velocidade_y
        
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_pontuacao(tamanho_cobra - 1)
        
        pygame.display.update()
        relogio.tick(velocidade_jogo)

rodar_jogo()
