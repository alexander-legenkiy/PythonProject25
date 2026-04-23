import masks


def mask_account_card(card_or_accaunt_information: str) -> str:
    # """функция принимает информацию о счетах и картах и обрабатывает их"""

    numbers_count = 0
# устанавливаем счётчик цифр в введённой информации
    card_or_account_number = ""
# устанавливаем пустую строку для сбора номера счёта или номера карты
    card_or_account_name = ""
# устанавливаем пустую строку для сбора названия карты
    card_or_account_name_correct = ""
# устанавливаем пустую строку для сбора названия карты, c учётом отступов между словами
    for i in card_or_accaunt_information:
        if i.isdigit():
            # выбираем из введённой информации цифры
            numbers_count = numbers_count + 1
            # считаем количество цифр в введённой информации
            card_or_account_number = card_or_account_number + i
            # формирмуем строку с номером счёта или номером карты

    for i in card_or_accaunt_information:
        if i.isalpha():
            # выбираем из введённой информации буквы
            card_or_account_name = card_or_account_name + i
            # формируем строку с названием карты или словом "счёт"


    for i in card_or_account_name:
        # разбиваем строку названия карты на отдельные слова, начинающиеся с большой буквы.
        if i.islower():
            # из названия карты выбираем строчные буквы
            card_or_account_name_correct = card_or_account_name_correct + i
        if i.isupper():
            # из названия карты выбираем заглавные буквы
            card_or_account_name_correct = card_or_account_name_correct + " " + i
            # делаем отступ перед заглавной буквой
    card_or_account_name_correct_final = card_or_account_name_correct[1:]
    # убираем отступ перед первой заглавной буквой

    if numbers_count == 20:
        # если в введённой информации 20 цифр, то введён номер счёта
        mask_account_number = masks.get_mask_account(card_or_account_number)
        # преобразуем номер счёта в заданную маску используя функцию get_mask_account из файла masks.py
        full_mask_account_number = str("Счёт " + mask_account_number)
        return full_mask_account_number

    if numbers_count == 16:
        # если в введённой информации 16 цифр, то введён номер карты
        mask_card_number = masks.get_mask_card_number(card_or_account_number)
        # преобразуем номер счёта в заданную маску используя функцию get_mask_card_number из файла masks.py
        full_card_number = str(card_or_account_name_correct_final + " " + mask_card_number)
        # добаляем к названию карты маску номера карты
        return full_card_number

    if numbers_count != 20 and numbers_count != 16:
        # если в введённой информации не 16 или 20 цифр, то функция выдаёт информацию об ошибке
        return "Ошибка ввода информации!"


# проверка работы функции:
card_or_accaunt_information = input("Введите номер Вашего банковского счёта или номер карты:")
print(mask_account_card(card_or_accaunt_information))


def get_date(date_information: str) -> str:
    # """функция принимает на вход дату в определённом формате и возвращает дату в заданном формате"""
    year = str(date_information[0:4])
    month = str(date_information[5:7])
    day = str(date_information[8:10])
    new_date = str(day + "." + month + "." + year)
    return new_date


# проверка работы функции:
date_information = input("Введите дату:")
print(get_date(date_information))
