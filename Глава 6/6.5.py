# 6.5 Реки: создайте словарь с названиями трех больших рек и стран, по которым протекает каждая река
rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'lena': 'russia'
}
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
# Вывести названия всех рек
for river in rivers.keys():
    print(river.title())
# Вывести названия всех стран
for country in rivers.values():
    print(country.title())
