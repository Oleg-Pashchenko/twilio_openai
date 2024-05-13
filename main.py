from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    print(request.values)
    resp = VoiceResponse()
    resp.say("Привет от Олега для Влада")
    resp.record()

    return str(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6644)
