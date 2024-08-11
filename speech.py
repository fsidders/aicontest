from gtts import gTTS
from io import BytesIO
import pygame


def speak(text, language="en"):
    pygame.init()
    pygame.mixer.pre_init(buffer=4096)
    pygame.mixer.init()

    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    channel = sound.play()
    while channel.get_busy():
        pygame.time.wait(100)

