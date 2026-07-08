import pytest

from src.generator import card_number_generator, filter_by_currency, transaction_descriptions


# Проверка, что функция корректно фильтрует транзакции по заданной валюте
def test_filter_by_currency(list_state_2, result_state_5):
    assert list(filter_by_currency(list_state_2, "USD")) == result_state_5

# Проверка, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутсвуют
def test_filter_by_currency(list_state_2):
    assert list(filter_by_currency(list_state_2, "CZK")) == []

# Проверка,что генератор не завершается ошибкой при обработке пустого списка
def test_filter_by_currency(list_state_3):
    assert list(filter_by_currency(list_state_3, "USD")) == []

# Проверка,что генератор не завершается ошибкой при обработке списка без соответствующих валютных операций
def test_filter_by_currency(list_state_2):
    assert list(filter_by_currency(list_state_2, "")) == []

#Проверка, что функция возвращает корректные описания для каждой транзакции
def test_transaction_descriptions(list_state_2):
    assert list(transaction_descriptions(list_state_2)) == ['Перевод организации', 'Перевод со счета на счет', 'Перевод со счета на счет', 'Перевод с карты на карту', 'Перевод организации']

#Тестирование работы функции с различным количеством входных транзацкций
def test_transaction_descriptions(list_state_4):
    assert list(transaction_descriptions(list_state_4)) == ['Перевод организации',
 'Перевод со счета на счет',
 'Перевод со счета на счет',
 'Перевод с карты на карту',
 'Перевод организации',
 'Возврат перевода',
 'Перевод по договору']

#Тестирование работы функции с пустым списком
def test_transaction_descriptions(list_state_3):
    assert list(transaction_descriptions(list_state_3)) == []

#Проверяет, что генератор выдат правильные номера карт в заданном диапозоне
def test_card_number_generator():
    assert print(card_number_generator(1,1)) == "0000 0000 0000 0001"

def test_card_number_generator():
    assert list(card_number_generator(1,2)) == ['0000 0000 0000 0001', '0000 0000 0000 0002']

def test_card_number_generator():
    assert list(card_number_generator(100000000,100000001)) == ['0000 0001 0000 0000', '0000 0001 0000 0001']

@pytest.mark.parametrize("start, stop, expected",
    [(1, 1, ['0000 0000 0000 0001']),
    (5, 5, ['0000 0000 0000 0005']),
    (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003'])
     ])

def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected

# Проверка работы генератора при выходе за рамки заданного диапазона.
def test_card_number_generator():
    assert list(card_number_generator(1,10000000000000001)) == []

# Проверка работы генератора при выходе за рамки заданного диапазона.
def test_card_number_generator():
    with pytest.raises(ValueError):
        assert list(card_number_generator(1, 10000000000000001))

# Проверка соответсвия вывода генератором номера карты в заданном стандартном формате
def test_card_number_generator():
    with pytest.raises(AssertionError):
        assert list(card_number_generator(1, 1)) == ['0000000000000001']

# Проверяет, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию
def test_card_number_generator():
    assert list(card_number_generator(9999999999999998,9999999999999999)) == ['9999 9999 9999 9998', '9999 9999 9999 9999']

#Тестирование работы функции с различным количеством входных транзацкций
@pytest.mark.parametrize("list_1, expected",
    [([{"id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"},
            {
                "id": 594221111,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Возврат перевода",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"},
            {
                "id": 594222222,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод по договору",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"}
            ],
            ['Перевод организации',
 'Перевод со счета на счет',
 'Перевод со счета на счет',
 'Перевод с карты на карту',
 'Перевод организации',
 'Возврат перевода',
 'Перевод по договору']),
     ([
            {
                "id": 100000001,
                "state": "EXECUTED",
                "date": "2023-01-15T09:30:15.123456",
                "operationAmount": {
                    "amount": "1500.50",
                    "currency": {"name": "EUR", "code": "EUR"}
                },
                "description": "Оплата услуг",
                "from": "Счет 12345678901234567890",
                "to": "Счет 98765432109876543210"
            },
            {
                "id": 100000002,
                "state": "EXECUTED",
                "date": "2023-02-20T14:45:30.987654",
                "operationAmount": {
                    "amount": "25000.00",
                    "currency": {"name": "руб.", "code": "RUB"}
                },
                "description": "Перевод на карту",
                "from": "Счет 11111111111111111111",
                "to": "Visa Gold 1234567890123456"
            },
            {
                "id": 100000003,
                "state": "CANCELED",
                "date": "2023-03-10T11:20:45.456789",
                "operationAmount": {
                    "amount": "3200.75",
                    "currency": {"name": "USD", "code": "USD"}
                },
                "description": "Покупка в магазине",
                "from": "MasterCard 2345678901234567",
                "to": "Счет 22222222222222222222"
            },
            {
                "id": 100000004,
                "state": "EXECUTED",
                "date": "2023-04-05T16:10:20.654321",
                "operationAmount": {
                    "amount": "850.30",
                    "currency": {"name": "GBP", "code": "GBP"}
                },
                "description": "Перевод по договору",
                "from": "Счет 33333333333333333333",
                "to": "Счет 44444444444444444444"
            },
            {
                "id": 100000005,
                "state": "EXECUTED",
                "date": "2023-05-12T08:55:10.321098",
                "operationAmount": {
                    "amount": "100000.00",
                    "currency": {"name": "руб.", "code": "RUB"}
                },
                "description": "Возврат перевода",
                "from": "Visa Platinum 3456789012345678",
                "to": "Счет 55555555555555555555"
            }
        ],
        ['Оплата услуг', 'Перевод на карту', 'Покупка в магазине',
         'Перевод по договору', 'Возврат перевода'])
     ])

def test_transaction_descriptions(list_1, expected):
    assert list(transaction_descriptions(list_1)) == expected
