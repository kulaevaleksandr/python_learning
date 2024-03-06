# 7.10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они
# хотели провести отпуск. Включите блок кода для вывода результатов опроса

responses = {}

polling_active = True

while polling_active:
    name = input('\nВаше имя? ')
    response = input('Где бы вы хотели провести отпуск? ')

    responses[name] = response

    repeat = input('\nХотите ли дать другому человеку ответить? (Да/Нет) ')
    if repeat.lower() == 'нет':
        polling_active = False

print('\n---Результаты опроса---')
for name, response in responses.items():
    print(f'{name.title()} хочет провести отпуск в {response}.')
