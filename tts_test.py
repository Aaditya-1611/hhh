from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()  # reads ELEVENLABS_API_KEY from your .env file

client = ElevenLabs()  # picks up the key automatically

audio = client.text_to_speech.convert(
    text="Hello! This is my first ElevenLabs voice.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

print("Saved output.mp3")
