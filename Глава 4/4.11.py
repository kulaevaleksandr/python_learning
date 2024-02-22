# Скопировать список пицц в любимые пиццы друга, добавить в каждый список по элементу и вывести каждый список циклом
pizzas = ['пепперони', 'маргарита', 'три сыра']
friend_pizzas = pizzas[:]
pizzas.append('грибная')
friend_pizzas.append('4 сезона')
print('Я люблю такие пиццы, как:')
for pizza in pizzas:
    print(pizza.title())
print('\nЛюбимые пиццы друга')
for pizza in friend_pizzas:
    print(pizza.title())
