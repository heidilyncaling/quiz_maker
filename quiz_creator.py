#Welcome notes.
import pygame

#initialize pygame
pygame.init()

#scree set up
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to QUIZ CREATOR!")

#colors
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)

#font
FONT = pygame.font.SysFont("Helvetica", 25)

running = True
while running:
    screen.fill(PURPLE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
#Loop:
    #Input question
    #Input choices (a, b, c, d)
    #Input the correct answer.
    #Save in txt file.
    #Ask if input another or end program
#If no, end loop.

#Show ending message.
