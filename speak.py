from gtts import gTTS

language = 'en'
text = "Welcome to D-Mart Shopping mall"

speech = gTTS(text=text, lang=language, slow=False)

speech.save('text.mp3')