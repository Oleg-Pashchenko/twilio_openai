import requests

# Данные запроса
data = {
    'Called': '+13187029367',
    'RecordingUrl': 'https://api.twilio.com/2010-04-01/Accounts/AC6742f16eb65321c514705f79689a7f94/Recordings/RE290cc2b164f023c7653e327650de42dc',
    'ToState': 'LA',
    'CallerCountry': 'RU',
    'Direction': 'inbound',
    'CallerState': '',
    'ToZip': '',
    'CallSid': 'CAecb7829bd7c653d14b078f5ff91058f62',
    'To': '+13187029367',
    'CallerZip': '',
    'ToCountry': 'US',
    'CalledZip': '',
    'ApiVersion': '2010-04-01',
    'CalledCity': '',
    'CallStatus': 'in-progress',
    'RecordingSid': 'RE290cc2b164f023c7653e327650de42dc',
    'From': '+79870739395',
    'AccountSid': 'AC6742f16eb65321c514705f79689a7f94',
    'CalledCountry': 'US',
    'CallerCity': '',
    'ToCity': '',
    'FromCountry': 'RU',
    'Caller': '+79870739395',
    'FromCity': '',
    'CalledState': 'LA',
    'FromZip': '',
    'FromState': '',
    'RecordingDuration': '9'
}

# URL для отправки запроса
url = 'http://85.193.95.151:6644/voice'  # замените на нужный URL

# Отправка POST-запроса
response = requests.post(url, data=data)

print(response.text)