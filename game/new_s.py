import pygame
import random
import os


pygame.init()

screen = pygame.display.set_mode((1000, 600))

move_left = False
move_right = False
move_scor = False
move_left_2 = False
move_right_2 = False
move_scor_2 = False
BG = (255, 255, 255)
GRAVITY = 0.35
BLACK = (0, 0, 0)

def draw_b():
    screen.fill(BG)
    pygame.draw.line(screen, BLACK, (0, 550), (1000, 550))

class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed, flipik):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.alive = True
        self.vel = 0
        self.hp = 100
        self.nums = random.randint(4, 5)
        self.char_type = char_type
        self.direction = 1
        self.flip = flipik
        self.krit = False
        self.jump = False
        self.in_air = True
        self.runs = False
        self.atacks = False
        self.animation = []
        self.index = 0
        self.action = 0
        self.up_time = pygame.time.get_ticks()

        anim_type = ['Idle', 'Walk', 'Run', 'Jump', 'Attack_1', 'Attack_2', 'Attack_3']

        for anim in anim_type:
            temp = []
            num_files = len(os.listdir(f'img/{char_type}/{anim}.png'))
            for i in range(1, num_files + 1):
                img = pygame.image.load(f'img/{char_type}/{anim}.png/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * 2), int(img.get_height() * 2)))
                temp.append(img)
            self.animation.append(temp)

        self.image = self.animation[self.index][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def atack(self):
        pass


    def move(self, moving_left, moving_right, move_scor):
        sx = 0
        sy = 0
        if moving_left:
            sx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_left and move_scor:
            sx = -(self.speed + 4)
            self.flip = True
            self.direction = -1
        if moving_right:
            sx = self.speed
            self.flip = False
            self.direction = 1
        if moving_right and move_scor:
            sx = self.speed + 4
            self.flip = False
            self.direction = 1
        if self.jump and self.in_air == False:
            self.vel = -11
            self.jump = False
            self.in_air = True

        self.vel += GRAVITY

        sy += self.vel
        if self.rect.bottom + sy > 550:
            sy = 550 - self.rect.bottom
            self.in_air = False

        self.rect.x += sx
        self.rect.y += sy

    def update_anim(self):
        FLIPPER = 80
        self.image = self.animation[self.action][self.index]
        if pygame.time.get_ticks() - self.up_time > FLIPPER:
            self.up_time = pygame.time.get_ticks()
            self.index += 1
        if not self.atacks and not self.krit:
            if self.index >= len(self.animation[self.action]):
                self.index = 0
        elif self.krit:
            if self.index >= len(self.animation[self.action]):
                self.krit = False
                self.index = 0
        else:
            if self.index >= len(self.animation[self.action]):
                self.atacks = False
                self.nums = random.randint(4, 5)
                self.index = 0


    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
            self.up_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Player('Fighter', 100, 450, 5, False)
player2 = Player('Fighter', 900, 450, 5, True)

clock = pygame.time.Clock()
FPS = 60
x = 200
y = 200

running = True
while running:

    draw_b()
    player.update_anim()
    player2.update_anim()
    player.draw()
    player2.draw()
    player.atack()
    player2.atack()

    if player.alive:
        if player.in_air:
            player.update_action(3)
        elif player.krit:
            player.update_action(6)
        elif (move_left or move_right) and move_scor and not player.krit:
            player.update_action(2)
        elif move_left or move_right and not player.krit:
            player.update_action(1)
        elif player.atacks:
            player.update_action(player.nums)
        else:
            player.update_action(0)
        if not player.krit:
            player.move(move_left, move_right, move_scor)


    if player2.alive:
        if player2.in_air:
            player2.update_action(3)
        elif player2.krit:
            player2.update_action(6)
        elif (move_left_2 or move_right_2) and move_scor_2 and not player2.krit:
            player2.update_action(2)
        elif move_left_2 or move_right_2 and not player2.krit:
            player2.update_action(1)
        elif player2.atacks:
            player2.update_action(player2.nums)
        else:
            player2.update_action(0)
        if not player2.krit:
            player2.move(move_left_2, move_right_2, move_scor_2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
                move_left = True
                move_scor = True
            if keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
                move_right = True
                move_scor = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key == pygame.K_r:
                player.atacks = True
            if event.key == pygame.K_f:
                player.krit = True

            if keys[pygame.K_RSHIFT] and keys[pygame.K_j]:
                move_left_2 = True
                move_scor_2 = True
            if keys[pygame.K_RSHIFT] and keys[pygame.K_l]:
                move_right_2 = True
                move_scor_2 = True
            if event.key == pygame.K_j:
                move_left_2 = True
            if event.key == pygame.K_l:
                move_right_2 = True
            if event.key == pygame.K_i and player2.alive:
                player2.jump = True
            if event.key == pygame.K_o:
                player2.atacks = True
            if event.key == pygame.K_p:
                player2.krit = True



        if event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            if not(keys[pygame.K_LSHIFT] and keys[pygame.K_a]):
                move_left = False
                move_scor = False
            if not(keys[pygame.K_LSHIFT] and keys[pygame.K_d]):
                move_right = False
                move_scor = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_d and event.key == pygame.K_LSHIFT:
                move_right = False
                move_scor = False
            if event.key == pygame.K_a and event.key == pygame.K_LSHIFT:
                move_left = False
                move_scor = False

            if not(keys[pygame.K_RSHIFT] and keys[pygame.K_j]):
                move_left_2 = False
                move_scor_2 = False
            if not(keys[pygame.K_RSHIFT] and keys[pygame.K_l]):
                move_right_2 = False
                move_scor_2 = False
            if event.key == pygame.K_j:
                move_left_2 = False
            if event.key == pygame.K_l:
                move_right_2 = False
            if event.key == pygame.K_l and event.key == pygame.K_RSHIFT:
                move_right_2 = False
                move_scor_2 = False
            if event.key == pygame.K_j and event.key == pygame.K_RSHIFT:
                move_left_2 = False
                move_scor_2 = False




    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()