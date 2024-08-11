import pygame
from pygame.locals import *
from dotenv import load_dotenv, find_dotenv

import os
import gemini
import cam
import capttypes
import speech

load_dotenv(find_dotenv())

img_dir = os.getenv("IMG_DIR")

pygame.init()


def square(colorb, text):
    squareb = pygame.Surface((400, 240))
    color = pygame.Color(colorb)
    squareb.fill(color)
    text = font.render(text, True, (255, 255, 255))
    text_rect = text.get_rect(center=(200, 120))
    squareb.blit(text, text_rect)
    return squareb


font = pygame.font.SysFont("freesans", 45)

screen = pygame.display.set_mode((800, 480), FULLSCREEN | SCALED, display=0)

run = True
while run:
    pygame.time.delay(100)

    news_button = square(("#7D8D87"), "News")
    tv_button = square(("#B87F45"), "Tv Series/Movies")
    land_button = square(("#CBC497"), "Landscapes")
    sports_button = square(("#9EB45B"), "Sports")

    screen.blit(news_button, (0, 0))
    screen.blit(tv_button, (400, 0))
    screen.blit(land_button, (0, 240))
    screen.blit(sports_button, (400, 240))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            questiontype = ""
            if news_button.get_rect(topleft=(0, 0)).collidepoint(pos):
                questiontype = "NEWS"
            if tv_button.get_rect(topleft=(400, 0)).collidepoint(pos):
                questiontype = "TVMOVIES"
            if land_button.get_rect(topleft=(0, 240)).collidepoint(pos):
                questiontype = "LANDSCAPES"
            if sports_button.get_rect(topleft=(400, 240)).collidepoint(pos):
                questiontype = "SPORTS"

            warn_sign = square(("#000000"), "Checking A.I.")

            screen.blit(warn_sign, (200, 120))
            pygame.display.update()

            filename = cam.capture(img_dir)
            qtype = capttypes.select(questiontype)
            question = qtype.question()
            answer = qtype.post_process(gemini.ask(question, filename))

            speech.speak(answer)
