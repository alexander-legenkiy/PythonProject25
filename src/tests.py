from src import masks

# test_1 = masks.get_mask_card_number(str(7000792289606362))
# print(test_1)
#
# if test_1 != "7365 41** **** 3587":
#     raise Exception("Ошибка!")


def test_get_mask_card_number():
    assert masks.get_mask_card_number(str(7000792289606362)) == "7000 79** **** 6362"
