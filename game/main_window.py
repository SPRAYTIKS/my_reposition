import os
import sys
import pygame


def load_image(name, color_key=None):
    fullname = os.path.join('img', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image
pygame.init()


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1429, 800
    screen = pygame.display.set_mode(size)
    intro_text = ["Приветствую тебя, новобранец, ты попал в Battle of Heroes", "", "", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon_start.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font_45 = pygame.font.Font(None, 45)
    font_30 = pygame.font.Font(None, 30)
    text_coord = 75
    string_rendered = font_45.render(intro_text[0], 1, pygame.Color('green'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord - 10
    intro_rect.x = 175
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)
    text_coord = 75

    all_sprites = pygame.sprite.Group()
    button = pygame.sprite.Sprite()
    button.image = load_image("button_start.png")
    button.rect = button.image.get_rect()

    button.rect.x = 500
    button.rect.y = 200
    all_sprites.add(button)
    all_sprites.draw(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()


pygame.init()

size = (1000, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Mortal Kombat')

run = False

clock = pygame.time.Clock()

player_image = load_image('hero_stan.gif')
player_image = pygame.transform.scale(player_image, (58*3, 89*3))

player_image_second = load_image('hero_stan.gif')
player_image_second = pygame.transform.scale(player_image_second, (58*3, 89*3))
player_image_second = pygame.transform.flip(player_image_second, True, False)

map_image = load_image('les.jpg')
map_image = pygame.transform.scale(map_image, (1000, 600))


class Player_first:
    def __init__(self, image, pos):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_jump = False
        self.do = False
        self.frease = 0
        self.frease_2 = 0
        self.jump_count = 8

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def border(self):
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.left < 0:
            self.rect.left = 0


    def move(self):
        key = pygame.key.get_pressed()
        if not key[pygame.K_a] and not key[pygame.K_d] and not key[pygame.K_w] and not key[pygame.K_s]:
            self.frease += 0.2
            if self.frease > 13:
                self.frease -= 13
            pers_img = ['idle_1.png', 'idle_2.png', 'idle_3.png', 'idle_4.png', 'idle_5.png', 'idle_6.png',
                        'idle_7.png', 'idle_6.png', 'idle_5.png', 'idle_4.png', 'idle_3.png', 'idle_2.png',
                        'idle_1.png']
            self.image = load_image(pers_img[int(self.frease)]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (58 * 3.3, 89 * 3.3))
        if key[pygame.K_s]:
            pers_img = 'sit_3.png'
            self.image = load_image(pers_img).convert_alpha()
            self.image = pygame.transform.scale(self.image, (58 * 3.3, 89 * 3.3))
        if key[pygame.K_d]:
            self.frease_2 += 0.2
            if self.frease_2 > 4:
                self.frease_2 -= 4
            self.rect.x += 5
            pers_img = ['102.png', '103.png', '112.png', '113.png']
            self.image = load_image(pers_img[int(self.frease_2)]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (58 * 3.3, 89 * 3.3))
        if key[pygame.K_a]:
            self.rect.x -= 5
        if not self.is_jump:
            if key[pygame.K_w]:
                self.is_jump = True
        else:
            if self.jump_count >= -8:
                if self.jump_count > 0:
                    self.rect.y -= (self.jump_count ** 2) // 2
                else:
                    self.rect.y += (self.jump_count ** 2) // 2
                self.jump_count -= 0.5
            else:
                print(self.rect.y)
                self.is_jump = False
                self.jump_count = 8
        self.border()


class Player_second:
    def __init__(self, image, pos):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_jump = False
        self.do = False
        self.frease = 0
        self.jump_count = 8

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def border(self):
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.left < 0:
            self.rect.left = 0


    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_l]:
            self.rect.x += 5
        if key[pygame.K_j]:
            self.rect.x -= 5
        if not self.is_jump:
            if key[pygame.K_i]:
                self.is_jump = True
        else:
            if self.jump_count >= -8:
                if self.jump_count > 0:
                    self.rect.y -= (self.jump_count ** 2) // 2
                else:
                    self.rect.y += (self.jump_count ** 2) // 2
                self.jump_count -= 0.5
            else:
                print(self.rect.y)
                self.is_jump = False
                self.jump_count = 8
        self.border()



player = Player_first(player_image, (100, 445))
player_2 = Player_second(player_image_second, (900, 450))
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
    screen.fill((255, 255, 255))
    screen.blit(map_image, (0, 0))
    player.draw(screen)
    player_2.draw(screen)
    player.move()
    player_2.move()
    pygame.display.flip()

    clock.tick(60)
pygame.quit()