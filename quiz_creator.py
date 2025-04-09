#Welcome notes
import pygame
import sys

#initialize pygame
pygame.init()

#screen set up
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QUIZ CREATOR GAME")

#colors
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)

#font
FONT = pygame.font.SysFont("Helvetica", 25)
BIG_FONT = pygame.font.SysFont("Helvetica", 50)

#sfx
ding_sound = pygame.mixer.Sound("C:/Users/HANZ JOSEPH CALING/Downloads/sounds/ding.wav.mp3")
pygame.mixer.music.load("C:/Users/HANZ JOSEPH CALING/Downloads/sounds/from_the_start.mp3")

#center font in screen
def draw_text(text, font, color, surface, x, y, center=True):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(x,y)if center else(x,y))
    surface.blit(rendered,rect)

#Input question
def get_input(prompt):
    user_input = ''
    active = True
    while active:
        screen.fill(PURPLE)
        draw_text(prompt, FONT, WHITE, screen, WIDTH // 2, HEIGHT // 3)
        draw_text(user_input + '|', FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
    return user_input.strip()

#Input choices (a, b, c, d)
#Input the correct answer.
#Save in txt file.
#Ask if input another or end program
#If no, end loop.

def start_screen():
    running = True
    pygame.mixer.music.play(-1,0.0)
    while running:
        screen.fill(PURPLE)
        draw_text("Welcome to Quiz Creator Game!", BIG_FONT, WHITE, screen, WIDTH // 2, HEIGHT // 3)
        draw_text("Click to Start!", FONT, WHITE, screen, WIDTH // 2, HEIGHT // 1.5)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ding_sound.play()  # 🔊 plays the ding sound
                running = False

def main():
    start_screen()
    question = get_input("Enter your question:")
    print(question)

    option_A = get_input("A.")
    option_B = get_input("B.")
    option_C = get_input("C.")
    option_D = get_input("D.")

    valid_answer = ['A', 'B', 'C', 'D']
    correct_answer = ''

    while correct_answer not in valid_answer:
        correct_answer = get_input("Enter answer A/B/C/D:"),upper()
        if correct_answer not in valid_answer:
            print("Please enter a/b/c/d ony.")
    print(correct_answer)

    pygame.quit()
    sys.exit()
    
main()

#Show ending message.