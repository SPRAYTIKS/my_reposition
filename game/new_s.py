import pygame
import random
import os

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 600))


move_left = False
move_right = False
move_scor = False
move_left_2 = False
move_right_2 = False
move_scor_2 = False
rouds = 1
WHITE = (255, 255, 255)
GRAVITY = 0.25
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELOW = (255, 255, 0)
BLUES = (0, 0, 255)
map_image = pygame.image.load('img/les.jpg')
map_image = pygame.transform.scale(map_image, (1000, 600))






def draw_b():
    screen.blit(map_image, (0, 0))


def draw_text(text, text_col, x, y, size):
    img = pygame.font.Font('font/batle.ttf', size)
    img = img.render(text, True, text_col)
    screen.blit(img, (x, y))

def status_bar():
    if player2.hp >= 100:
        player2.hp = 100
    if player.hp >= 100:
        player.hp = 100
    if player.in_air:
        player.stamina -= 0.15
    if player2.in_air:
        player2.stamina -= 0.15


    if player.stamina < 0:
        player.stamina = 0
    if player2.stamina < 0:
        player2.stamina = 0

    if player.stamina <= 100:
        player.stamina += 0.07
    if player2.stamina <= 100:
        player2.stamina += 0.07


def restart_game():
    global time, time2, move_left, move_right, \
        move_scor, move_left_2, move_right_2, move_scor_2
    player.stamina = 100
    player2.stamina = 100
    player.hp = 100
    player2.hp = 100
    time = 5000
    time2 = 200
    time3 = 5000
    player.rect.center = (100, 450)
    player2.rect.center = (900, 450)
    player.dethent = False
    player2.dethent = False
    move_left = False
    move_right = False
    move_scor = False
    move_left_2 = False
    move_right_2 = False
    move_scor_2 = False


def game_rounds():
    global running

    pygame.draw.circle(screen, WHITE, (35, 80), 10)
    pygame.draw.circle(screen, WHITE, (63, 80), 10)

    pygame.draw.circle(screen, WHITE, (935, 80), 10)
    pygame.draw.circle(screen, WHITE, (963, 80), 10)

    if player.round == 1:
        pygame.draw.circle(screen, YELOW, (35, 80), 8)
    if player.round == 2:
        pygame.draw.circle(screen, YELOW, (35, 80), 8)
        pygame.draw.circle(screen, YELOW, (63, 80), 8)

    if player2.round == 1:
        pygame.draw.circle(screen, YELOW, (963, 80), 8)
    if player2.round == 2:
        pygame.draw.circle(screen, YELOW, (935, 80), 8)
        pygame.draw.circle(screen, YELOW, (963, 80), 8)


    if player.round == 2:
        running = False
    if player2.round == 2:
        running = False



class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed, flipik, id):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.alive = True
        self.coldown = 0
        self.vel = 0
        self.hp = 100
        self.round = 0
        self.nums = 0
        self.char_type = char_type
        self.direction = 1
        self.flip = flipik
        self.ability = False
        self.dethent = False
        self.jump = False
        self.id = id
        self.hurting = True
        self.in_air = True
        self.runs = False
        self.hurts = True
        self.death = False
        self.atacks = False
        self.swing = False
        self.charge = False
        self.stamina = 100
        self.animation = []
        self.abil_krit = False
        self.indexis = 0
        self.indexis2 = 0
        self.abil_helth = False
        self.abili_thrower = False
        self.index = 0
        self.action = 0
        self.sets = False
        self.up_time = pygame.time.get_ticks()
        if self.char_type == 'Samurai_Archer':
            anim_type = ['Idle', 'Walk', 'Run', 'Jump', 'Attack_1', 'Attack_2', 'Attack_3', 'Dead', 'Hurt', 'Attack_4']
        else:
            anim_type = ['Idle', 'Walk', 'Run', 'Jump', 'Attack_1', 'Attack_2', 'Attack_3', 'Dead', 'Hurt']

        if char_type in ['Fighter', 'Samurai', 'Shinobi']:
            sow = 2
        elif char_type == 'Samurai_Archer':
            sow = 2.2
        else:
            sow = 2.5


        for anim in anim_type:
            temp = []
            num_files = len(os.listdir(f'img/{char_type}/{anim}.png'))
            for i in range(1, num_files + 1):
                img = pygame.image.load(f'img/{char_type}/{anim}.png/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * sow), int(img.get_height() * sow)))
                temp.append(img)
            self.animation.append(temp)

        self.image = self.animation[self.index][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def attack(self):
        if player.atacks and player.swing and player2.hurting:
            player.swing = False
            player.stamina -= 5
            if pygame.sprite.collide_mask(player, player2):
                if random.randint(1, 2) == 1:
                    sound_attack_1.play()
                else:
                    sound_attack_2.play()
                player2.hurting = False
                player2.hp -= random.randint(4, 8)
            else:
                sound_promax.play()
        if player2.atacks and player2.swing and player.hurting:
            player2.swing = False
            player2.stamina -= 5
            if pygame.sprite.collide_mask(player, player2):
                if random.randint(1, 2) == 1:
                    sound_attack_1p.play()
                else:
                    sound_attack_2p.play()
                player.hurting = False
                player.hp -= random.randint(4, 8)
            else:
                sound_promaxp.play()

    def abilitys(self):
        if player.abil_krit:
            if player.ability and player.swing and player2.hurting:
                player.swing = False
                player.stamina -= 20
                if pygame.sprite.collide_mask(player, player2):
                    sound_attack_3.play()
                    player2.hp -= random.choice([35, 5, 33, 3, 4, 6, 35, 40])
                    player2.hurting = False
                else:
                    sound_promax.play()
        if player2.abil_krit:
            if player2.ability and player2.swing and player.hurting:
                player2.swing = False
                player2.stamina -= 20
                if pygame.sprite.collide_mask(player, player2):
                    sound_attack_3p.play()
                    player.hurting = False
                    player.hp -= random.choice([35, 5, 33, 3, 4, 6, 35, 40])
                else:
                    sound_promaxp.play()
        if player.abil_helth:
            if player.ability and player.swing:
                player.swing = False
                player.stamina -= 50
                sound_attack_3.play()
                if player.hp <= 100:
                    player.hp += random.choice([35, 20, 33, 25, 24, 28, 50, 20, 21])
                else:
                    player.hp = 100
        if player2.abil_helth:
            if player2.ability and player2.swing:
                player2.swing = False
                player2.stamina -= 50
                sound_attack_3p.play()
                if player2.hp <= 100:
                    player2.hp += random.choice([35, 20, 33, 25, 24, 28, 50, 20, 21])
                else:
                    player2.hp = 100


    def draw_health_bar(self, health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, YELOW, (x - 2, y - 2, 404, 29))
        pygame.draw.rect(screen, RED, (x, y, 400, 25))
        pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 25))

    def draw_stamina_bar(self, stamina, x, y):
        stam = stamina / 100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 12))
        pygame.draw.rect(screen, BLUES, (x, y, 400 * stam, 8))


    def dead(self):
        if player.hp <= 0:
            FLIPPER = 150
            player.image = player.animation[7][player.indexis - 1]
            if player.indexis == len(player.animation[7]):
                player.image = player.animation[7][player.indexis - 1]
            elif pygame.time.get_ticks() - player.up_time > FLIPPER :
                player.up_time = pygame.time.get_ticks()
                player.indexis += 1
            player.dethent = True


        if player2.hp <= 0:
            FLIPPER = 150
            player2.image = player2.animation[7][player2.indexis - 1]
            if player2.indexis == len(player2.animation[7]):
                player2.image = player2.animation[7][player2.indexis - 1]
            elif pygame.time.get_ticks() - player2.up_time > FLIPPER:
                player2.up_time = pygame.time.get_ticks()
                player2.indexis += 1
            player2.dethent = True

    def update(self):
        self.update_anim()
        if self.coldown > 0:
            self.coldown -= 1


    def move(self, moving_left, moving_right, move_scor):
        sx = 0
        sy = 0
        if moving_left:
            sx = -self.speed
            self.flip = True
            if time % random.randint(40, 48)  == 1:
                walk.play()
            self.direction = -1
        if moving_left and move_scor:
            if time % random.randint(20, 35)  == 1:
                walk.play()
            sx = -(self.speed + 4)
            self.flip = True
            self.direction = -1
        if moving_right:
            sx = self.speed
            self.flip = False
            self.direction = 1
            if time % random.randint(40, 48)  == 1:
                walk.play()
        if moving_right and move_scor:
            if time % random.randint(20, 35) == 1:
                walk.play()
            sx = self.speed + 4
            self.flip = False
            self.direction = 1
        if self.jump and self.in_air == False:
            self.vel = -11
            self.jump = False
            self.in_air = True


        self.vel += GRAVITY


        sy += self.vel
        if self.rect.bottom + sy > 560:
            sy = 560 - self.rect.bottom
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
            if player.abili_thrower and not player.charge and player.char_type == 'Samurai_Archer':
                sound_attack_4.play()
                player.charge = True
            if player2.abili_thrower and not player2.charge and player2.char_type == 'Samurai_Archer':
                sound_attack_4.play()
                player2.charge = True
            if self.index >= len(self.animation[self.action]):
                player.hurting = True
                player2.hurting = True
                if player.ability:
                    if player.abili_thrower:
                        player.stamina -= 15
                        player.charge = False
                        player.shoot()
                if player2.ability:
                    if player2.abili_thrower:
                        player2.stamina -= 15
                        player.charge = False
                        player2.shoot()
                self.ability = False

                self.index = 0
        else:
            if self.index >= len(self.animation[self.action]):
                self.atacks = False
                player.hurting = True
                player2.hurting = True
                self.nums = random.randint(4, 5)
                self.index = 0


    def shoot(self):
        if self.coldown == 0:
            self.coldown = 40
            if self.id == 0:
                sound_attack_3.play()
                bulet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction),
                               self.rect.centery + 30, self.direction)
                bulet_group.add(bulet)
            else:
                sound_attack_3p.play()
                bul = Bullet_two(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction),
                               self.rect.centery + 30, self.direction)
                bulet_group.add(bul)



    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
            self.up_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.index = 0
        self.image = list_bulet[self.index]
        self.rect = self.image.get_rect()
        self.up_time = pygame.time.get_ticks()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        FLIPPER = 80
        self.image = list_bulet[self.index]
        if pygame.time.get_ticks() - self.up_time > FLIPPER:
            self.up_time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(list_bulet):
            self.index = 0
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > 1000 - 100:
            self.kill()
        if pygame.sprite.spritecollide(player2, bulet_group, False):
            if player.alive:
                player2.hp -= random.randint(5, 20)
                self.kill()



class Bullet_two(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.index_1 = 0
        self.image = list_bulet_2[self.index_1]
        self.rect = self.image.get_rect()
        self.up_time = pygame.time.get_ticks()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        FLIPPER = 80
        self.image = list_bulet_2[self.index_1]
        if pygame.time.get_ticks() - self.up_time > FLIPPER:
            self.up_time = pygame.time.get_ticks()
            self.index_1 += 1
        if self.index_1 >= len(list_bulet_2):
            self.index_1 = 0
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > 1000 - 100:
            self.kill()
        if pygame.sprite.spritecollide(player, bulet_group, False):
            if player.alive:
                player.hp -= random.randint(5, 20)
                self.kill()




bulet_group = pygame.sprite.Group()
player = Player('Lightning Mage', 100, 450, 5, False, 0)
player2 = Player('Kunoichi', 900, 450, 5, True, 1)
player2.direction = -1

sound_attack_4 = pygame.mixer.Sound('sounds/vipusk (mp3cut.net).mp3')
walk = pygame.mixer.Sound('sounds/shagi.mp3')
jumpik = pygame.mixer.Sound('sounds/prig-s.mp3')


if player.char_type == 'Fighter':
    sound_attack_1 = pygame.mixer.Sound('sounds/attack_rukoi_1.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/attack_rukoi_2.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/attack_noga.mp3')
    sound_promax = pygame.mixer.Sound('sounds/promax.mp3')
if player2.char_type == 'Fighter':
    sound_attack_1p = pygame.mixer.Sound('sounds/attack_rukoi_1.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/attack_rukoi_2.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/attack_noga.mp3')
    sound_promaxp = pygame.mixer.Sound('sounds/promax.mp3')


if player.char_type == 'Samurai':
    sound_attack_1 = pygame.mixer.Sound('sounds/udarchik.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/udar_nozhom.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/udar_katanoi.mp3')
    sound_promax = pygame.mixer.Sound('sounds/promoi.mp3')
if player2.char_type == 'Samurai':
    sound_attack_1p = pygame.mixer.Sound('sounds/udarchik.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/udar_nozhom.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/udar_katanoi.mp3')
    sound_promaxp = pygame.mixer.Sound('sounds/promoi.mp3')


if player.char_type == 'Samurai_Archer':
    sound_attack_1 = pygame.mixer.Sound('sounds/udarchik.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/udar_nozhom.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/strela.mp3')
    sound_promax = pygame.mixer.Sound('sounds/promoi.mp3')
if player2.char_type == 'Samurai_Archer':
    sound_attack_1p = pygame.mixer.Sound('sounds/udarchik.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/udar_nozhom.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/strela.mp3')
    sound_promaxp = pygame.mixer.Sound('sounds/promoi.mp3')


if player.char_type == 'Shinobi':
    sound_attack_1 = pygame.mixer.Sound('sounds/nozhom_1_attack.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/attack_2_nozhom.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/attacks_3_super.mp3')
    sound_promax = pygame.mixer.Sound('sounds/promoi.mp3')
if player2.char_type == 'Shinobi':
    sound_attack_1p = pygame.mixer.Sound('sounds/nozhom_1_attack.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/attack_2_nozhom.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/attacks_3_super.mp3')
    sound_promaxp = pygame.mixer.Sound('sounds/promoi.mp3')


if player.char_type == 'Ninja_Monk':
    sound_attack_1 = pygame.mixer.Sound('sounds/nozhom_1_attack.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/attack_2_nozhom.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/kunai_1.mp3')
    sound_promax = pygame.mixer.Sound('sounds/promoi.mp3')
if player2.char_type == 'Ninja_Monk':
    sound_attack_1p = pygame.mixer.Sound('sounds/nozhom_1_attack.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/attack_2_nozhom.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/kunai_1.mp3')
    sound_promaxp = pygame.mixer.Sound('sounds/promoi.mp3')


if player.char_type == 'Kunoichi':
    sound_attack_1 = pygame.mixer.Sound('sounds/cepi_1.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/cepi_2.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/eda.mp3')
    sound_promax = pygame.mixer.Sound('sounds/promax_cepi.mp3')
if player2.char_type == 'Kunoichi':
    sound_attack_1p = pygame.mixer.Sound('sounds/cepi_1.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/cepi_2.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/eda.mp3')
    sound_promaxp = pygame.mixer.Sound('sounds/promax_cepi.mp3')


if player.char_type == 'Fire vizard':
    sound_attack_1 = pygame.mixer.Sound('sounds/udarchik.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/attack_2_nozhom.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/shar.mp3')
    sound_attack_3.set_volume(0.2)
    sound_promax = pygame.mixer.Sound('sounds/promoi.mp3')
if player2.char_type == 'Fire vizard':
    sound_attack_1p = pygame.mixer.Sound('sounds/udarchik.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/attack_2_nozhom.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/shar.mp3')
    sound_attack_3p.set_volume(0.2)
    sound_promaxp = pygame.mixer.Sound('sounds/promoi.mp3')


if player.char_type == 'Lightning Mage':
    sound_attack_1 = pygame.mixer.Sound('sounds/udar_mechom_2.mp3')
    sound_attack_2 = pygame.mixer.Sound('sounds/udar_mechom.mp3')
    sound_attack_3 = pygame.mixer.Sound('sounds/shar_electro.mp3')
    sound_attack_3.set_volume(0.2)
    sound_promax = pygame.mixer.Sound('sounds/vazm.mp3')
if player2.char_type == 'Lightning Mage':
    sound_attack_1p = pygame.mixer.Sound('sounds/udar_mechom_2.mp3')
    sound_attack_2p = pygame.mixer.Sound('sounds/udar_mechom.mp3')
    sound_attack_3p = pygame.mixer.Sound('sounds/shar_electro.mp3')
    sound_attack_3p.set_volume(0.2)
    sound_promaxp = pygame.mixer.Sound('sounds/vazm.mp3')





if player.char_type == 'Samurai_Archer':
    player.nums = random.choice([4, 5, 9])
else:
    player.nums = random.choice([4, 5])

if player2.char_type == 'Samurai_Archer':
    player2.nums = random.choice([4, 5, 9])
else:
    player2.nums = random.choice([4, 5])


if player.char_type in ['Fighter', 'Samurai', 'Shinobi']:
    player.abil_krit = True
elif player.char_type in ['Fire vizard', 'Lightning Mage', 'Ninja_Monk', 'Samurai_Archer']:
    player.abili_thrower = True
elif player.char_type in ['Kunoichi']:
    player.abil_helth = True
if player2.char_type in ['Fighter', 'Samurai', 'Shinobi']:
    player2.abil_krit = True
elif player2.char_type in ['Fire vizard', 'Lightning Mage', 'Ninja_Monk', 'Samurai_Archer']:
    player2.abili_thrower = True
elif player2.char_type in ['Kunoichi']:
    player2.abil_helth = True

clock = pygame.time.Clock()
FPS = 60
x = 200
y = 200
time = 5000
time2 = 200
time3 = 5000

list_bulet = []
list_bulet_2 = []

if player.char_type == 'Fire vizard':
    for i in range(1, 12):
        img = pygame.image.load(f'img/Fire vizard/bulet.png/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (200, 200))
        img = pygame.transform.scale(img, (int(img.get_width()), int(img.get_height())))
        list_bulet.append(img)
elif player.char_type == 'Lightning Mage':
    for i in range(1, 10):
        img = pygame.image.load(f'img/Lightning Mage/bulet.png/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (200, 200))
        img = pygame.transform.scale(img, (int(img.get_width()), int(img.get_height())))
        list_bulet.append(img)
elif player.char_type == 'Ninja_Monk':
    for i in range(1, 4):
        img = pygame.image.load(f'img/Ninja_Monk/bulet.png/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (20, 20))
        img = pygame.transform.scale(img, (int(img.get_width()) * 3, int(img.get_height()) * 3))
        list_bulet.append(img)
elif player.char_type == 'Samurai_Archer':
    img = pygame.image.load('img/Samurai_Archer/bulet.png/1.png').convert_alpha()
    img = pygame.transform.scale(img, (100, 100))
    list_bulet.append(img)



if player2.char_type == 'Fire vizard':
    for i in range(1, 12):
        img = pygame.image.load(f'img/Fire vizard/bulet.png/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (int(img.get_width()), int(img.get_height())))
        img = pygame.transform.scale(img, (200, 200))
        img = pygame.transform.flip(img, True, False)
        list_bulet_2.append(img)
elif player2.char_type == 'Lightning Mage':
    for i in range(1, 10):
        img = pygame.image.load(f'img/Lightning Mage/bulet.png/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (int(img.get_width()), int(img.get_height())))
        img = pygame.transform.scale(img, (200, 200))
        img = pygame.transform.flip(img, True, False)
        list_bulet_2.append(img)
elif player2.char_type == 'Ninja_Monk':
    for i in range(1, 4):
        img = pygame.image.load(f'img/Ninja_Monk/bulet.png/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (int(img.get_width()) * 3, int(img.get_height()) * 3))
        img = pygame.transform.scale(img, (20, 20))
        img = pygame.transform.flip(img, True, False)
        list_bulet_2.append(img)
elif player2.char_type == 'Samurai_Archer':
    img = pygame.image.load('img/Samurai_Archer/bulet.png/1.png').convert_alpha()
    img = pygame.transform.scale(img, (100, 100))
    img = pygame.transform.flip(img, True, False)
    list_bulet_2.append(img)

running = True
while running:
    status_bar()

    draw_b()
    player.draw_health_bar(player.hp, 20, 20)
    player2.draw_health_bar(player2.hp, 580, 20)

    player.draw_stamina_bar(player.stamina, 20, 55)
    player2.draw_stamina_bar(player2.stamina, 580, 55)

    bulet_group.update()
    bulet_group.draw(screen)


    player.draw()
    player2.draw()
    if not (player.dethent or player2.dethent):
        if time2 < 0 or time2 > 198:
            player.dead()
            player2.dead()
            player.update()
            player2.update()
            player.abilitys()
            player2.abilitys()
            player.attack()
            player2.attack()


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
                elif not player2.hurting:
                    player2.update_action(8)
                else:
                    player2.update_action(0)
                if not player2.ability:
                    player2.move(move_left_2, move_right_2, move_scor_2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if time2 < 0 or time2 > 198:
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
                    if event.key == pygame.K_w and player.alive and player.stamina > 5:
                        player.jump = True
                        jumpik.play()
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
                    if event.key == pygame.K_i and player2.alive and player2.stamina > 5:
                        player2.jump = True
                        jumpik.play()
                    if event.key == pygame.K_o and player2.stamina > 10 and not player2.in_air:
                        player2.swing = True
                        player2.atacks = True
                    if event.key == pygame.K_p and player2.stamina > 10 and not player2.in_air:
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
        if time2 > 0:
            if time // 4000 == 1:
                draw_text("01:" + str(time % 3600 // 60), RED, 468, 18, 35)
                if str(time2 % 3600 // 60) == '0':
                    draw_text(f'Round {rouds}', YELOW, 420, 200, 70)
                else:
                    draw_text(str(time2 % 3600 // 60), YELOW, 490, 200, 80)
                time2 -= 1
        if time2 < 0:
            if time // 3600 == 1:
                if time % 3600 // 60 < 10:
                    draw_text("01:0"+ str(time % 3600 // 60), RED, 468, 18, 35)
                else:
                    draw_text("01:"+ str(time % 3600 // 60), RED, 468, 18, 35)
            else:
                if time % 3600 // 60 < 10:
                    draw_text("00:0"+ str(time % 3600 // 60), RED, 468, 18, 35)
                else:
                    draw_text("00:"+ str(time % 3600 // 60), RED, 468, 18, 35)
        if time == 0:
            player.dethent = True
            player2.dethent = True
            player.round += 1
            player2.round += 1
        time = time - 1
        time2 -= 1
        time3 -= 1

        player.dead()
    else:
        if player.hp <= 0:
            player2.round += 1
        if player2.hp <= 0:
            player.round += 1

        rouds += 1
        restart_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    if '_' in player.char_type:
        name = player.char_type.replace('_', ' ')
    else:
        name = player.char_type
    draw_text(name, YELOW, 30, 12, 35)
    if '_' in player2.char_type:
        name1 = player2.char_type.replace('_', ' ')
    else:
        name1 = player2.char_type
    draw_text(name1, YELOW, 590, 12, 35)

    game_rounds()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()