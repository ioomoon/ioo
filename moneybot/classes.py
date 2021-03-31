import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote, base, amount):
        if quote == base:
            raise ConvertionExeption('Неудалось перевести валюту. Повторите Ваш запрос.')

        try:
            quote in keys
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base in keys
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        quote_ticker = keys[quote]
        base_ticker = keys[base]
        #r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        res = json.loads(r.content)
        rate = res["rates"][base_ticker]

        return rate