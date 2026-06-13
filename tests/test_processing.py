from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_state, result_state_1, result_state_2):
    assert filter_by_state(list_state, "EXECUTED") == result_state_2  # тестирование функции
    # на значение переменной state = EXECUTED
    assert filter_by_state(list_state, "CANCELED") == result_state_1  # тестирование функции
    # на значение переменной state = CANCELED
    assert filter_by_state(list_state, "") == []  # тестирование функции на пустое значение переменной state


def test_sort_by_date(list_state, result_state_3, result_state_4):
    assert sort_by_date(list_state) == result_state_3  # тестирование сортировки списка словарей по датам
    # в порядке убывания
    assert sort_by_date(list_state, False) == result_state_4  # тестирование сортировки списка словарей
    # по датам в порядке в порядке возростания
    assert sort_by_date([]) == []  # тестирование сортировки списка словарей на ввод пустой даты
