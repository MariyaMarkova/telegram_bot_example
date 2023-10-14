import requests, telebot
from datetime import datetime 
from token_data import token

def gain_info():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price - {sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_greeting(message):
        bot.send_message(message.chat.id, "Hello, dear applicant. Write price of BTC.")
    
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n\nSell BTC price - {sell_price}"

                )
            except Exception as ex:
                print(ex)   
                bot.send_message(
                    message.chat.id,
                    "Something wrong happended....."
                ) 
        else:
            bot.send_message(message.chat.id, "Command is not corrrect. Try one more time.")        

        
    bot.polling()    

if __name__ == "__main__":
    # gain_info()
    telegram_bot(token)