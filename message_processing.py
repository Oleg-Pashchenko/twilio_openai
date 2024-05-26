import os
import time

import requests
import random
import mimetypes
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))


def execute(recording_link: str, message_history: list[dict]):
    filename = f'{random.randint(10000, 100000)}.mp3'
    download_file(recording_link, filename)

    # Проверка формата файла
    if not is_supported_format(filename):
        print(f"Unsupported file format: {filename}")
        os.remove(filename)
        return "Error: Unsupported file format", message_history

    transcription = transcribe(filename)
    if transcription is None:
        print(f"Transcription failed for: {filename}")
        os.remove(filename)
        return "Error: Transcription failed", message_history

    message_history.append({'role': 'user', 'content': transcription})
    print("Transcription:", transcription)
    answer = generate_answer(message_history)
    message_history.append({'role': 'assistant', 'content': answer})
    print("GPT4O answer:", answer)
    os.remove(filename)
    return answer, message_history


def transcribe(filename):
    try:
        with open(filename, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcription.text
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


def generate_answer(messages):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error generating answer: {e}")
        return "Error: Unable to generate answer"


def download_file(url, filename):
    dotenv.load_dotenv()
    account_sid = os.getenv('SID')
    auth_token = os.getenv('TOKEN')

    for i in range(10):
        response = requests.get(url, auth=(account_sid, auth_token))
        print(response.status_code)
        if response.status_code == 200:
            break
        time.sleep(1)
    with open(filename, 'wb') as f:
        f.write(response.content)


def is_supported_format(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    supported_formats = ['audio/flac', 'audio/x-m4a', 'audio/mp3', 'video/mp4', 'audio/mpeg', 'audio/mp4', 'audio/ogg',
                         'audio/wav', 'audio/webm']
    return mime_type in supported_formats
