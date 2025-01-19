import pygame

pygame.init()
# создаём окно игры
screen = pygame.display.set_mode((640, 480))
# задаём время таймера в миллисекундах
timer_duration = 5000
# запоминаем время начала таймера
start_time = pygame.time.get_ticks()

# игровой цикл
while True:
    # обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # закрываем окно игры и завершаем программу
            pygame.quit()
            quit()
    # проверяем, истекло ли время таймера
    current_time = pygame.time.get_ticks()
    if current_time - start_time >= timer_duration:
        # закрываем окно игры и завершаем программу
        pygame.quit()
        quit()
    # отображаем оставшееся время таймера на экране
    remaining_time = (timer_duration - (current_time - start_time)) // 1000 + 1
    font = pygame.font.Font(None, 36)
    text = font.render(f"Осталось времени: {remaining_time}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    # обновляем экран
    pygame.display.flip()
    # ждём некоторое время, чтобы не загружать процессор
    pygame.time.wait(10)