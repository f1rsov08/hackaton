import pygame
import memory
import puzzle
import card

pygame.init()
size = width, height = 800, 900
screen = pygame.display.set_mode(size)
memory.memory(screen)
card.show_card(screen, 'data/cards/1.json')
puzzle.puzzle(screen)
card.show_card(screen, 'data/cards/2.json')
memory.memory(screen)
card.show_card(screen, 'data/cards/3.json')
puzzle.puzzle(screen)
card.show_card(screen, 'data/cards/4.json')
memory.memory(screen)
card.show_card(screen, 'data/cards/5.json')
puzzle.puzzle(screen)
card.show_card(screen, 'data/cards/6.json')
pygame.quit()
