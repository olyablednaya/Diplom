# Ольга Церелунова, 26-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# тест что код ответа равен 200. 
def test_sucsess_create_order():
    #arange - в файле sender_stand_request
    #act 
    order_response = sender_stand_request.get_order_by_number(sender_stand_request.track_number)
    #assert 
    assert order_response.status_code == 200