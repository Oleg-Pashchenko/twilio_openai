import os

import requests
import random
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))


def execute(recording_link: str, message_history: list[dict]):
    filename = f'{random.randint(10000, 100000)}.mp3'
    download_file(recording_link, filename)
    transcription = transcribe(filename)
    message_history.append({'role': 'user', 'content': transcription})
    print("Transcription:", transcription)
    answer = generate_answer(message_history)
    message_history.append({'role': 'assistant', 'content': answer})
    print("GPT4O answer:", answer)
    os.remove(filename)
    return answer, message_history


def transcribe(filename):
    audio_file = open(filename, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription.text


def generate_answer(messages):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return completion.choices[0].message.content


def download_file(url, filename):
    account_sid = os.getenv('SID')
    auth_token = os.getenv('TOKEN')
    response = requests.get(url, auth=(account_sid, auth_token))
    with open(filename, 'wb') as f:
        f.write(response.content)

