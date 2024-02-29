# 6.12. Расширение: примеры, с которыми мы работаем, стали достаточно сложными,
# и в них можно вносить разного рода усовершенствования. Воспользуйтесь одним из примеров этой главы и расширьте его:
writers = {
    'achehov': {
        'first': 'Антон',
        'last': 'Чехов',
        'life_year': '1860-1904',
        'work': 'Человек в футляре',
    },
    'vnabokov': {
        'first': 'Владимир',
        'last': 'Набоков',
        'life_year': '1899-1977',
        'work': 'Лолита',
    },
    'fdostoevskiy': {
        'first': 'Фёдор',
        'last': 'Достоевский',
        'life_year': '1821-1881',
        'work': 'Преступление и наказание',
    },
    'asolzhenicin': {
        'first': 'Александр',
        'last': 'Солженицын',
        'life_year': '1918-2008',
        'work': 'Архипелаг ГУЛАГ',
    },
    'iturgenev': {
        'first': 'Иван',
        'last': 'Тургенев',
        'life_year': '1818-1883',
        'work': 'Отцы и дети',
    },
    'mbulgakov': {
        'first': 'Михаил',
        'last': 'Булгаков',
        'life_year': '1891-1940',
        'work': 'Мастер и Маргарита',
    },
}
for username, user_info in writers.items():
    print(f'\nUsername: {username}')
    full_name = f'{user_info['first']} {user_info['last']}'
    life_year = user_info['life_year']
    work = user_info['work']
    print(f'\tПолное имя: {full_name.title()}')
    print(f'\tГоды жизни: {life_year}')
    print(f'\tИзвестное произведение: "{work}"')
