# 5.10. Проверка имен пользователей: выполните следующие действия для создания программы, моделирующей проверку уникальности имен пользователей
current_users = ['Саша', 'Керик', 'Макс', 'Таня', 'Санчоус', 'Кирюха', 'Женя', 'Арина']
new_names = ['Тимоха', 'Руслан', 'Макс', 'Керик', 'Матвей']
current_users_lower = [user.lower() for user in current_users]
for new_name in new_names:
    if new_name.lower() in current_users_lower:
        print(f"Имя {new_name} уже используется. Выберите другое имя")
    else:
        print(f"Имя {new_name} свободно. Отличный выбор!")
