import pygame, sys
from screen import screen
from constants import *

# font_path = pygame.font.match_font('Arial')
font_path = pygame.font.get_default_font()

def draw_text(text, center, color=white, size=30, bold=False, background=None,
              left=False):
    font = pygame.font.Font(font_path, size, bold=bold)
    if background:
        surface = font.render(text, True, color, background)
    else:
        surface = font.render(text, True, color)

    rect = surface.get_rect()
    rect.center = tuple(center)
    if left:
        rect.left = center[0]

    screen.blit(surface, rect)
    return rect

def draw_image(img, center):
    rect = img.get_rect()
    rect.center = tuple(center)
    screen.blit(img, rect)

def draw_focus_screen():
    p = screen.get_rect().center
    draw_text('+', p, size=100)

def focus_slide():
    screen.fill(background_color)
    draw_focus_screen()
    pygame.display.flip()


def simple_slide(text, size=100):
    screen.fill(background_color)
    p = screen.get_rect().center
    draw_text(text, p, size=size)
    pygame.display.flip()

def text_slide(text, size=30):
    screen.fill(background_color)
    lines = text.split('\n')
    rect = draw_text('test', (SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
                     size=size, color=background_color)
    height = rect.height + 6
    y = SCREEN_HEIGHT/2 - (len(lines)-1)*(height/2)
    for line in lines:
        draw_text(line.strip(), (SCREEN_WIDTH/2, y), size=size)
        y += height
    pygame.display.flip()

def recognize_slide(word, size=100):
    screen.fill(background_color)
    p = screen.get_rect().center
    draw_text(word, p, size=size)

    draw_text("1=unknown", (200, SCREEN_HEIGHT-100), size=50)
    draw_text("4=recognized", (SCREEN_WIDTH-250, SCREEN_HEIGHT-100), size=50)

    pygame.display.flip()
