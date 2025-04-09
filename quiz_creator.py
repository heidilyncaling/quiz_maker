#Welcome notes
import pygame
import sys
import os

#initialize pygame
pygame.init()

#screen set up
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QUIZ CREATOR GAME")

#colors
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
DARK_PURPLE = (100, 0, 150)

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

#Progress bar
def draw_progress_bar(current, total):
    bar_width = 400
    bar_height = 30
    progress = int((current/total)) * bar_width
    pygame.draw.rect(screen, WHITE, [150, 400, progress, bar_height], 2)
    pygame.draw.rect(screen, DARK_PURPLE, [150, 400, progress, bar_height])
    percent = f"{int((current / total)*100)}%"
    draw_text(f"question {current} of {total} | {percent} completed", FONT, WHITE, screen, WIDTH // 2, HEIGHT // 4)

def main():
    start_screen()

    total_questions = int(get_input("How many questions will you input?"))
    questions_data = []
    for i in range(total_questions):
        screen.fill(PURPLE)
        draw_text((f"loading question of {i+1} of {total_questions}.."), FONT, WHITE, screen, WIDTH // 2, HEIGHT // 4)
        pygame.display.flip()
        pygame.time.wait(1000)

        screen.fill(PURPLE)
        draw_progress_bar(i+1, total_questions)
        pygame.display.flip()
        pygame.time.wait(3000)

        #Input question & options
        question = get_input("Enter your question:")
        option_A = get_input("A.")
        option_B = get_input("B.")
        option_C = get_input("C.")
        option_D = get_input("D.")

        #Input the correct answer.
        valid_answer = ['A', 'B', 'C', 'D']
        correct_answer = ''

        while correct_answer not in valid_answer:
            correct_answer = get_input("Enter answer A/B/C/D:").upper()
            if correct_answer not in valid_answer:
                draw_text("Please enter a/b/c/d ony."), FONT, WHITE, screen, WIDTH//2, HEIGHT//2
                pygame.display.flip()
                pygame.time.wait(1000)

        #store inputs
        question_text = f"Q: {question}\n"
        question_text += f"a) {option_A}\n"
        question_text += f"a) {option_B}\n"
        question_text += f"a) {option_C}\n"
        question_text += f"a) {option_D}\n"
        question_text += f"Answer: {correct_answer}\n"
        question_text += "-" * 50 + "\n"
        questions_data.append(question_text)

        pygame.time.wait(500)

    #Save in txt file.
    file_path = "quiz_data.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(questions_data)

    #Show ending message.
    screen.fill(PURPLE)
    draw_text("All inputs saved to quiz_data.txt", BIG_FONT, WHITE, screen, WIDTH // 2, HEIGHT // 3)
    pygame.display.flip()
    pygame.time.wait(1500)

    os.startfile(file_path)

    pygame.quit()
    sys.exit()
    
main()