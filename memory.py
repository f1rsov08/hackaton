import pygame
from load_image import load_image
import random
from pprint import pprint

IMAGE = None


class MemoryCard:
    def __init__(self, id_):
        self.id = id_
        self.image = pygame.transform.scale(load_image(f'memory/{id_}.jpg'), (60, 80))
        self.open = False
        self.open_time = 0

    def get_click(self):
        global IMAGE
        if IMAGE is None:
            IMAGE = self
        elif IMAGE != self:
            self.open = True
            IMAGE.open = True
            if self.id == IMAGE.id:
                self.open_time = float('inf')
                IMAGE.open_time = float('inf')
            else:
                self.open_time = pygame.time.get_ticks()
                IMAGE.open_time = pygame.time.get_ticks()
            IMAGE = None

    def update(self):
        if pygame.time.get_ticks() - self.open_time >= 30:
            self.open = False

    def draw(self, screen, x, y):
        global IMAGE
        if IMAGE == self or self.open:
            screen.blit(self.image, (x, y))
        else:
            pygame.draw.rect(screen, (229, 81, 55), pygame.Rect(x, y, 60, 80), width=5)
            pygame.draw.rect(screen, (255, 204, 153), pygame.Rect(x + 5, y + 5, 50, 70), width=0)

    def __str__(self):
        return f'MemoryCard({self.id})'

    def __repr__(self):
        return f'MemoryCard({self.id})'


def memory(screen):
    board = [[MemoryCard(0), MemoryCard(0), MemoryCard(1), MemoryCard(1)],
             [MemoryCard(2), MemoryCard(2), MemoryCard(3), MemoryCard(3)],
             [MemoryCard(4), MemoryCard(4), MemoryCard(5), MemoryCard(5)],
             [MemoryCard(6), MemoryCard(6), MemoryCard(7), MemoryCard(7)]]
    for i in board:
        random.shuffle(i)
    board = list(map(list, zip(*board[::-1])))
    for i in board:
        random.shuffle(i)
    pprint(board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = x % 80, y % 100
                board[y][x].get_click()
        screen.fill((70, 149, 151))
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j].draw(screen, 80 * i, 100 * j)
        pygame.display.flip()


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 255))
memory(screen)
pygame.quit()
