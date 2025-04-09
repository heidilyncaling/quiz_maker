#Welcome notes
import pygame
import sys

#initialize pygame
pygame.init()
pygame.mixer.init()

#screen set up
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QUIZ CREATOR GAME")

#colors
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)

#font
FONT = pygame.font.SysFont("Helvetica", 25)
BIG_FONT = pygame.font.SysFont("Helovetica", 50)

#center font in screen
def draw_text(text, font, color, surface, x, y, center=True):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(x,y)if center else(x,y))
    surface.blit(rendered,rect)

running = True
while running:
    screen.fill(PURPLE)
    draw_text("Welcome to Quiz Creator Game!", BIG_FONT, WHITE, screen, WIDTH // 2, HEIGHT // 3)
    draw_text("Click to Start!", FONT, WHITE, screen, WIDTH // 2, HEIGHT // 1.5)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False

pygame.quit()
sys.exit()

#Loop:
    #Input question
    #Input choices (a, b, c, d)
    #Input the correct answer.
    #Save in txt file.
    #Ask if input another or end program
#If no, end loop.

#Show ending message.
