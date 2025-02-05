import configuration
import requests
import data

#функция создания нового заказа
def post_order():
    #выполнение пост запроса
    return requests.post(url=configuration.URL_SERVICE + configuration.ORDER_PATH,
                         json=data.body)

response = post_order()

# Вывод статус-кода
print("Status Code:", response.status_code)
# Вывод тела ответа в виде текста
print("Response Body:", response.text)

#сохраняем трек номер
track_number = response.json()["track"]
print(track_number)

def get_order_by_number(track_number):
    #выполенение гет запроса
    return requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER_PATH + str(track_number))

response_get_order = get_order_by_number(track_number)
print(response_get_order.status_code)
print(response_get_order.text)