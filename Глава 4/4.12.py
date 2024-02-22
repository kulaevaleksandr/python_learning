# Использовать циклы для вывода обоих списков любимой еды
my_foods = ['солянка', 'хачапури', 'чизкейк']
friend_foods = my_foods[:]

my_foods.append('паста')
friend_foods.append('мороженое')

for my_food in my_foods:
    print(f'Моя любимая еда: {my_food}')

for friend_food in friend_foods:
    print(f'Любимая еда моего друга: {friend_food}')
