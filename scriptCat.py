import pygame
import cv2
import os
import time
from colorama import Fore, Back, Style, init

pygame.mixer.init()
ASCII_CHARS = " .:-=+*#%@#@&$"

def resize_frame(frame, width):
    height = int(frame.shape[0] * (width / frame.shape[1]))
    return cv2.resize(frame, (width, height))

def frame_to_ascii(frame, width):
    frame = resize_frame(frame, width)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ascii_frame = ""
    for y in range(gray_frame.shape[0]):
        for x in range(gray_frame.shape[1]):
            pixel_value = gray_frame[y, x]
            ascii_char = ASCII_CHARS[pixel_value // 25]
            b, g, r = frame[y, x] 
            ascii_frame += f"\033[38;2;{r};{g};{b}m{ascii_char}" 
        ascii_frame += "\n"
    return ascii_frame

def video_to_ascii(video_path, width=80, fps=10):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erreur : Impossible de lire la vidéo.")
        return
    pygame.mixer.music.load(video_path) 
    pygame.mixer.music.play()  
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ascii_art = frame_to_ascii(frame, width)
        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_art)
        time.sleep(1 / fps)

    cap.release()
video_to_ascii("./video/uiiaiCat.mp4", width=80, fps=10)
