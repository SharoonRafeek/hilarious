from gtts import gTTS


def text_to_speech(joke):
    audio = gTTS(text=joke, slow=True, lang="en")
    audio.save("assets/audio.mp3")
