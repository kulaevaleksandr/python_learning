# 5.2. Больше условий: Программа должна выдавать по крайней мере один истинный и один ложный результат для следующих видов проверок:
# Проверка равенства и неравенства строк
name = 'Саша'
my_name = 'Саша'
print(name == my_name)
print(name != my_name)

# Проверки с использованием функции lower()
car = 'Volvo'
my_car = 'voLvo'
print(car == my_car)
print(car.lower() == my_car.lower())

# Числовые проверки равенства и неравенства, условий «больше», «меньше», «больше или равно», «меньше или равно»
age = 26
min_age = 18
print(age == min_age)
print(age != min_age)
print(age > min_age)
print(age < min_age)
print(age >= min_age)
print(age <= min_age)

# Проверки с ключевым словом and и or
gender = 'men'
age = 20
if (gender == 'men') and (age > 18):
    print('Взрослый мужчина')

gender = 'men'
age = 20
if (gender == 'men') or (age > 18):
    print('Как минимум одно из условий подходит')

# Проверка вхождения элемента в список
popular_languages = ['JS', 'Python', 'Java']
learn_language = 'Python'
if learn_language in popular_languages:
    print(f"Я изучаю один из популярнейших языков - {learn_language}.")

# Проверка отсутствия элемента в списке
popular_languages = ['JS', 'Python', 'Java']
language = 'C++'
if language not in popular_languages:
    print(f"{language} - не входит в топ популярных языков программирования.")
