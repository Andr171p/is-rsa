import requests


url = "https://orders-rmq-broker-production.up.railway.app/api/orders/push/"

data = {
    "client": "string",
    "number": "string",
    "date": "string",
    "status": "Принят оператором",
    "amount": 1000,
    "pay_link": "https://test",
    "pay_status": "string",
    "cooking_time_from": "string",
    "cooking_time_to": "string",
    "delivery_time_from": "string",
    "delivery_time_to": "string",
    "project": "string",
    "trade_point": "string",
    "trade_point_card": "string",
    "delivery_method": "string",
    "delivery_adress": "string",
    "phones": [
        "+7(919)935-09-14"
    ]
}

r = requests.post(
    url=url,
    json=data
)
print(r.json())