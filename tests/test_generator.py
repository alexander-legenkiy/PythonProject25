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