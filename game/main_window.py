import pygame
import os

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000, 600))

WHITE = (255, 255, 255)
GRAVITY = 0.25
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELOW = (255, 255, 0)
BLUES = (0, 0, 255)
name = 'Lightning Mage'


def draw_b():
    screen.fill(BLACK)

class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, flipik):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.direction = 1
        self.flip = flipik
        self.updateds = 0
        self.animation = []
        self.index = 0
        self.action = 0
        self.coldown = 0
        self.up_time = pygame.time.get_ticks()
        anim_type = ['Idle']


        for anim in anim_type:
            temp = []
            num_files = len(os.listdir(f'img/{char_type}/{anim}.png'))
            for i in range(1, num_files + 1):
                img = pygame.image.load(f'img/{char_type}/{anim}.png/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 4), int(img.get_height() * 4)))
                temp.append(img)
            self.animation.append(temp)

        self.image = self.animation[self.index][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        self.update_anim()
        if self.coldown > 0:
            self.coldown -= 1


    def update_anim(self):
        FLIPPER = 80
        self.image = self.animation[self.action][self.index]
        if pygame.time.get_ticks() - self.up_time > FLIPPER:
            self.up_time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.animation[self.action]):
            self.index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
            self.up_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Player(name, 850, 300, True)

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    draw_b()
    player.draw()
    player.update()
    player.update_action(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()