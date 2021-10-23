import os
from dotenv import load_dotenv
from joke_api.joke import joke
from audio.text_to_audio import text_to_speech
from image.image import keywords


load_dotenv()

url = os.getenv("JOKE_URL")
text = joke(url)

text_to_speech(text)

print(keywords("The indefinite article takes two forms. It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet. The indefinite article only appears with singular nouns. Consider the following examples of indefinite articles used in"))
