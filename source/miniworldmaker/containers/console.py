import os
from miniworldmaker.containers.container import Container
import pygame


class Console(Container):

    def __init__(self, lines=5):
        super().__init__()
        self._lines = lines
        self._height = self._lines * 20
        self._text_queue = []
        self.margin_first = 10
        self.margin_last = 5
        self.row_height = 25
        self.row_margin = 10
        self.margin_left = 10
        self.margin_right = 10
        self._dirty = 1


    def repaint(self):
        if self.dirty:
            self.surface.fill((255, 255, 255))
            package_directory = os.path.dirname(os.path.abspath(__file__))
            myfont = pygame.font.SysFont("monospace", 15)
            for i, text in enumerate(self._text_queue):
                row = pygame.Surface((self.width - (self.margin_left + self.margin_right), self.row_height))
                row.fill((200, 200, 200))
                label = myfont.render(text, 1, (0, 0, 0))
                row.blit(label, (10, 5))
                self.surface.blit(row, (self.margin_left, self.margin_first + i * self.row_height + i * self.row_margin))
        self.window.repaint_areas.append(self.rect)
        self.dirty = 0

    def max_height(self):
        width = self.margin_first
        for widget in self.widgets:
            width += widget.width + 5
        return width - 5

    @property
    def lines(self):
        self._lines = int(self.height - self.margin_first - self.margin_last) / (self.row_height + self.row_margin)
        return self._lines

    def newline(self, text):
        self._text_queue.append(text)
        if len(self._text_queue) > self.lines:
            self._text_queue.pop(0)
        self.dirty = 1
