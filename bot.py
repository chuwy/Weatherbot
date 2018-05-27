import requests
import token_number
import json

token = token_number.token

# https://api.telegram.org/bot568185611:AAG1M2E4xoi12zlgI1wYsOxnHiuXt74W3Os/sendMessage?chat_id=37205471&text=Hi
URL = "https://api.telegram.org/bot" + token + "/"
# получаю обновления от сервера телеграм в виде словаря в формате json :
def get_updates():
    url = URL + "getUpdates"
    responce = requests.get(url)
    return responce.json()
# в файле в списках ищу id пользователя и его text, записываю их в переменные
# и возвращаю себе словарь, состоящий только из этих переменных
def get_message():
    data = get_updates()
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    message_text = data["result"][-1]["message"]["text"]

    message = {"chat_id": chat_id,
                "text": message_text}
    return message

def send_message(chat_id, text = "Hi, wait a minute."):
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)

def main():
    # dictionary = get_updates()
    # with open('updates.json', 'w') as jsonfile:
    #      json.dump(dictionary, jsonfile, indent=2, ensure_ascii=False)
    answer = get_message()
    chat_id = answer["chat_id"]
    text = answer["text"]

    if '/start' in text:
        send_message(chat_id, "Hi, I can halp you to know the weather in you city, just tell me it.")
    else:
        send_message(chat_id, "If you want to know the weather just send me a city.")

if __name__ == '__main__':
     main()
