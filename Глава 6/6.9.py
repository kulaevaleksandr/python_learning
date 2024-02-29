# 6.9. Любимые места: создайте словарь с именем favorite_places. Придумайте названия трех мест, которые станут ключами словаря,
# и сохраните для каждого человека от одного до трех любимых мест.
favorite_places = {
    'Краснодар': 'Максим',
    'Минск': {'Саша', 'Максим'},
    'Екб': {'Кирилл', 'Максим'},
}
for place, people in favorite_places.items():
    for name in people.values():
        print(f'\nName: {name}')
    people = people['name']
    print(f'\tPlace: {place.title()}')
