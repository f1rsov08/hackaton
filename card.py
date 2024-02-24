import pygame
import json
from load_image import load_image
import sys

class Card:
    def __init__(self, path):
        with open(path, 'r', encoding='utf8') as f:
            data = json.load(f)
        self.name = data["name"]
        self.description = data["description"]
        self.image = pygame.transform.scale(load_image(f'card_images/{data["image"]}'), (560, 360))

    def draw(self, screen):
        screen.blit(pygame.font.Font(None, 80).render(self.name, True, (255, 204, 153)), (20, 20))
        s, c = [], 0
        cs = 0
        for i in self.description.split():
            s.append(i)
            c += len(i)
            if c >= 30:
                screen.blit(pygame.font.Font(None, 40).render(' '.join(s), True, (255, 204, 153)), (20, 80 + cs * 30))
                s, c = [], 0
                cs += 1
        screen.blit(self.image, (20, 520))


def show_card(screen, path):
    screen.fill((70, 149, 151))
    card = Card(path)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        screen.fill((70, 149, 151))
        card.draw(screen)

        pygame.display.flip()
        clock.tick(60)
