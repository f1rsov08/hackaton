import pygame
from pygame.locals import *
import time
import tkinter as tk
from tkinter import messagebox as tmsg
import random
import os

root = tk.Tk()
root.withdraw()


class Puzzle:
    def __init__(self):
        self.x = 120
        self.y = 150

    def draw(self, win):
        for i in range(4):
            pygame.draw.line(win, (200, 200, 200), (self.x - 4, self.y + 90 * i),
                             (self.x + 5 + 3 * 90, self.y + 90 * i), 10)

        for i in range(4):
            pygame.draw.line(win, (200, 200, 200), (self.x + 90 * i, self.y), (self.x + 90 * i, self.y + 3 * 90), 10)


puzzle = Puzzle()


class Pieces:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("lucida", 60)
        self.wd = 90
        self.loc = [[126 + self.wd * 0, 156 + self.wd * 0, 1], [126 + self.wd * 1, 156 + self.wd * 0, 2],
                    [126 + self.wd * 2, 156 + self.wd * 0, 3],
                    [126 + self.wd * 0, 156 + self.wd * 1, 4], [126 + self.wd * 1, 156 + self.wd * 1, 5],
                    [126 + self.wd * 2, 156 + self.wd * 1, 6],
                    [126 + self.wd * 0, 156 + self.wd * 2, 7], [126 + self.wd * 1, 156 + self.wd * 2, 8]]
        self.solved_loc = [[126 + self.wd * 0, 156 + self.wd * 0, 1], [126 + self.wd * 1, 156 + self.wd * 0, 2],
                           [126 + self.wd * 2, 156 + self.wd * 0, 3],
                           [126 + self.wd * 0, 156 + self.wd * 1, 4], [126 + self.wd * 1, 156 + self.wd * 1, 5],
                           [126 + self.wd * 2, 156 + self.wd * 1, 6],
                           [126 + self.wd * 0, 156 + self.wd * 2, 7], [126 + self.wd * 1, 156 + self.wd * 2, 8]]

        self.empty_spot = [126 + self.wd * 2, 156 + self.wd * 2, 0]

        # Load the images from the "images" folder
        self.image_size = 80  # Width and height of each image
        self.images = {}
        image_files = os.listdir("images/monument")
        for image_file in image_files:
            image = pygame.image.load(os.path.join(f"images/monument", image_file))
            image = pygame.transform.scale(image, (self.image_size, self.image_size))
            self.images[image_file.split(".")[0]] = image

    def show(self, win):
        for l in self.loc:
            pygame.draw.rect(win, (50, 30, 20), (l[0], l[1], 80, 80))
            if l[2] != 0:
                win.blit(self.images[str(l[2])], (l[0], l[1]))

    def check_solved(self):
        if self.solved_loc == self.loc:
            tmsg.showinfo("Solved", "Congratulations! You have solved the puzzle.")
            shuffle(self)
            return False
        else:
            return True

    def search_and_shift(self, pos):
        pressed = False
        for i in range(len(self.loc)):
            if pos[0] > self.loc[i][0] and pos[0] < self.loc[i][0] + 80 and pos[1] > self.loc[i][1] and pos[1] < \
                    self.loc[i][1] + 80:
                pressed = True
                break
        if pressed:
            if self.loc[i][0] + 90 == self.empty_spot[0] and self.loc[i][1] == self.empty_spot[1]:
                temp = self.loc[i]
                self.empty_spot[2] = self.loc[i][2]
                self.loc[i] = self.empty_spot
                self.empty_spot = temp
                self.empty_spot[2] = 0

            elif self.loc[i][0] - 90 == self.empty_spot[0] and self.loc[i][1] == self.empty_spot[1]:
                temp = self.loc[i]
                self.empty_spot[2] = self.loc[i][2]
                self.loc[i] = self.empty_spot
                self.empty_spot = temp
                self.empty_spot[2] = 0

            elif self.loc[i][0] == self.empty_spot[0] and self.loc[i][1] + 90 == self.empty_spot[1]:
                temp = self.loc[i]
                self.empty_spot[2] = self.loc[i][2]
                self.loc[i] = self.empty_spot
                self.empty_spot = temp
                self.empty_spot[2] = 0

            elif self.loc[i][0] == self.empty_spot[0] and self.loc[i][1] - 90 == self.empty_spot[1]:
                temp = self.loc[i]
                self.empty_spot[2] = self.loc[i][2]
                self.loc[i] = self.empty_spot
                self.empty_spot = temp
                self.empty_spot[2] = 0


pieces = Pieces()


def shuffle(pieces):
    for _ in range(1000):
        i = random.randint(0, 7)
        if pieces.loc[i][0] + 90 == pieces.empty_spot[0] and pieces.loc[i][1] == pieces.empty_spot[1]:
            temp = pieces.loc[i]
            pieces.empty_spot[2] = pieces.loc[i][2]
            pieces.loc[i] = pieces.empty_spot
            pieces.empty_spot = temp
            pieces.empty_spot[2] = 0

        elif pieces.loc[i][0] - 90 == pieces.empty_spot[0] and pieces.loc[i][1] == pieces.empty_spot[1]:
            temp = pieces.loc[i]
            pieces.empty_spot[2] = pieces.loc[i][2]
            pieces.loc[i] = pieces.empty_spot
            pieces.empty_spot = temp
            pieces.empty_spot[2] = 0


        elif pieces.loc[i][0] == pieces.empty_spot[0] and pieces.loc[i][1] - 90 == pieces.empty_spot[1]:
            temp = pieces.loc[i]
            pieces.empty_spot[2] = pieces.loc[i][2]
            pieces.loc[i] = pieces.empty_spot
            pieces.empty_spot = temp
            pieces.empty_spot[2] = 0


def main():
    pygame.init()
    background_image = pygame.image.load("images/chuvashiya.png")
    win = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Puzzle")
    # Load the background image
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pieces.search_and_shift(pos)
                pieces.check_solved()
        win.fill((10, 10, 10))
        puzzle.draw(win)
        pieces.show(win)
        # Draw the background image
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
