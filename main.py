import pygame
import puzzle

pygame.init()
size = width, height = 800, 900
screen = pygame.display.set_mode(size)
puzzle.puzzle(screen)
pygame.quit()
