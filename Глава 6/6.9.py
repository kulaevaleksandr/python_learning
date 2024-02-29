# 6.9. Любимые места: создайте словарь с именем favorite_places. Придумайте названия трех мест, которые станут ключами словаря,
# и сохраните для каждого человека от одного до трех любимых мест.
favorite_places = {
    'Краснодар': {'Максим'},
    'Минск': {'Саша', 'Максим'},
    'Екб': {'Кирилл', 'Максим'},
}

for places, names in favorite_places.items():
    if len(names) == 1:
        print(f"\t{names} любит город {places.title()}.")
    else:
        for name in names:
            print(f"\t{name.title()} любит город {places.title()}.")
