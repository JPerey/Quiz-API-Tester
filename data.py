import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
try:
    response = requests.get(url="https://opentdb.com/api.php?amount=10", params=parameters)
except Exception as e:
    print(e)
else:
    response.raise_for_status()
    question_data = response.json()['results']
