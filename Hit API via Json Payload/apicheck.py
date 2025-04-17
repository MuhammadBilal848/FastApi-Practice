import requests


payload = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}


send = requests.get('http://0.0.0.0:8000/get-info', json=payload)


print(send.json())