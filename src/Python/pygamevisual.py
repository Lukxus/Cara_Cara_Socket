# Example file showing a basic pygame "game loop"
import pygame


def caras():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Image') 
    gustavo = pygame.image.load(r'src\\Imagens\\gustavo.jpg')
    jamilson = pygame.image.load(r'src\\Imagens\\jamilson.jpg')
    kishimoto = pygame.image.load(r'src\\Imagens\\kishimoto.jpg')
    leonardo = pygame.image.load(r'src\\Imagens\\Leonardo.jpg')
    luba = pygame.image.load(r'src\\Imagens\\luba.jpg')
    orlando = pygame.image.load(r'src\\Imagens\\Orlando.jpg')
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("grey")
        # RENDER YOUR GAME HERE
        screen.blit(gustavo, (0, 0))
        screen.blit(luba, (1000, 1000))
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()