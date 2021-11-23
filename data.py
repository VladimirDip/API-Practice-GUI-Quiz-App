import requests

COUNT_QUESTIONS = 10
TYPE_QUESTIONS = "boolean"


parametrs = {
    'amount': COUNT_QUESTIONS,
    'type': TYPE_QUESTIONS
}


req = requests.get(url="https://opentdb.com/api.php", params=parametrs)
req.raise_for_status()
data = req.json()["results"]

question_data = data

