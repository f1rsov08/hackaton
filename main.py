import pygame
import memory
import puzzle
import puzzle1
import puzzle2
import puzzle3
import card

pygame.init()
size = width, height = 800, 900
screen = pygame.display.set_mode(size)
memory.memory(screen)
card.show_card(screen, 'data/cards/1.json')
puzzle1.puzzle(screen)
card.show_card(screen, 'data/cards/2.json')
memory.memory(screen)
card.show_card(screen, 'data/cards/3.json')
puzzle2.puzzle(screen)
card.show_card(screen, 'data/cards/4.json')
memory.memory(screen)
card.show_card(screen, 'data/cards/5.json')
puzzle3.puzzle(screen)
card.show_card(screen, 'data/cards/6.json')
pygame.quit()
