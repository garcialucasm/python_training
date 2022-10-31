import pygame
pygame.init()
#O arquivo mp3 deve estar carregado no pycharm
pygame.mixer.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
