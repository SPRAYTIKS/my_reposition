import os
import sys
import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox



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
    global slider_m, slider_e, open_settings, gromkosti_e, gromkosti_m, count_click, mode_play
    count_click += 1
    if (count_click == 1):
        open_settings = True
        screen.blit(fon, (0, 0))
        intro_text = ["Музыка", "Эффекты", ]
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
        if mode_play:
            choice_character()

def mode():
    global slider_m, slider_e, gromkosti_e, gromkosti_m, count_click, btn_1pl, btn_2pl
    slider_e.hide()
    slider_m.hide()
    gromkosti_m.hide()
    gromkosti_e.hide()
    screen.blit(fon, (0, 0))
    btn_1pl = Button(screen, 550, 300, 200, 100, text='1 plaer', fontSize=50, margin=20,
                      inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0),
                      overpressedColour=(0, 200, 20),
                      radius=20,
                      onClick=lambda: settings(False)
                      )
    btn_2pl = Button(screen, 250, 300, 200, 100, text='2 plaer', fontSize=50, margin=20,
                      inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0),
                      overpressedColour=(0, 200, 20),
                      radius=20,
                      onClick=lambda: settings(True)
                      )


def obrabotka(n):
    list_for_obrabotka.append(n)
    pl1_char = list_for_obrabotka[0]
    if not mode_play:
        return True
    if len(list_for_obrabotka) == 2:
        pl2_char = list_for_obrabotka[1]
        return True
    return False


def choice_character():
    character1 = [['Fighter', 30, 120], ['Fire Vizard', 100, 120], ['Kunoichi', 180, 120],
                  ['Lightning  Mage', 30, 190], ['Ninja Monk', 100, 190], ['Samurai', 180, 160],
                  ['Samurai Archer', 50, 260], ['Shinobi', 160, 260]]
    global mode_play, btn_1pl, btn_2pl
    btn_1pl.hide()
    btn_2pl.hide()
    if mode_play:
        for i in range(8):
            btn = Button(screen, character1[i][1], character1[i][2], 200, 100,
                         text=character1[i][0], fontSize=25, margin=20,
                         inactiveColour=(200, 90, 0), hoverColour=(150, 0, 0),
                         overpressedColour=(0, 200, 20),
                         radius=20,
                         onClick=lambda: obrabotka(i)
                         )
        for i in range(8):
            btn = Button(screen, character1[i][1] + 500, character1[i][2], 200, 100,
                         text=character1[i][0], fontSize=25, margin=20,
                         inactiveColour=(200, 90, 0), hoverColour=(150, 0, 0),
                         overpressedColour=(0, 200, 20),
                         radius=20,
                         onClick=lambda: obrabotka(i + 8)
                         )
    else:
        btn = Button(screen, character1[i][1] + 350, character1[i][2], 200, 100,
                     text=character1[i][0], fontSize=25, margin=20,
                     inactiveColour=(200, 90, 0), hoverColour=(150, 0, 0),
                     overpressedColour=(0, 200, 20),
                     radius=20,
                     onClick=lambda: obrabotka(i)
                     )

# Создаем переменные громкостей музыки и эффектов
music_value = 0
effects_value = 0
slider_m = slider_e = gromkosti_e = gromkosti_m = count_click = btn_1pl = btn_2pl = mode_play =  0
open_settings = False
pygame.init()
list_for_obrabotka = []
pl1_char = pl2_char = 0

size = width, height = 1000, 600
screen = pygame.display.set_mode(size)

fon = pygame.transform.scale(load_image('start_fon.jpg'), (width, height))
screen.blit(fon, (0, 0))
btn_play = Button(screen, 400, 150, 200, 100, text='Play', fontSize=50, margin=20,
                  inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0),
                  overpressedColour=(0, 200, 20),
                  radius=20,
                  onClick=lambda: settings()
                  )



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEDOWN:
        pygame_widgets.update(event)
    pygame.display.flip()
    # Обновляем громкость звуков
    if open_settings:
        gromkosti_m.setText(slider_m.getValue())
        gromkosti_e.setText(slider_e.getValue())
        # Обновляем громкость звуков
        music_value = slider_m.getValue()
        effects_value = slider_e.getValue()
pygame.quit()
