import pytest

from src.widget import get_date  # импорт функции get_date из файла widget
from src.widget import mask_account_card  # импорт функции mask_account_card из файла widget


def test_mask_account_card():  # тестирование корректности маскировки номера карты и номера счёта
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счёт **4305"


@pytest.mark.parametrize(
    "mask_card_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счёт **4305"),
        ("Maestro 1234567891234567", "Maestro 1234 56** **** 4567"),
        ("Maestro 123", "Ошибка ввода информации!"),
    ],
)
def test_mask_account_card(mask_card_number, expected):  # параметризированные тесты с заданными параметрами
    # номеров карты и номеров счёта, в т.ч. с некорректными номерами
    assert mask_account_card(mask_card_number) == expected


def test_get_date():  # тестирование корректности маскировки даты
    assert get_date("2019-07-03") == "03.07.2019"  # тестирование работы функции
    assert get_date("2019.NN.03") != "03.07.2019"  # тестирование на некорректный ввод даты
    assert get_date("") == "Ошибка ввода информации!"  # тестирование на ввод пустой даты
