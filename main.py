import pygame
import memory

pygame.init()
size = width, height = 800, 900
screen = pygame.display.set_mode(size)
memory.memory(screen)
pygame.quit()
