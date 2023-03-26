# Example file showing a basic pygame "game loop"
from tkinter import font
import pygame
import Objetos.figuras

comprimento = 1800
altura = 720

def escolhaCaras(objetos):
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((comprimento, altura))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Image') 
    pygame.display.set_caption('Show Text')

    green=(255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Escolha a sua cara!!', True, green)
    textRect = text.get_rect()
    textRect.center = (comprimento // 2, altura // 2)
    
    

    imagens_caras = [pygame.transform.smoothscale(pygame.image.load(r'src\\Imagens\\gustavo.jpg').convert_alpha(), (300, 300)),
                     pygame.transform.smoothscale(pygame.image.load(r'src\\Imagens\\jamilson.jpg').convert_alpha(), (300, 300)),
                     pygame.transform.smoothscale(pygame.image.load(r'src\\Imagens\\kishimoto.jpg').convert_alpha(), (300, 300)),
                     pygame.transform.smoothscale(pygame.image.load(r'src\\Imagens\\Leonardo.jpg').convert_alpha(), (300, 300)),
                     pygame.transform.smoothscale(pygame.image.load(r'src\\Imagens\\Luba.jpg').convert_alpha(), (300, 300)),
                     pygame.transform.smoothscale(pygame.image.load(r'src\\Imagens\\Orlando.jpg').convert_alpha(), (300, 300))]
    


    running = True
    while running:
        x = 0
        y = 0

        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN  and pygame.mouse.get_pos()[1] <= 300: 
                pos = pygame.mouse.get_pos()[0]
                if pos in range(0, 300):
                    pygame.quit()
                    return objetos["Gustavo"]
                elif pos in range(300, 600):
                    pygame.quit()
                    return objetos["Jamilson"]
                elif pos in range(600, 900):
                    pygame.quit()
                    return objetos["Kishimoto"]
                elif pos in range(900, 1200):
                    pygame.quit()
                    return objetos["Leonardo"]
                elif pos in range(1200, 1500):
                    pygame.quit()
                    return objetos["Luba"]
                elif pos in range(1500, 1800):
                    pygame.quit()
                    return objetos["Orlando"]
                    
        screen.fill("grey")
        # RENDER YOUR GAME HERE

        for image in imagens_caras:
            screen.blit(image, (x, y))
            x+=300
        screen.blit(text, textRect)
        
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()