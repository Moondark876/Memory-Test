from enum import Enum
import pygame
import os

pygame.init()

class Colours(Enum):

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, r, g, b):
        self.rgb = (r, g, b)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    CYAN = (0, 255, 255)
    LIME = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    MAROON = (128, 0, 0)
    OLIVE = (128, 128, 0)
    NAVY = (0, 0, 128)
    TEAL = (0, 128, 128)
    PINK = (255, 192, 203)
    LIGHT_BLUE = (173, 216, 230)
    DARK_BLUE = (0, 0, 128)
    DARK_GREEN = (0, 100, 0)
    DARK_RED = (128, 0, 0)
    DARK_ORANGE = (255, 140, 0)
    DARK_PURPLE = (128, 0, 128)
    DARK_CYAN = (0, 128, 128)
    DARK_LIME = (0, 128, 0)
    DARK_MAGENTA = (128, 0, 128)
    DARK_SILVER = (192, 192, 192)
    DARK_GRAY = (64, 64, 64)
    DARK_MAROON = (64, 0, 0)
    DARK_OLIVE = (64, 64, 0)
    DARK_NAVY = (0, 0, 64)
    DARK_TEAL = (0, 64, 64)
    DARK_PINK = (192, 128, 128)
    DARK_LIGHT_BLUE = (96, 128, 255)


rectangle = pygame.Rect(60, 370, 200, 50)
rectangle_2 = pygame.Rect(360, 370, 200, 50)
BIGFONT = pygame.font.Font(os.path.join("Assets", "Pixeltype.ttf"), 100)
FONT = pygame.font.Font(os.path.join("Assets", "Pixeltype.ttf"), 75)
NEWWORD_EVENT = pygame.event.custom_type()
# (self.screen.get_width() // 2 - x.get_width(), self.screen.get_height() // 2 - x.get_height())
coin = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "coin.png")), (120, 90))