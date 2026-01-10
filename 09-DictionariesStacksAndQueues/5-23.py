import json

with open('euro.json', 'r') as file:
    data = json.load(file)

    print(f"Waluta: {data['currency']} ({data['code']})")
    print('-' * 30)

    for rate in data['rates']:
        date = rate['effectiveDate']
        value = rate['mid']

        print(f"Data: {date} | Kurs: {value}")