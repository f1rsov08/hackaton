import pygame


class Piece:
    def __init__(self, piece_size, p_id):
        self.piece_size = piece_size
        self.p_id = p_id

        if self.p_id != 9:
            img_path = f'images/monument/{self.p_id + 1}.png'
            self.img = pygame.image.load(img_path)
            self.img = pygame.transform.scale(self.img, self.piece_size)
        else:
            self.img = None
