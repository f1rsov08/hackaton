import pygame
from load_image import load_image
import random

IMAGE = None
LAST_OPEN = float('-inf')
MOVES = 12


class MemoryCard:
    def __init__(self, id_):
        self.id = id_
        self.image = pygame.transform.scale(load_image(f'memory/{id_}.jpg'), (160, 160))
        self.open = False
        self.open_time = 0

    def get_click(self):
        global IMAGE, LAST_OPEN, MOVES
        if not self.open:
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
                    LAST_OPEN = pygame.time.get_ticks()
                    MOVES -= 1
                IMAGE = None

    def update(self):
        if pygame.time.get_ticks() - self.open_time >= 600:
            self.open = False

    def draw(self, screen, x, y):
        global IMAGE
        if IMAGE == self or self.open:
            screen.blit(self.image, (x, y))
        else:
            pygame.draw.rect(screen, (255, 204, 153), pygame.Rect(x + 5, y + 5, 150, 150), width=0)
        pygame.draw.rect(screen, (229, 81, 55), pygame.Rect(x, y, 160, 160), width=5)

    def __str__(self):
        return f'MemoryCard({self.id})'

    def __repr__(self):
        return f'MemoryCard({self.id})'


def memory(screen, top_text=''):
    global MOVES
    board = [[MemoryCard(0), MemoryCard(0), MemoryCard(1), MemoryCard(1)],
             [MemoryCard(2), MemoryCard(2), MemoryCard(3), MemoryCard(3)],
             [MemoryCard(4), MemoryCard(4), MemoryCard(5), MemoryCard(5)],
             [MemoryCard(6), MemoryCard(6), MemoryCard(7), MemoryCard(7)]]
    for i in board:
        random.shuffle(i)
    board = list(map(list, zip(*board[::-1])))
    for i in board:
        random.shuffle(i)

    font = pygame.font.Font(None, 50)

    MOVES = 12
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.time.get_ticks() - LAST_OPEN >= 600:
                mx, my = event.pos
                mx, my = mx - 20, my - 110
                x, y = mx // 200, my // 200
                if mx >= 0 and my >= 0 and x < len(board[0]) and y < len(board) and mx % 200 <= 160 and my % 200 <= 160:
                    board[y][x].get_click()

        screen.fill((70, 149, 151))
        screen.blit(font.render(top_text, True, (255, 204, 153)), (40, 20))
        screen.blit(font.render(f'Осталось попыток: {MOVES}', True, (255, 204, 153)), (40, 60))
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j].update()
                board[i][j].draw(screen, 20 + 200 * j, 110 + 200 * i)

        if MOVES < 0:
            running = False
            memory(screen, 'Вы проиграли, попробуйте еще раз')
        pygame.display.flip()
        clock.tick(60)


pygame.init()
size = width, height = 800, 900
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 255))
memory(screen)
pygame.quit()
