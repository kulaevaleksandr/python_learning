# 5.11. Порядковые числительные: порядковые числительные в английском языке заканчиваются суффиксом th (кроме 1st, 2nd и 3rd).
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')
