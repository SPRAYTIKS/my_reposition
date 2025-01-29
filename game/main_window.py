import os
import sys
import pygame
import pygame_widgets
from pygame_widgets.button import Button, ButtonArray
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


def draw_b():
    screen.blit(fon, (0, 0))


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
                img = pygame.transform.scale(img,
                                             (int(img.get_width() * 4), int(img.get_height() * 4)))
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


def load_image(name, color_key=None):
    fullname = os.path.join('img', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def settings(*args):
    global slider_m, slider_e, open_settings, gromkosti_e, gromkosti_m, count_click, \
        mode_play, start, locat, plaer
    count_click += 1
    if (count_click == 1):
        open_settings = True
        screen.blit(fon, (0, 0))
        intro_text = ["Музыка", "Эффекты"]
        font_30 = pygame.font.Font(None, 30)
        text_coord = 73
        for i in range(2):
            string_rendered = font_30.render(intro_text[i], 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord - 10
            intro_rect.x = 860 - i * 15
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            text_coord += 75
        text1 = ['Первый игрок:', 'a - влево', 'd - вправо', 'w - прыжок', 'r - обычный удар',
                 'f - способность']
        text2 = ['Второй игрок:', 'j - влево', 'l - вправо', 'i - прыжок', 'o - обычный удар',
                 'p - способность']
        text_coord = 60
        for i in range(6):
            string_rendered = pygame.font.Font(None, 24).render(text1[i], 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord - 10
            intro_rect.x = 50
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            text_coord += 24
        text_coord = 60
        for i in range(6):
            string_rendered = pygame.font.Font(None, 24).render(text2[i], 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord - 10
            intro_rect.x = 220
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            text_coord += 24

        slider_m = Slider(screen, 840, 10, 150, 20, min=0, max=99, step=1, initial=0)
        font = pygame.font.Font(None, 50)
        text = font.render("Музыка", True, (100, 255, 100))
        gromkosti_m = TextBox(screen, 950, 50, 45, 40, fontSize=30)
        gromkosti_m.disable()

        slider_e = Slider(screen, 840, 110, 150, 20, min=0, max=99, step=1, initial=0)
        font = pygame.font.Font(None, 50)
        text = font.render("Эффекты", True, (100, 255, 100))
        gromkosti_e = TextBox(screen, 950, 150, 45, 40, fontSize=30)
        gromkosti_e.disable()

        text = font.render("Эффекты", True, (100, 255, 100))
    elif count_click == 2:
        mode()
    elif count_click == 3:
        if args:
            mode_play = args[0]
        choice_character()
    elif count_click == 4:
        if args:
            pl1_char = args[0]
        if mode_play:
            choice_character(2)
        else:
            location()
    elif count_click == 5:
        if args and mode_play:
            pl2_char = args[0]
            location()
        else:
            locat = args[0]
    elif count_click == 6:
        locat = args[0]


def mode():
    global slider_m, slider_e, gromkosti_e, gromkosti_m, count_click, btn_1pl, btn_2pl
    slider_e.hide()
    slider_m.hide()
    gromkosti_m.hide()
    gromkosti_e.hide()
    screen.blit(fon, (0, 0))
    btn_play.hide()
    btn_1pl = Button(screen, 550, 300, 200, 100, text='1 player', fontSize=50, margin=20,
                     colour=(128, 128, 128),
                     inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0),
                     overpressedColour=(0, 200, 20),
                     radius=20,
                     onClick=lambda: settings(False)
                     )
    btn_2pl = Button(screen, 250, 300, 200, 100, text='2 player', fontSize=50, margin=20,
                     inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0),
                     overpressedColour=(0, 200, 20), colour=(128, 128, 128),
                     radius=20,
                     onClick=lambda: settings(True)
                     )


def persona(n):
    character1 = ['Fighter', 'Fire Vizard', 'Kunoichi', 'Lightning Mage', 'Ninja_Monk',
                  'Samurai', 'Samurai_Archer', 'Shinobi']
    global mode_play, btn_choice, red_flag, plaer
    btn_choice = Button(screen, 380, 520, 120, 70, text='Выбрать', fontSize=30, margin=20,
                        inactiveColour=(128, 128, 128), hoverColour=(150, 0, 0),
                        overpressedColour=(0, 200, 20),
                        radius=20,
                        onClick=lambda: settings(n), red_flag=False
                        )
    plaer = Player(character1[n], 850, 300, True)


def choice_character(*args):
    global mode_play, btn_1pl, btn_2pl, buttonChar, btn_play, btn_choice
    character1 = ['Fighter', 'Fire Vizard', 'Kunoichi', 'Lightning Mage', 'Ninja Monk',
                  'Samurai', 'Samurai Archer', 'Shinobi']
    if not args:
        btn_1pl.hide()
        btn_2pl.hide()
        btn_play.hide()
        if btn_choice != 0:
            btn_choice.hide()
        i = 0
    else:
        buttonChar.hide()
        btn_choice.hide()
        screen.blit(fon, (0, 0))
        i = 1
    intro_text = ['Игрок(1) выберите персонажа:', 'Игрок(2), выберите персонажа:']
    font_35 = pygame.font.Font(None, 35)
    text_coord = 35
    string_rendered = font_35.render(intro_text[i], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord - 10
    intro_rect.x = 250
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    buttonChar = ButtonArray(screen, 150, 50, 600, 450, (2, 4), colour=(128, 128, 128),
                             border=40, texts=character1,
                             onClicks=(
                                 lambda: persona(0), lambda: persona(1), lambda: persona(2),
                                 lambda: persona(3),
                                 lambda: persona(4), lambda: persona(5), lambda: persona(6),
                                 lambda: persona(7)))


def location():
    global buttonChar, btnLocations, btn_choice, plaer
    plaer = 0
    buttonChar.hide()
    btn_choice.hide()
    screen.blit(fon, (0, 0))
    locations_map = []
    # for i in range(3):
    # im = pygame.Surface((180, 400))
    # pers = pygame.transform.scale(load_image('btn_3.png'), (width, height))
    # im.blit(pers, (0, 0))
    # locations_map.append(im)
    btnLocations = ButtonArray(screen, 200, 50, 600, 450, (1, 3), colour=(128, 128, 128),
                               image=locations_map,
                               border=20,
                               onClicks=(
                                   lambda: settings(0), lambda: settings(1), lambda: settings(2)))


# Создаем переменные громкостей музыки и эффектов
music_value = 0
effects_value = btn_play = fon = plaer = 0
slider_m = slider_e = gromkosti_e = gromkosti_m = count_click = btn_1pl \
    = btn_2pl = mode_play = btn_choice = 0
open_settings = red_flag = False
pygame.init()
list_for_obrabotka = []
pl1_char = pl2_char = buttonChar = btnLocations = locat = 0

size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60


def start():
    global btn_play, fon, count_click
    count_click = 0
    fon = pygame.transform.scale(load_image('start_fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    btn_play = Button(screen, 400, 150, 200, 100, text='Play', fontSize=50, margin=20,
                      inactiveColour=(128, 128, 128), hoverColour=(150, 0, 0),
                      overpressedColour=(0, 200, 20),
                      radius=20,
                      onClick=lambda: settings()
                      )


start()
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    pygame_widgets.update(events)
    pygame.display.flip()
    # Обновляем громкость звуков
    if open_settings:
        gromkosti_m.setText(slider_m.getValue())
        gromkosti_e.setText(slider_e.getValue())
        # Обновляем громкость звуков
        music_value = slider_m.getValue()
        effects_value = slider_e.getValue()
    if plaer != 0:
        draw_b()
        plaer.draw()
        plaer.update()
        plaer.update_action(0)
    clock.tick(FPS)
pygame.quit()

