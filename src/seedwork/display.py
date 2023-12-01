import pygame
from PIL import Image
import numpy as np


def display_simulation(images: list[Image], fps: int) -> None:
    pygame.init()

    frame_size = images[0].size
    screen = pygame.display.set_mode(frame_size)
    pygame.display.set_caption("Forest Fire Simulation")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)

    running = True
    idx = 0

    while running and idx < len(images):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        np_image = np.array(images[idx])
        pygame_image = pygame.surfarray.make_surface(np.transpose(np_image, (1, 0, 2)))
        screen.blit(pygame_image, (0, 0))

        text_surface = font.render(f'Generation: {idx+1}', True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()

        idx += 1
        clock.tick(fps)

    exit_text_surface = font.render("Press Q to exit", True, (255, 255, 255))
    text_rect = exit_text_surface.get_rect(center=(frame_size[0] // 2, frame_size[1] // 2))
    screen.blit(exit_text_surface, text_rect)
    pygame.display.flip()
    waiting_for_exit = True
    while waiting_for_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_exit = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                waiting_for_exit = False

    pygame.quit()
