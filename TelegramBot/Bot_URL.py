import requests as requests
import random

url = "https://api.telegram.org/bot1083609466:AAHjQd9vMPK4NmBclfmuU00F2PzW7-OKJrY/"

def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id

def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

def get_first_name(update):
    first_name = update["message"]["chat"]["username"]
    return first_name

def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]

def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hola" or get_message_text(update).lower() == "/start":
                send_message(get_chat_id(update), 'Hola Bienvenid@ ' + '"' + get_first_name(update) + '"' + ', a nuestro bot. Escribe "play" para jugar a contar datos.')
            elif get_message_text(update).lower() == "play":
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                _3 = random.randint(1, 6)
                send_message(get_chat_id(update), 'Tu tienes ' + str(_1) + ' + ' + str(_2) + ' + ' + str(_3) + '!\n Tu resultado es ' + str(_1 + _2 + _3) + '!!!')
            else:
                send_message(get_chat_id(update), '¿Porque eres así?, Solo escribe la palabra "play" :V')
            update_id += 1
main()
