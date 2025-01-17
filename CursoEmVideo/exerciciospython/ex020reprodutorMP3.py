import pygame
pygame.mixer.init()
caminho_audio = "C:/Users/Raphael/Downloads/musicateste.mp3"
try:
    pygame.mixer.music.load(caminho_audio)
    pygame.mixer.music.play()
    input("Pressione Enter para sair e parar o áudio.")
    pygame.mixer.music.stop()
except Exception as e:
    print(f"Erro ao reproduzir o áudio: {e}")

