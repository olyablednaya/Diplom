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


track_number = response.json()["track"]
print(track_number)


