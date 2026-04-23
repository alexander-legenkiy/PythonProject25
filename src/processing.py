def filter_by_state(dictionary_list: list, state="EXECUTED") -> list:
    # """функция принимает список словарей и возвращает новый список словарей,
    # исходя из значения ключа state (по умолчанию установлено значение "EXECUTED" """

    new_dictionary_list = []
    # создаём пустой список для формирования нового списка словарей

    for key in dictionary_list:
        if key["state"] == state:
            new_dictionary_list.append(key)
            # формируем новый список словарей, в который попадают словари содержащие ключ state с заданным значением

    return new_dictionary_list
    # функция возвращает новый список словарей


# проверка работы функции


dictionary_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(dictionary_list, "EXECUTED"))


def sort_by_date(dictionary_list: list, reverse=False) -> list:
    # """функция принимает список словарей и возвращает новый список отсортированный по дате,
    # по умолчанию отсортированный по убыванию"""

    sorted_new_dictionary_list = sorted(dictionary_list, key=lambda x: x["date"], reverse=reverse)
    return sorted_new_dictionary_list
    #  функция возвращает новый список словарей


# проверка работы функции


dictionary_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(dictionary_list))
