# mAlc_Jke \ vya4es.ru/projects/txt-to-speech-mic

import gtts
import pygame
import os

from time import sleep
from pydub import AudioSegment
from pygame import mixer, _sdl2 as devices


def play(file_path: str, device: str):
    if device is None:
        devices = get_devices()
        if not devices:
            raise RuntimeError("No device!")
        device = devices[0]
    print("Play: {}\r\nDevice: {}".format(file_path, device))
    pygame.mixer.init(devicename=device)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    duration = get_audio_duration(file_path)
    sleep(duration)
    pygame.mixer.quit()


def text_to_speech(text):
    tts = gtts.gTTS(text, lang="en-us", tld="com.tr")
    tts.save("temp.mp3")


def get_audio_duration(file_path):
    audio = AudioSegment.from_file(file_path)
    duration_in_seconds = len(audio) / 1000  # Преобразование миллисекунд в секунды
    return duration_in_seconds


def get_audio_input_device():
    mixer.init()  # Инициализация mixer
    audio_devices = devices.audio.get_audio_device_names(
        False
    )  # Получение всех доступных аудио-входных устройств

    print("availableAudioEntryDevices:")
    for i, device in enumerate(audio_devices):
        print(f"{i+1}. {device}")

    while True:
        try:
            choice = int(input("Select the number of the audio-entry device: "))
            if 1 <= choice <= len(audio_devices):
                break
            else:
                print(f"Please select a number from 1 to {len(audio_devices)}")
        except ValueError:
            print("Please enter the correct number")

    selected_device = audio_devices[choice - 1]  # Выбор указанного устройства

    # while True:
    #     try:
    #         choice = int(
    #             input("Select the second device number of the audio-entry device: ")
    #         )
    #         if 1 <= choice <= len(audio_devices):
    #             break
    #         else:
    #             print(f"Please select a number from 1 to {len(audio_devices)}")
    #     except ValueError:
    #         print("Please enter the correct number")

    # selected_device2 = audio_devices[choice - 1]  # Выбор указанного устройства

    mixer.quit()  # Completion of work mixer

    return selected_device


def main():

    selected_device = get_audio_input_device()

    while True:
        text = input("")
        if text.lower() == "выход":
            break

        if text == "":
            continue

        os.system("cls")

        text_to_speech(text)

        # Воспроизведение сохраненной речи через виртуальный микрофон
        play("temp.mp3", selected_device)


if __name__ == "__main__":
    main()
