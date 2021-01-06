import requests
import json
from config import keys


class Get_priceException(Exception):
    pass

class APIException:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise Get_priceException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise Get_priceException(f'не удалось распознать валюту {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise Get_priceException(f'не удалось распознать валюту {quote}')
        try:
            amount = float(amount)
        except ValueError:
            raise Get_priceException(f'Не удалось обработать колличество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={quote_ticker}')
        total_base = json.loads(r.content)['rates'][keys[quote]]
        total_base = round(total_base * amount, 2)

        return total_base




