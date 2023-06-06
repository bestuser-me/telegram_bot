import requests

from pprint import pprint

API_KEY = 'b48c5030c55f751d2cf30d1b'

currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
# pprint(response.status_code)
currency = response.json()
pprint(currency['conversion_rate'])
# res = r.json()
# pprint(res)
# pprint(res['conversion_rate'])
