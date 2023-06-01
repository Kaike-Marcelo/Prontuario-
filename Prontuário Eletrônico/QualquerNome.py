import requests
import json

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzMDUxNDA0LCJpYXQiOjE2ODMwNTExMDQsImp0aSI6ImJiMGM4YjQxZTc1NzRlNDA4MWM5NWIzMjg5NDk4YzU5IiwidXNlcl9pZCI6MSwibmFtZSI6IiIsImNucyI6IjEyMzQ1Njc4OSIsImlkIjoxfQ.9A353B585C_yF0XMAwkRGblTP4Wv8D7cbuxYS1DZHRA'

dados = requests.get('http://127.0.0.1:8000/api/user', headers={'Content-Type': 'application/json',
                                                                'Authorization': 'Bearer {}'.format(token)})

dados = json.loads(dados.text)

for dado in dados:
    print()
    print(dado)