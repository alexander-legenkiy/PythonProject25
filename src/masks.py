def get_mask_card_number(card_number: str) -> str:
    """функция принимает на вход номер карты и возвращает его маску"""
    if len(card_number) == 16 and card_number.isdigit() == True:  # проверяем, что ведённые символы - цифры и их 16
        mask_card_number = str(
            (card_number[0:4]) + " " + (card_number[4:6]) + "**" + " " + "****" + " " + (card_number[12:16])
        )
        # переводм номер карты в заданный формат
        return mask_card_number
    else:
        raise ValueError("Неверные данные!")


# проверка работы функции
# 7000792289606361
# card_number = input("Введите номер Вашей банковской карты:")
# print(get_mask_card_number(card_number))


def get_mask_account(account_number: str) -> str:
    """функций принимает на вход номер счёта и возвращает его маску"""
    if len(account_number) == 20 and account_number.isdigit() == True:  # проверяем, что ведённые символы - цифры
        # и их ровно 20
        mask_account_number = str("**" + (account_number[-4:]))
        # переводм номер карты в заданный формат
        return mask_account_number
        # функция возвращает номер счёта в виде заданного формата
    else:
        raise ValueError("Неверные данные!")


# проверка работы функции
# 73654108430135874305
# account_number = input("Введите номер Вашего банковского счёта:")
# print(get_mask_account(account_number))
