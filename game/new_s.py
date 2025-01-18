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
        self.ability = False
        self.dethent = False
        self.jump = False
        self.hurting = True
        self.in_air = True
        self.runs = False
        self.hurts = True
        self.death = False
        self.atacks = False
        self.swing = False
        self.stamina = 10000
        self.animation = []
        self.index = 0
        self.action = 0
        self.up_time = pygame.time.get_ticks()

        anim_type = ['Idle', 'Walk', 'Run', 'Jump', 'Attack_1', 'Attack_2', 'Attack_3', 'Dead', 'Hurt']

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

    def attack(self):
        if player.atacks and player.swing and player2.hurting:
            player.swing = False
            player.stamina -= 10
            if pygame.sprite.collide_mask(player, player2):
                player2.hurting = False
                player2.hp -= random.randint(5, 8)
        if player2.atacks and player2.swing and player.hurting:
            player2.swing = False
            player2.stamina -= 10
            if pygame.sprite.collide_mask(player, player2):
                player.hurting = False
                player.hp -= random.randint(5, 8)

    def abilitys(self):
        if player.ability and player.swing and player2.hurting:
            player.swing = False
            player.stamina -= 25
            if pygame.sprite.collide_mask(player, player2):
                player2.hp -= random.choice([35, 5, 33, 3, 4, 6])
                player2.hurting = False
        if player2.ability and player2.swing and player.hurting:
            player2.swing = False
            player2.stamina -= 25
            if pygame.sprite.collide_mask(player, player2):
                player.hurting = False
                player.hp -= random.choice([35, 5, 33, 3, 4, 6])

    def dead(self):
        if player.hp <= 0:
            player.death = True
        if player2.hp <= 0:
            player2.death = True

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
            player.stamina -= 15
            player2.stamina -= 15
            self.vel = -11
            self.jump = False
            self.in_air = True

        self.vel += GRAVITY

        sy += self.vel
        if self.rect.bottom + sy > 550:
            sy = 550 - self.rect.bottom
            self.in_air = False
        if self.rect.right + sx >= 1100:
            sx = 1000 - self.rect.right
        elif self.rect.left + sx <= -100:
            sx = 0 + self.rect.left
        else:
            self.rect.x += sx

        self.rect.y += sy


    def update_anim(self):
        FLIPPER = 80
        self.image = self.animation[self.action][self.index]
        if pygame.time.get_ticks() - self.up_time > FLIPPER:
            self.up_time = pygame.time.get_ticks()
            self.index += 1
        if not self.atacks and not self.ability and not self.death:
            if self.index >= len(self.animation[self.action]):
                self.index = 0
        elif self.ability:
            if self.index >= len(self.animation[self.action]):
                self.ability = False
                player.hurting = True
                player2.hurting = True
                print(player.hp, player2.hp)
                print(player.stamina, player2.stamina)
                self.index = 0
        elif self.death:
            if self.index >= len(self.animation[self.action]):
                self.death = False
                self.index = 0
        else:
            if self.index >= len(self.animation[self.action]):
                self.atacks = False
                player.hurting = True
                player2.hurting = True
                print(player.hp, player2.hp)
                print(player.stamina, player2.stamina)
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
    player.abilitys()
    player2.abilitys()
    player.attack()
    player2.attack()
    if not player.dethent:
        player.dead()
    if not player.dethent:
        player2.dead()

    if player.alive:
        if player.in_air:
            player.update_action(3)
        elif player.ability:
            player.update_action(6)
        elif (move_left or move_right) and move_scor and not player.ability:
            player.update_action(2)
        elif move_left or move_right and not player.ability:
            player.update_action(1)
        elif player.atacks:
            player.update_action(player.nums)
        elif player.death:
            player.update_action(7)
        elif not player.hurting:
            player.update_action(8)
        else:
            player.update_action(0)
        if not player.ability:
            player.move(move_left, move_right, move_scor)


    if player2.alive:
        if player2.in_air:
            player2.update_action(3)
        elif player2.ability:
            player2.update_action(6)
        elif (move_left_2 or move_right_2) and move_scor_2 and not player2.ability:
            player2.update_action(2)
        elif move_left_2 or move_right_2 and not player2.ability:
            player2.update_action(1)
        elif player2.atacks:
            player2.update_action(player2.nums)
        elif player2.death:
            player2.update_action(7)
        elif not player2.hurting:
            player2.update_action(8)
        else:
            player2.update_action(0)
        if not player2.ability:
            player2.move(move_left_2, move_right_2, move_scor_2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if move_left and keys[pygame.K_LSHIFT]:
                move_scor = True
            if move_right and keys[pygame.K_LSHIFT]:
                move_scor = True
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key == pygame.K_r and player.stamina > 10 and not player.in_air:
                player.swing = True
                player.atacks = True
            if event.key == pygame.K_f and player.stamina > 10 and not player.in_air:
                player.swing = True
                player.ability = True


            if event.key == pygame.K_j:
                move_left_2 = True
            if event.key == pygame.K_l:
                move_right_2 = True
            if keys[pygame.K_RSHIFT] and move_left_2:
                move_scor_2 = True
            if keys[pygame.K_RSHIFT] and move_right_2:
                move_scor_2 = True
            if event.key == pygame.K_i and player2.alive:
                player2.jump = True
            if event.key == pygame.K_o and player.stamina > 10 and not player2.in_air:
                player2.swing = True
                player2.atacks = True
            if event.key == pygame.K_p and player.stamina > 10 and not player2.in_air:
                player2.swing = True
                player2.ability = True



        if event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if not(keys[pygame.K_LSHIFT] and move_left):
                move_scor = False
            if not(keys[pygame.K_LSHIFT] and move_right):
                move_scor = False

            if event.key == pygame.K_j:
                move_left_2 = False
            if event.key == pygame.K_l:
                move_right_2 = False
            if not(keys[pygame.K_RSHIFT] and move_left_2):
                move_scor_2 = False
            if not(keys[pygame.K_RSHIFT] and move_right_2):
                move_scor_2 = False




    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()