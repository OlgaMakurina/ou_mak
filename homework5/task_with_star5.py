# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    # Здесь нужно написать код
    my_lst = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]
    roman_str = 'M' * (val // 1000)
    val = val - 1000 * (val // 1000)
    for k in range(2, 8, 2):
        if val // my_lst[k][0] < 4:
            roman_str = roman_str + my_lst[k][1] * (val // my_lst[k][0])
        elif val // my_lst[k][0] == 4:
            roman_str = roman_str + my_lst[k][1] + my_lst[k - 1][1]
        elif (val // my_lst[k][0] > 4) and (val // my_lst[k][0]) < 9:
            roman_str = roman_str + my_lst[k - 1][1] + my_lst[k][1] * (val // my_lst[k][0] - 5)
        else:
            roman_str = roman_str + my_lst[k][1] + my_lst[k - 2][1]
        val = val - my_lst[k][0] * (val // my_lst[k][0])
    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
