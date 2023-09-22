import requests
from colorama import Fore
def phone_locator(phone_number, api_key):
    url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def print_phone_details(phone_details):
    print("Phone Details:")
    print(f"Numero: {phone_details['number']}")
    print(f"Regione: {phone_details['country_name']} ({phone_details['country_code']})")
    print(f"Carriera: {phone_details['carrier']}")
    print(f"Linea: {phone_details['line_type']}")
    print(f"Posizione: {phone_details['location']}")
    print(f"Valid*: {phone_details['valid']}")

api_key = "22WfDqB635jMOWkxdeC1r2BXew1tXHLU"

phone_number = input(Fore.CYAN+Scrivi il numero di telefono per localizzarlo: ")

phone_details = phone_locator(phone_number, api_key)
print_phone_details(phone_details)
