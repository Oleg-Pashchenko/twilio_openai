import os

import requests
import random
from openai import OpenAI
import dotenv


dotenv.load_dotenv()
url = 'https://api.twilio.com/2010-04-01/Accounts/AC6742f16eb65321c514705f79689a7f94/Recordings/RE9c14f37fcc3dd6f5e702253e73a6ae2d'
filename = f'{random.randint(10000, 100000)}.mp3'
client = OpenAI(api_key=os.getenv('API_KEY'))

message_history = [
    {"role": "system",
     "content": "Ты ассистент команды аватарекс. Твоя задача продавать бананы, представляйся Анастасией."}
]


def transcribe(filename):
    audio_file = open(filename, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription.text


def create_completion(messages):
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



# download_file(url, filename)
# transcription = transcribe(filename)
# answer = generate_answer(transcription)
