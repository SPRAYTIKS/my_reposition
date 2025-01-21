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


# Создаем переменные громкостей музыки и эффектов
music_value = 0
effects_value = 0
pygame.init()

if __name__ == "__main__":
    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)

    fon = pygame.transform.scale(load_image('start_fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    btn_play = Button(screen, 400, 150, 200, 100, text='Play', fontSize=50, margin=20,
                      inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0),
                      overpressedColour=(0, 200, 20),
                      radius=20,
                      onClick=lambda: print('Click')
                      )

    intro_text = ["Музыка", "Эффекты", ]
    font_30 = pygame.font.Font(None, 30)
    text_coord = 73
    for i in range(2):
        string_rendered = font_30.render(intro_text[i], 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord - 10
        intro_rect.x = 860 - i * 30
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        text_coord += 75

    slider_m = Slider(screen, 840, 10, 150, 20, min=0, max=99, step=1, initial=0)
    gromkosti_m = TextBox(screen, 950, 50, 45, 40, fontSize=30)
    gromkosti_m.disable()
    font = pygame.font.Font(None, 50)
    text = font.render("Музыка", True, (100, 255, 100))

    slider_e = Slider(screen, 840, 110, 150, 20, min=0, max=99, step=1, initial=0)
    gromkosti_e = TextBox(screen, 950, 150, 45, 40, fontSize=30)
    gromkosti_e.disable()
    font = pygame.font.Font(None, 50)
    text = font.render("Эффекты", True, (100, 255, 100))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEDOWN:
            pygame_widgets.update(event)
        pygame.display.flip()
        gromkosti_m.setText(slider_m.getValue())
        gromkosti_e.setText(slider_e.getValue())
        # Обновляем громкость звуков
        music_value = slider_m.getValue()
        effects_value = slider_e.getValue()
    pygame.quit()
