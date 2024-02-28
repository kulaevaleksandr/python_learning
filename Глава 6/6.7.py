# 6.7. Люди: начните с программы, написанной для упражнения 6.1 (с. 113). Создайте два новых словаря, представляющих разных людей, и сохраните все три словаря в списке с именем people.
people = {
    'brother': {
        'first_name': 'Леонид',
        'last_name': 'Кулаев',
        'city': 'Чайковский',
        'birth_date': '30_12_2004',
        'age': '19',
        },
    'sister': {
        'first_name': 'Катя',
        'last_name': 'Бикинёва',
        'city': 'Чайковский',
        'birth_date': '15_04_2004',
        'age': '18',
    },
    'friend': {
        'first_name': 'Максим',
        'last_name': 'Кривошеев',
        'city': 'Чайковский',
        'birth_date': '11_12_1997',
        'age': '26',
    }
}
for kinship, kin_info in people.items():
    print(f'\nКто: {kinship}')
    full_name = f'{kin_info['first_name']} {kin_info['last_name']}'
    location = kin_info['city']
    birth_date = kin_info['birth_date']
    age = kin_info['age']
    print(f'\tFull name: {full_name.title()}')
    print(f'\tCity: {location.title()}')
    print(f'\tBirth_date: {birth_date}')
    print(f'\tAge: {age}')
