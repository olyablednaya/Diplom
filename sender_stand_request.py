import configuration
import requests
import data

#функция создания нового заказа
def post_order():
    #выполнение пост запроса
    return requests.post(url=configuration.URL_SERVICE + configuration.ORDER_PATH,
                         json=data.body)

response = post_order()

#сохраняем трек номер
track_number = response.json()["track"]

def get_order_by_number(track_number):
    #выполенение гет запроса
    return requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER_PATH + str(track_number))

response_get_order = get_order_by_number(track_number)