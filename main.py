import speech_recognition as sr
from datetime import datetime


class VoiceTyper:
    def __init__(self):
        self.audio_text = ""
        self.current_time = datetime.now().strftime("%d-%m-%Y %H-%M")

    def record_and_write(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            audio = recognizer.listen(mic)
            self.audio_text = recognizer.recognize_google(audio)
            with open(f"{self.current_time}", "w") as text_file:
                text_file.write(self.audio_text)


if __name__ == '__main__':
    voice_typer = VoiceTyper()
    voice_typer.record_and_write()
