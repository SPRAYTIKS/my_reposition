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
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    intro_text = ["Приветствую тебя, новобранец, ты попал в Battle of Heroes", "", "", ""]

    fon = pygame.transform.scale(load_image('start_fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font_45 = pygame.font.Font(None, 45)
    font_30 = pygame.font.Font(None, 30)
    text_coord = 75
    string_rendered = font_45.render(intro_text[0], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord - 10
    intro_rect.x = 60
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)
    text_coord = 75

    all_sprites = pygame.sprite.Group()
    button = pygame.sprite.Sprite()
    button.image = load_image("btn_start.png", 'white')
    button.rect = button.image.get_rect()

    im = load_image('btn_3.png')
    im = pygame.transform.scale(im, (100, 100))
    button_win3 = pygame.sprite.Sprite()
    button_win3.image = im
    button_win3.rect = button_win3.image.get_rect()

    im = load_image('btn_1.png')
    im = pygame.transform.scale(im, (100, 100))
    button_win1 = pygame.sprite.Sprite()
    button_win1.image = im
    button_win1.rect = button_win3.image.get_rect()


    button.rect.x = 340
    button.rect.y = 130

    button_win3.rect.x = 350
    button_win3.rect.y = 250

    button_win1.rect.x = 540
    button_win1.rect.y = 250
    all_sprites.add(button)
    all_sprites.add(button_win3)
    all_sprites.add(button_win1)
    all_sprites.draw(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.MOUSEDOWN:

        pygame.display.flip()
    pygame.quit()
