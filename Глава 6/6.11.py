# 6.11. Города: создайте словарь с именем cities. Используйте названия трех городов в качестве ключей словаря. Создайте словарь с информацией о каждом городе; включите в него
# страну, в которой расположен город, примерную численность населения и один примечательный факт, относящийся к этому городу. Ключи словаря каждого города должны называться country, population и fact. Выведите название каждого города и всю сохраненную
# информацию о нем.
cities = {
    'Longyearbyen': {
        'country': 'Norway',
        'population': '2548',
        'fact': 'На территории города нельзя умирать, т.к. это привлекает хищников.',
    },
    'Shaven': {
        'country': 'Morocco',
        'population': '35609',
        'fact': 'Город почти полностью выкрашен в голубой цвет.',
    },
    'Whittier': {
        'country': 'USA',
        'population': '272',
        'fact': 'Весь город находится в одном здании - церковь, клиника, магазины, полиция и почти все жители.',
    }
}
for city, city_info in cities.items():
    print(f'\nCity: {city}')
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f'\tCountry: {country.title()}')
    print(f'\tPopulation: {population}')
    print(f'\tFact: {fact}')