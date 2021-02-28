import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding="utf-8") as fl:
        data = json.loads(fl.read())

    data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

    with open('orders.json', "w", encoding="utf-8") as fl:
        json.dump(data, fl, indent=4)



write_order_to_json('Книга','3','256','Antonov','11.05.20')