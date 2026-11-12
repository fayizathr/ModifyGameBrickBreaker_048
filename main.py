import pygame
import random

pygame.init()

# Dimensions of the screen
WIDTH, HEIGHT = 600, 500

# Modern Arcade Colors
BLACK = (15, 15, 20)
WHITE = (255, 255, 255)
NEON_BLUE = (0, 243, 255)
NEON_PURPLE = (188, 19, 254)
NEON_GREEN = (57, 255, 20)
NEON_YELLOW = (255, 230, 0)
NEON_RED = (255, 42, 109)
GRAY = (100, 100, 100)

font = pygame.font.Font('freesansbold.ttf', 16)
font_large = pygame.font.Font('freesansbold.ttf', 32)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker - Arcade Edition")

# to control the frame rate
clock = pygame.time.Clock()
FPS = 60  # Ditingkatkan jadi 60 FPS agar gerakan lebih mulus dan responsif


