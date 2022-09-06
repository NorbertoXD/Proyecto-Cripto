import requests


apikey = "223C305D-FB30-4F3B-A4CC-FB1935013054"
headers = {
    "X-CoinAPI-Key": apikey
} 
api_url = "http://rest.coinapi.io"
endpoint = "/v1/assets"

url = api_url + endpoint

respuesta = requests.get(url, headers=headers)
codigo = respuesta.status_code

if codigo == 200:
    print("Las monedas disponibles son:")
    respuesta_json = respuesta.json()

    for moneda in respuesta_json:
        if moneda["asset_id"].startswith("EUR"):
            print(moneda["asset_id"], moneda["name"])



else:
    print("La peticion a la API ha fallado")
    print(f"Codigo del error {codigo}")
    print(f"Razon del error {respuesta.reason}")
    print(respuesta.text)