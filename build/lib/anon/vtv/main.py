# -*- coding: utf-8 -*-
# Módulos
import sys, os, pygame
from pygame.locals import *
# Constantes
WIDTH = 400
HEIGHT = 490

# Clases
# ---------------------------------------------------------------------

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("src/anon/vtv/images/ven_logo.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.plx = 120
        self.ply = 0
        self.speed = 0
        self.gravity = 0.1

    def actualizar(self, time):
        self.ply = self.ply + self.speed
        self.speed = self.speed + self.gravity
        if (self.ply > HEIGHT):
            self.speed = self.speed * -0.95

# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message: raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

# ---------------------------------------------------------------------

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("vtv pygame")
    background_image = load_image('src/anon/vtv/images/anomonkey.jpg')
    bola = Bola()
    clock = pygame.time.Clock()

    while True:
        time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        bola.actualizar(time)
        screen.blit(background_image, (0, 0))
        screen.blit(bola.image, (bola.plx, bola.ply))
        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()
