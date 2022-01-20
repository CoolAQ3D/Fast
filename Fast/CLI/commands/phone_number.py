import phonenumbers
from phonenumbers import geocoder, carrier

#Basic, NOT DONE

def phone(number):
  try:
    country = phonenumbers.parse(number, "CH")
    country = geocoder.description_for_number(country, 'en')
    print(f"Country: {country}")

    _carrier = phonenumbers.parse(number, "RO")
    _carrier = carrier.name_for_number(_carrier, 'en')
    print(f"Carrier: {_carrier}")

  except Exception as e:
    print(e)