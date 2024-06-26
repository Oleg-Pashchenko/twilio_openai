from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

import message_processing

app = Flask(__name__)

hi_message = "Добро пожаловать. Что бы вы хотели узнать?"
prompt_message = "Ты ассистент команды аватарекс. Твоя задача продавать бананы, представляйся Анастасией."
prompt = [{"role": "system",
           "content": prompt_message},
          {'role': 'assistant', 'content': hi_message}]
calls = {}


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    global calls

    recording_url = request.values.get('RecordingUrl', None)
    call_id = request.values.get('CallSid', None)
    resp = VoiceResponse()
    if recording_url and call_id in calls.keys():
        message_history = calls[call_id]
        answer, message_history = message_processing.execute(recording_url, message_history)
        calls[call_id] = message_history
        resp.say(answer)
    if call_id not in calls.keys():
        calls[call_id] = prompt
        resp.say(hi_message)
    resp.record(timeout=1)
    return str(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6644)
